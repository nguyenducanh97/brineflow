# -*- coding: utf-8 -*-
"""Build the published page: encrypt app-unlocked.html into index.html.

    python build.py <id> <password>
    python build.py swat mypassword

app-unlocked.html is the source you edit. index.html is the build artefact that
gets committed and served - it holds only ciphertext plus a small unlock screen.
The ID and password are combined, stretched through PBKDF2-HMAC-SHA256 (310,000
rounds) into an AES-256-GCM key, and are never written into the output.

Note that both files live in this repository, so the unlock screen keeps the page
out of search results and away from casual visitors, but anyone reading the
repository can open app-unlocked.html directly.

Every build draws a fresh random salt and IV, so re-running with a new password
makes the previous one unable to decrypt the file at all.

Needs: pip install cryptography
The same thing can be done without Python by opening protect.html in a browser.
"""
import base64, hashlib, io, os, re, sys

try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:
    sys.exit("needs the cryptography package:  pip install cryptography")

HERE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(HERE, "app-unlocked.html")
OUT  = os.path.join(HERE, "index.html")
TMPL = os.path.join(HERE, "protect.html")

if len(sys.argv) != 3:
    sys.exit(__doc__)
UID, PWD = sys.argv[1], sys.argv[2]


def unescape(t):
    """Resolve the escapes a JS template literal resolves, in one pass.

    protect.html carries the unlock page inside a backtick template literal, so
    its \\\\ , \\` , \\$ and <\\/script> sequences have to be collapsed the way the
    browser would collapse them before the page is written out.
    """
    out, i = [], 0
    while i < len(t):
        if t[i] == '\\' and i + 1 < len(t) and t[i+1] in '\\`$/':
            out.append(t[i+1]); i += 2
        else:
            out.append(t[i]); i += 1
    return ''.join(out)


tmpl = io.open(TMPL, encoding='utf-8').read()
page = unescape(re.search(r"const PAGE = `(.*?)`;\n</script>", tmpl, re.S).group(1))

plain = io.open(SRC, encoding='utf-8').read()
salt, iv = os.urandom(16), os.urandom(12)
key = hashlib.pbkdf2_hmac('sha256', (UID + '\n' + PWD).encode('utf-8'), salt, 310000, 32)
ct = AESGCM(key).encrypt(iv, plain.encode('utf-8'), None)

b64 = lambda x: base64.b64encode(x).decode()
out = (page.replace('__SALT__', b64(salt))
           .replace('__IV__',   b64(iv))
           .replace('__CT__',   b64(ct)))

# the separator between ID and password must survive templating intact, or the
# key derived here will not match the one the browser derives
sep = re.search(r"encode\(id\+'([^']*)'\+pw\)", out)
assert sep and sep.group(1) == '\\n', "separator mangled: %r" % (sep and sep.group(1))

for probe in (PWD, UID + '\n' + PWD, 'P3CASES', 'MEMLIB'):
    assert probe not in out, "the build leaked %r" % probe[:20]

# LF endings, so the committed file matches what the server returns
io.open(OUT, 'w', encoding='utf-8', newline="\n").write(out)
print("%s  %.0f KB  ->  %s  %.0f KB" % (
    os.path.basename(SRC), len(plain)/1024, os.path.basename(OUT), len(out)/1024))
print("locked with ID %r - commit index.html to publish it" % UID)
