# joannelsmikle.com — Independent Director Landing Page

Project handoff for GitHub hosting. Client: Dr. Joanne L. Smikle (existing Tenacity IT client, smiklespeaks.com). Goal: a separate, single-purpose site positioning her as an **Independent Director** candidate for board nominating committees and executive search firms. Reference site for tone/simplicity: annmdanner.com. Client is away until July 7; not urgent.

## Deliverables in hand

| File | What it is |
|---|---|
| `joannelsmikle-landing.html` | Complete one-page site. Fully self-contained — headshot is base64-embedded, fonts load from Google Fonts CDN. No build step, no JS dependencies. |
| `Smikle_Board_Resume_2026.pdf` | Two-page designed board resume matching the site (garnet #7a1f2b / charcoal #232326, Fraunces + Source Serif 4 + Archivo). This is the target of the site's "Download Board Resume" button. |

## Repo / hosting plan (GitHub Pages)

1. New repo (suggest `tenacityit/joannelsmikle` or client org), default branch `main`.
2. Rename `joannelsmikle-landing.html` → `index.html` at repo root.
3. **Optional cleanup:** extract the base64 headshot into `img/headshot.jpg` and point the `<img src>` at it — nicer diffs, better caching. Source image is a 400×500 JPG (~128 KB).
4. Add the PDF as `Smikle_Board_Resume_2026.pdf` at root; wire the "Download Board Resume" button to it (`href` + `download` attribute).
5. Enable GitHub Pages (deploy from `main` / root). Add `CNAME` file containing `joannelsmikle.com`.
6. DNS at the registrar:
   - Apex `A` records → GitHub Pages IPs: 185.199.108.153 / .109.153 / .110.153 / .111.153
   - `www` CNAME → `<org>.github.io`
   - Enable "Enforce HTTPS" in Pages settings once the cert issues.
7. Add basic `<meta>` OG tags + favicon before launch (not yet in the file).

## Placeholders to resolve before launch (waiting on client, back July 7)

- [ ] Contact **email** — appears in hero buttons is fine, and in the dark "Board Inquiries" section + PDF contact block (currently `placeholder@joannelsmikle.com` / `[Email placeholder]`)
- [ ] **LinkedIn URL** — hero button + contact section + PDF
- [ ] **Phone** (PDF only, optional)
- [ ] **Doctorate details** (field + institution) — should be added near credentials; board audiences expect it
- [ ] **Board logos** (Saybrook, American Brain Foundation, Heritage Ministry, ElevateMeD) — optional logo strip, high impact for recruiters
- [ ] Confirm podcast listener count — source doc said both 29,000 and 30,000; both deliverables currently standardized on **30,000**
- [ ] Optional: one-line **sector focus** statement (profile clusters: healthcare/post-acute care, higher ed, human-capital-heavy orgs)

## Design tokens (if edits are needed)

- Ink `#232326` · Ink-soft `#4c4c52` · Paper `#faf9f6` · Paper-deep `#f1efe9` · Garnet `#7a1f2b` · Line `#dcd8cf`
- Display: **Fraunces** (500/600) · Body: **Source Serif 4** · Labels/UI: **Archivo** (600, tracked-out uppercase)
- Signature element: the "board ledger" — each board as a row with an uppercase garnet role label and pill tags for committee assignments. Keep this pattern if adding/editing boards.

## Content source

All copy derives from the client's board resume docx (`Bd_Resume_SMIKLE_1_2025.docx`). Boards listed: Saybrook University (Trustee; Chair, Institutional Advancement), American Brain Foundation (Director, Governance Cmte), Heritage Ministry Charitable Care Network (Director), Maryland Oversight Committee on Quality of Care (gubernatorial appointment), ElevateMeD (National Advisory Board), Bridges to Housing Stability (past, three terms; Secretary). Do not add claims not present in the source doc without client sign-off.
