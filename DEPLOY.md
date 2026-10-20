# Putting BrineFlow on a public web address

The tool is **one self-contained file** (`index.html`, ~200 KB, no build step, no server code),
so any static web host will serve it. Viewers need no account and no login — they just open the URL.

Whichever host you pick, the rule is the same: the file must be named **`index.html`** and sit at the
root of what you upload.

---

## Option 1 — your own lab site (recommended)

You already have `swatlab.or.kr`. Putting the tool there costs nothing extra, keeps it on the lab's
own domain, and makes it unmistakably a SWAT Lab product:

```
http://www.swatlab.or.kr/tools/brineflow/
```

Send `index.html` to whoever maintains the site and ask them to place it in a new folder, e.g.
`/tools/brineflow/index.html`. There is nothing to configure — no database, no PHP, no permissions
beyond "serve this file". Any web admin can do it in a couple of minutes.

**Best for:** a tool you want associated with the lab, linked from the site, cited in a paper.

---

## Option 2 — GitHub Pages (free, permanent, no command line needed)

1. Create a free account at <https://github.com> if you don't have one.
2. Click **New repository** → name it `brineflow` → tick **Public** → **Create**.
3. On the repo page click **Add file → Upload files**, drag `index.html` in, then **Commit changes**.
4. Go to **Settings → Pages**. Under *Source* choose **Deploy from a branch**, branch **main**,
   folder **/ (root)** → **Save**.
5. Wait about a minute. Your address appears at the top of that page:

```
https://<your-username>.github.io/brineflow/
```

To update it later, upload the new `index.html` over the old one — the URL never changes.

**Note:** on the free plan a Pages site must be **public**, so anyone with the link (and search
engines) can reach it. That is fine for a tool; don't use it for unpublished data.

If you'd rather use the command line, git is already installed here:

```bash
cd "C:/Users/user/OneDrive/Desktop/desal-train-tool" && git init && git add index.html && git commit -m "BrineFlow" && git branch -M main
```

then add your repo as a remote and push.

---

## Option 3 — Netlify Drop (fastest, ~30 seconds)

1. Go to <https://app.netlify.com/drop>.
2. Drag the whole **`desal-train-tool` folder** onto the page.
3. A live URL appears immediately, e.g. `https://cheerful-otter-12ab34.netlify.app`.
4. Sign up free to keep the site permanently and to rename it to something like
   `swatlab-brineflow.netlify.app`. Unclaimed drops are temporary.

**Best for:** getting a link to a colleague in the next minute.

Cloudflare Pages (<https://pages.cloudflare.com>) works the same way with a free account and has no
bandwidth limit worth worrying about.

---

## What not to use

| | |
|---|---|
| **OneDrive / SharePoint / Google Drive** | They serve HTML as a *download or preview*, not as a running page. The tool will not work. |
| **Email attachment** | Many mail systems strip or block `.html`. Zip it first, or send a link. |
| **A hosting service that needs a sign-in** | Works, but every viewer needs an account. Fine for private use, no good for sharing a link. |

---

## Comparison

| | Viewer login | Cost | Public? | Update effort |
|---|---|---|---|---|
| Lab site | none | free (already paid) | your choice | send file to web admin |
| GitHub Pages | none | free | must be public | re-upload one file |
| Netlify / Cloudflare | none | free | public by default | drag the folder again |

---

## After it is live

- Test it once in a private/incognito window — that proves no login is involved.
- The page works offline too, so anyone can still save it and run it locally.
- Nothing is sent anywhere: every calculation runs in the viewer's own browser, so there is no
  server cost, no traffic limit worth worrying about, and no data leaves their machine.
