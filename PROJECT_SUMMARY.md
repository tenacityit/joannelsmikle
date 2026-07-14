# joannelsmikle.com — Independent Director Landing Page

Project handoff for GitHub hosting. Client: Dr. Joanne L. Smikle (existing Tenacity IT client, smiklespeaks.com). Goal: a separate, single-purpose site positioning her as an **Independent Director** candidate for board nominating committees and executive search firms. Reference site for tone/simplicity: annmdanner.com. Client is away until July 7; not urgent.

## Deliverables in hand

| File | What it is |
|---|---|
| `index.html` | Complete one-page site, first-person copy. Headshot lives at `img/headshot.jpg`, fonts load from Google Fonts CDN. No build step, no JS dependencies. |
| `Smikle_Board_Resume_2026.pdf` | Two-page designed board resume matching the site (deep red #f50603 / charcoal #232326, Fraunces + Source Serif 4 + Archivo), first-person copy. This is the target of the site's "Download Board Resume" button. |
| `pdf-source/board-resume.html` | Source for the PDF above — a standalone print-styled HTML file. There's no InDesign/Figma source for this document; it's rendered to PDF via headless Chrome (`--print-to-pdf`). Edit this file and re-render rather than hand-editing the PDF. |

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

- [x] Contact **email** — confirmed as `joanne@joannelsmikle.com`, now live in both files. DNS side still to do: MX/forwarding so it delivers to her Office 365 smiklespeaks.com mailbox (domain alias in the M365 tenant preferred so she can also send-as), plus SPF/DKIM/DMARC on joannelsmikle.com.
- [x] **LinkedIn URL** — confirmed as `linkedin.smiklespeaks.com`, live in hero button + contact section + PDF. Also added the rest of her live social pattern (`instagram`/`spotify`/`podcast`/`youtube`.smiklespeaks.com) to the site's contact section.
- [x] **Phone** — confirmed as `410-730-4867`, live in PDF Board Inquiries line.
- [ ] **Doctorate details** (field + institution) — should be added near credentials; board audiences expect it
- [ ] **Board logos** (Saybrook, American Brain Foundation, Heritage Ministry, ElevateMeD) — optional logo strip, high impact for recruiters
- [ ] Confirm podcast listener count — source doc said both 29,000 and 30,000; both deliverables currently standardized on **30,000**
- [x] First revision round (July 13) applied: verbiage removed from top, deep red `#a6121f` replaces burgundy, new headshot (IMG_8516), "Independent Director" + "Governance · Strategy · Human Capital Utilization" under name, client's rewritten bio verbatim, "Three Terms" removed from Bridges entry — all in both HTML and PDF.
- [x] Second revision round (July 13): swapped in a photo where her hand isn't cropped out (IMG_8480), rewrote all bio/body copy on the site and in the PDF from third person ("she"/"Dr. Smikle") to first person ("I"). Page `<title>`/meta description tags were deliberately left in third person — that's the standard convention for search-result and social-share snippets, not "page" copy a reader sees.
- [ ] Optional: one-line **sector focus** statement (profile clusters: healthcare/post-acute care, higher ed, human-capital-heavy orgs)
- [x] Board tenure years — declined by client (ageism concern, same reasoning as the "20+ years" change below). Not adding these.
- [x] Third revision round (July 13): accent color changed from `#a6121f` to `#f50603` (site + PDF) — see updated design tokens below. PDF: removed the cursive logo/name from the upper-left corner (redundant with the name next to the photo), name next to photo changed to "Joanne L. Smikle, PhD" (dropped "Dr."), added a new "Professional Experience" section (paragraph + 4-item list, verbatim client copy) above "Consulting Experience", added `smiklespeaks.com` to Board Inquiries alongside `joannelsmikle.com`. Site: removed Instagram/Spotify from contact links, added `smiklespeaks.com` link, replaced the 6-cell "What I Bring to the Boardroom" grid with the same new "Professional Experience" section as the PDF. Both: Saybrook tags now show she chairs both Institutional Advancement and Nominating & Governance; podcast stat reads "leaders and learners in 24 countries"; "30+ years" changed to "20+ years" (and "three decades" → "two decades" in PDF body copy) per client's ageism concern; published-articles line now reads "business publications that focus on...".
- [x] Fourth revision round (July 13): removed the site's top nav bar entirely ("Joanne L. Smikle, Ph.D." wordmark, upper-left) — client wants no name/branding above the hero photo, matching the PDF's cleaned-up header. Hero section now starts at the top of the page.
- [x] Fifth revision round (July 13), client-approved and asked to go live: new consistent headshot (IMG_8512, gray dress) cropped to face/shoulders, used in both site and PDF, replacing the red-shirt hand photo. Site H1 changed "Dr. Joanne L. Smikle" → "Joanne L. Smikle, PhD" (matching the PDF). LinkedIn button on site changed from outline to solid red (`btn-primary`), matching Download Board Resume. Hero bio paragraph rewritten (client's exact wording) in both site and PDF. Added client's new closing paragraph ("Instrumental in developing and implementing organizational change initiatives...") to the bottom of the Professional Experience section in both site and PDF.
- [ ] **smiklespeaks.com → joannelsmikle.com back-link** — client wants the link to go both ways. smiklespeaks.com is a separate WordPress site on Cloudways, not in this repo — someone with access to that site needs to add the reverse link.
- [ ] **Email deliverability** — `joanne@joannelsmikle.com` is currently just a `mailto:` link; there are no MX records on the domain, so nothing actually receives mail there yet. Client wants replies to come from `joannelsmikle.com` specifically. Needs: MX records (or M365 domain alias if she wants to send-as from her existing smiklespeaks.com mailbox), plus SPF/DKIM/DMARC. Registrar + M365 admin access required — outside this repo.

## Design tokens (if edits are needed)

- Ink `#232326` · Ink-soft `#4c4c52` · Paper `#faf9f6` · Paper-deep `#f1efe9` · Deep red `#f50603` (client-specified, July 13) · Line `#dcd8cf`
- Display: **Fraunces** (500/600) · Body: **Source Serif 4** · Labels/UI: **Archivo** (600, tracked-out uppercase)
- Signature element: the "board ledger" — each board as a row with an uppercase deep-red role label and pill tags for committee assignments. Keep this pattern if adding/editing boards.

## Content source

All copy derives from the client's board resume docx (`Bd_Resume_SMIKLE_1_2025.docx`). Boards listed: Saybrook University (Trustee; Chair, Institutional Advancement), American Brain Foundation (Director, Governance Cmte), Heritage Ministry Charitable Care Network (Director), Maryland Oversight Committee on Quality of Care (gubernatorial appointment), ElevateMeD (National Advisory Board), Bridges to Housing Stability (past, three terms; Secretary). Do not add claims not present in the source doc without client sign-off.
