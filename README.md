# BrineFlow — multi-stage desalination train simulator

**A product of [SWAT Lab](http://www.swatlab.or.kr/) — Sustainable Water Treatment Laboratory,
Sungkyunkwan University.**

An interactive tool for building SWRO / HPRO / OARO trains, reordering them, changing the
operating parameters of every stage, and reading off the converged mass balance — with the
full calculation shown step by step for every stage.

Built from the hand sketch: `Feed → Pretreatment → SWRO(1) → SWRO(2) → HPRO → OARO → C`,
at 20 °C, 33,000–35,000 mg/L feed, brine concentrated toward 30,000+ mg/L and beyond.

---

## 1. Install

Nothing to install. The whole tool is one self-contained HTML file — no Node, no Python,
no internet connection, no data leaves your machine.

**Requirement:** Chrome or Edge 109+, or Firefox 115+ — any browser from 2023 onward. The SWAT Lab
and SKKU logos are embedded inside the file, so it works with no internet connection.

**Language:** English and Korean. The `🇰🇷 한국어` / `🇬🇧 EN` button in the toolbar switches the whole
interface — panels, fields, messages, the flow diagram, the stream table and the full calculation
narrative. Your choice is remembered.

## 2. Launch

**The simple way**

Double-click `index.html`. It opens in your default browser and is ready to use.

If Windows opens it in something unexpected, right-click → *Open with* → *Google Chrome*
(or Edge), and tick *Always use this app*.

**Make it feel like an app (optional)**

In Chrome or Edge, open the file, then ⋮ menu → *Cast, save and share* → *Install page as app*
(Edge: ⋯ → *Apps* → *Install this site as an app*). You get a desktop icon and a clean window
with no address bar.

**Serve it over localhost (optional)**

Only needed if you want to open it from another machine on your network. From this folder:

```bash
python -m http.server 8000
```

then open `http://localhost:8000` in a browser.

**Share it with colleagues**

Send them `index.html` — it works standalone on any machine. Or say the word and I'll publish
it as a private web page you can hand out by link.

---

## 3. Moving it to another PC

The tool is **one file**. Copy `index.html` anywhere — USB stick, email attachment, network share —
and double-click it. Nothing else is needed.

If it does not open on another machine, it is almost always one of these:

| Symptom | Cause | Fix |
|---|---|---|
| Blank white page | Browser too old (Internet Explorer, or Chrome/Edge before 2023) | Open with a current Chrome or Edge. The page now shows an explanatory message instead of staying blank. |
| Opens as text / code | Windows opened it with Notepad or an editor | Right-click → *Open with* → Chrome, and tick *Always use this app* |
| File is 0 KB, or "cannot be opened" | OneDrive placeholder — the file was never downloaded on that PC | In File Explorer, right-click the file → *Always keep on this device*, wait for the green tick, then copy it |
| Download blocked / "unsafe" | Some mail systems strip `.html` attachments | Put it in a ZIP first, or share it from OneDrive/Drive as a link |
| Equations look run-together | Browser predates MathML support (Chrome < 109) | Update the browser — everything else still works |

Do not open it through the OneDrive **web** viewer: that shows the source instead of running it.
Download the file first, then open the local copy.

If you need it to work on any device without copying files at all, the whole tool can be published
as a private web link — say the word and I'll set that up.

## 4. Using it — five-minute tour

**Presets.** The dropdown at the top right loads three starting points. *Sketch example* is
your diagram: SWRO → SWRO → HPRO → OARO.

**Feed panel (top left).** Flow, TDS in g/L (35 g/L = 35,000 mg/L), temperature, and the
pretreatment water loss. Everything downstream recalculates as you type.

**Building the train.**

| Action | How |
|---|---|
| Add a stage | the `+ SWRO` / `+ HPRO` / `+ OARO` buttons under the train |
| Reorder | drag a stage by its ⠿ handle, or use ▲ ▼ |
| Duplicate / delete | the ⧉ and ✕ buttons on the stage header |
| Rename | click the stage name and type |

**Per-stage parameters.**

- *Stream routing* — where this stage's feed comes from. `Previous stage — concentrate`
  follows reordering automatically; or pick any named stream from any other stage. `…take % of it`
  splits a stream between two consumers. `+ add a blended / recycled feed stream` mixes a second
  stream in (this is how you close a recycle loop).
- *Operating specification* — either fix the **water recovery**, or fix the **target concentrate
  TDS** and let the tool solve the recovery it needs from the salt balance.
- Salt rejection and concentration-polarisation factor β.
- *Hydraulics & energy* — net driving pressure, channel pressure drop, pump efficiency, and the
  membrane pressure limit (SWRO ≈ 83 bar, HPRO ≈ 120 bar, OARO ≈ 70 bar). Exceed it and the stage
  turns red with an explanation.

**OARO stages** have an extra sweep-side panel. The sweep is what makes OARO work: a *saline*
stream on the permeate side cancels most of the brine's osmotic pressure, so the stage keeps
concentrating below 70 bar. A pure-water sweep would defeat the purpose — it makes the stage
behave like an HPRO. Rule of thumb: sweep TDS at 60–80 % of the stage feed TDS.

In a real cascade that sweep is the diluate of the neighbouring stage, so once the salinities
line up, set it as an internal stream instead of the external default — the solver handles the
resulting recycle loop. Until you do, the tool tells you how much external water is entering and
how much diluate is leaving unrouted.

**Every field explains itself.** Each input carries a `?` with what the parameter means, a
realistic range, and what it actually changes — in whichever language you have selected. Fields that
only matter in certain configurations appear only then: *Make-up water TDS* shows up once a stage
sweeps with fresh water, and *ERD efficiency* only while the recovery device is switched on.

Three parameters deliberately change no process result, which the tooltips say plainly:
*Electricity price* and *Operating hours* drive the cost figures only, and *Max. pressure* is a
feasibility check that is never used in the calculation.

**Advisory notes.** Anything that stops the design being buildable — a stage over its pressure
rating, a routing error, a diverging recycle — is always shown in Performance Summary. Softer
advice (an OARO suggestion, external sweep water, unrouted diluate, the converged confirmation) is
folded away behind the **notes** checkbox in that panel's header, which shows how many are waiting.
Tick it when you want the commentary; leave it off for a clean panel.

**Reading the results.** KPI tiles (which count up as values change), the process flow diagram with the
converged numbers on every arrow, the stream table with the overall water and salt balance check, and the
calculation details.

**Calculation details.** One expandable block per stage. Each step is numbered and the equations are properly
typeset — symbolic form, then the same equation with your numbers substituted, then the result, with the `=`
signs aligned down the block:

> C_p  =  (1 − R) · C_f · β
> &nbsp;&nbsp;&nbsp;&nbsp;=  (1 − 0.9940) · 35.000 · 1.15
> &nbsp;&nbsp;&nbsp;&nbsp;=  **0.2415** g/L

Covered per stage: inlet mixing, permeate quality, recovery, salt balance with its closure check, a molality /
osmotic-coefficient / osmotic-pressure table for every stream, the required feed pressure against the membrane
limit, and pumping power. The first block documents the whole model; the last rolls the train up to SEC.

The math is real MathML rendered by the browser — no libraries, no internet. It builds only when you open a
block, so typing stays instant.

**Exports.** `💾 Save` stores a configuration you can reload later; `⭳ CSV` opens in Excel; `📄 Report` writes
the complete derivation, equations and all, to a text file.

---

## 5. Look and feel

The tool ships in a dark **control-room theme**: a drifting technical grid, rising micro-bubbles
behind the workspace, glass panels that light up on hover, and a live telemetry strip in the header
reading solver state, sweep count, residual, recovery and specific energy.

`☀ Light` in the toolbar switches to a daylight theme for printing or projector use — every colour,
including the stage colours in the diagram, follows the theme, and the technical grid is dropped for a
clean white background. Your choice is remembered.

In the flow diagram the pipes glow, carry marching dashes and travelling droplets whose **speed
follows the actual flow rate**, and each stage shows a pressure gauge of how close it runs to its own
rating (green → amber → red). Stages over the limit pulse. KPI tiles count up and grow a sparkline of
their own recent history as you edit.

`◉ Motion` pauses all of it — bubbles, droplets, sweeps — for a still, quiet view. The diagram keeps
every pipe, arrow and label; only the movement stops, so a paused diagram is the one to screenshot for
a report. The page also respects your operating system's reduced-motion setting automatically.

## 6. The workspace

Every section is a panel you can rearrange:

| | |
|---|---|
| **Move a panel** | drag it by the ⠿ grip in its header — within a column or across to the other one |
| **Resize a panel** | drag the ribbed handle along its bottom edge |
| **Resize the columns** | drag the vertical divider between them |
| **Collapse** | the ▾ button — useful for parking the input panels while you read results |
| **Focus one panel** | the ⤢ button blows it up over the whole window; `Esc` or a click outside returns |
| **Start over** | `⌗ Reset layout` in the toolbar |

Your layout *and* your process configuration are remembered in the browser, so closing the tab and coming back
picks up where you left off. (This needs the file opened from disk; a preview inside another app may block
browser storage.)

## 7. Automation

**⚡ Auto-tune**, under the stage list. Give it a target — say 95 % — and it sets the recovery of every
recovery-specified stage so that stage runs at 95 % of its own pressure limit, working down the train and then
doing a second pass to settle the interactions. It bisects on recovery, re-solving the whole network each time,
and highlights each stage as it lands on it.

On the default train it lifts recovery from 63 % to 65 % with all four stages sitting right under their ratings.
Watch for a stage that collapses to ~1 % recovery: that means its inlet is already at the limit and the stage is
earning nothing — the tool flags it, and it is a sign to delete that stage or convert it to OARO.

**Motion.** Pipes carry an animated dash whose speed follows the actual flow rate, KPI numbers count up when
they change, stages over pressure pulse red. `◉ Motion` in the toolbar pauses all of it, and the page respects
your operating system's reduced-motion setting automatically.

---

## 8. What the model does and doesn't do

**Included**

- Water and salt balance on every stage, converged across recycles by successive substitution
  (under-relaxed, with a divergence guard for loops that feed themselves).
- Osmotic pressure by van 't Hoff with a concentration-dependent osmotic coefficient fitted to
  NaCl — 27.1 bar at 35 g/L, 56 bar at 70 g/L, 103 bar at 120 g/L, all at 20 °C. This matters:
  a plain linear π ∝ C is 10–20 % off in the brine-concentration range these trains work in.
- Permeate quality from observed rejection and concentration polarisation, `C_p = (1 − R)·C_f·β`.
- Required feed pressure at the limiting (concentrate) end, checked against the membrane rating.
- Inter-stage pressure carry-over — a stage fed by an upstream concentrate that is already above
  its required pressure needs no booster pump.
- Pump power, ERD recovery on the streams leaving the train, SEC, energy cost.

**Deliberately not included** — the natural next layer, if this proves useful:

- Element-by-element flux profile and membrane area from A/B transport coefficients
  (the tool sets flux implicitly through the net driving pressure you specify).
- Scaling and fouling limits: LSI, CaSO₄ / SrSO₄ saturation, silica — the real ceiling on
  recovery in the HPRO/OARO range, well before the pressure limit.
- Multi-ion speciation (the solution is treated as a NaCl equivalent), boron, and pH effects.
- Capex, membrane replacement, and pump curves — energy only.

The osmotic-pressure model is the one thing worth checking against your own data before quoting
numbers from this: swap the fit in the `phiOsm` function near the top of the script if you have
a better correlation for your feed.
