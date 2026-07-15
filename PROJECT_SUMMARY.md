# joannelsmikle.com — Independent Director Landing Page

Project handoff for GitHub hosting. Client: Dr. Joanne L. Smikle (existing Tenacity IT client, smiklespeaks.com). Goal: a separate, single-purpose site positioning her as an **Independent Director** candidate for board nominating committees and executive search firms. Reference site for tone/simplicity: annmdanner.com. Client is away until July 7; not urgent.

## Deliverables in hand

| File | What it is |
|---|---|
| `index.html` | Complete one-page site, first-person copy. Headshot lives at `img/headshot.jpg`, fonts load from Google Fonts CDN. No build step, no JS dependencies. |
| `Smikle_Board_Resume_2026.pdf` | Two-page board resume, first-person copy. As of July 15, sans-serif throughout (Archivo, all weights) per client request — no longer matches the site's Fraunces/Source Serif 4 pairing, see note below. This is the target of the site's "Download Board Resume" button. |
| `pdf-source/board-resume.html` | Source for the PDF above — a standalone print-styled HTML file. There's no InDesign/Figma source for this document; it's rendered to PDF via headless Chrome (`--print-to-pdf`). Edit this file and re-render rather than hand-editing the PDF. Fonts are self-hosted (`pdf-source/assets/fonts/`) — see font note below before assuming Google Fonts CDN links work here. |
| `Smikle_Full_Resume_2026.pdf` | Three-page general-purpose resume (same design system as the board resume), target of the site's new "Download Full Resume" button. Condensed from her academic CV — see notes below. |
| `pdf-source/full-resume.html` | Source for the full resume, same headless-Chrome print-to-pdf workflow as the board resume source. |

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

- [x] Contact **email** — switched to `joanne@smiklespeaks.com` (her existing working mailbox) in both files, replacing `joanne@joannelsmikle.com`. Sidesteps the MX/deliverability setup that would've been needed on the new domain.
- [x] **LinkedIn URL** — as of July 15, `https://www.linkedin.com/in/joannesmikle/` (direct profile URL) everywhere — see revision round eight below for why it changed from the `linkedin.smiklespeaks.com` redirect. Also added the rest of her live social pattern (`instagram`/`spotify`/`podcast`/`youtube`.smiklespeaks.com) to the site's contact section.
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
- [x] **Email deliverability** — resolved by switching the mailto: to `joanne@smiklespeaks.com` (see above) instead of standing up mail on the new domain.
- [x] Sixth revision round (July 15): "full consistency" pass — the Professional Experience closing paragraph ("Instrumental in developing...") converted to first person in both site and PDF, matching the rest of the copy.
- [x] Seventh revision round (July 15) — new **full resume** deliverable, added per client request ("my colleague suggested we create a button for my full resume... please do what you think is necessary to make it a 2, no more than 3 page resume"). Source: client's academic CV (`JLSmikle CV July 2026 BOARD.doc`, 7 pages as delivered — converted with macOS `textutil`, no LibreOffice on this machine). Condensed to 3 pages, same design system as the board resume, reusing the already-approved Professional Experience copy verbatim for consistency. Condensing decisions, for client review:
  - **Kept in full:** Professional Experience summary + expertise list, Board & Governance ledger, Civic Engagement, Education, all 5 peer-reviewed publications.
  - **Condensed:** ~60 consulting clients down to ~18 representative names across public sector/corporate/associations; ~90 practitioner articles down to a summary line + 5 representative titles; ~60 conference presentations down to 8 recent/notable ones; faculty appointments kept but course lists dropped.
  - **Board tenure years:** left off the board ledger (matches the ageism decision above) — but faculty-appointment and publication years were kept, since a resume with zero dates anywhere would read as evasive rather than youthful. Flag if this distinction isn't what she wants.
  - **Phone number discrepancy:** the CV lists `410-707-8512` (mobile) and `410-730-7867` (office) — different from the `410-730-4867` already confirmed by the client and live everywhere else. Used the already-confirmed number and did not add the CV's numbers; needs a quick client confirmation on which is correct.
  - **LinkedIn URL:** CV lists the raw `linkedin.com/in/joannesmikle/` profile URL; used the established `linkedin.smiklespeaks.com` redirect instead for consistency with the rest of the site. *(Superseded July 15 — see below, now uses the direct URL everywhere.)*
  - No photo on this document (the source CV didn't have one either, and page budget was tight) — say the word if she wants it added.
- [x] Eighth revision round (July 15) — client feedback on "the bio" (board resume PDF):
  - **Board tenure years — reversed.** Client's colleague suggested adding them; client provided exact date ranges and said *"you only need to add this information to the bio"* — so years now show on each board row in `Smikle_Board_Resume_2026.pdf` only. Not added to the site or the full resume; ask before doing so.
  - **Font bug found and fixed.** The Google Fonts CDN (`fonts.googleapis.com`) was not reliably loading during headless Chrome's `--print-to-pdf`, so both PDFs were silently falling back to system fonts (Georgia/Times/Helvetica) — this is almost certainly what the client meant by "looks so much like Times Roman" and the "crooked J" (Fraunces' capital J has a pronounced swash that reads oddly when it's actually rendering as a substituted Times-Bold). Root-caused by checking the PDF's embedded font list (`page.get_fonts()` in PyMuPDF) — it showed base-14 fallback fonts, not the intended webfonts. Fixed for both PDFs by downloading the actual font files and self-hosting them via local `@font-face` (`pdf-source/assets/fonts/*.ttf`, `file://`-relative `src: url(...)`), removing the network dependency entirely. Confirmed fix by re-checking the embedded font list after re-rendering — both PDFs now embed the real fonts.
  - **Board resume switched to sans-serif** (Archivo only, all weights) per client's explicit request, on top of the font-embedding fix — this was a design change, not just a bug fix. The site and the full resume were **not** changed and still use Fraunces + Source Serif 4 + Archivo — flagging this inconsistency since "full consistency" has mattered to her before; say the word if the full resume or site should switch too.
  - Removed the "BOARD RESUME · INDEPENDENT DIRECTOR" eyebrow line from the top of the PDF header entirely.
  - PDF footer changed from "— BOARD RESUME" to "— INDEPENDENT DIRECTOR".
  - **LinkedIn URL changed** from the `linkedin.smiklespeaks.com` redirect to the direct profile URL `https://www.linkedin.com/in/joannesmikle/`, everywhere it appears: the site (hero button + contact section), the board resume PDF, and the full resume PDF. Note: the redirect was actually working correctly (verified — it 301s to the right profile URL); what she's seeing when she clicks it is LinkedIn showing her its "self-view" edit mode because she's logged in as herself. Any visitor who isn't logged in as her sees the normal public profile. Switching to the direct URL doesn't change that behavior, but it's what she asked for.
  - Thought Leadership section in the PDF now matches the site exactly: added the descriptive sentence under each stat, and matched the site's labels ("Published Articles" / "Podcast Listeners" / "Years Consulting" instead of the PDF's previous, more formal wording).
  - **Not done — blocked:** client said "change the headshot to the new one I sent," but no new photo came through in this message and nothing matching in Downloads. Still using IMG_8516 (gray sweater) on both the board resume and the site. Need her to resend.
  - Client also said she's sending fresh full-resume content "today" via her colleague's suggestion — worth flagging to her that `Smikle_Full_Resume_2026.pdf` already exists and is live (built July 15 from her academic CV, see revision round seven above), in case what she sends is meant to replace rather than duplicate it.

## Design tokens (if edits are needed)

- Ink `#232326` · Ink-soft `#4c4c52` · Paper `#faf9f6` · Paper-deep `#f1efe9` · Deep red `#f50603` (client-specified, July 13) · Line `#dcd8cf`
- Fonts differ by document as of July 15:
  - **Site (`index.html`) and full resume (`pdf-source/full-resume.html`):** Display **Fraunces** (500/600) · Body **Source Serif 4** · Labels/UI **Archivo** (600, tracked-out uppercase)
  - **Board resume (`pdf-source/board-resume.html`) only:** **Archivo** throughout (400/500/600/700), no serif — client's explicit request, see revision round eight
- PDFs must self-host their fonts as local files under `pdf-source/assets/fonts/` and reference them with relative `@font-face` `src: url(...)` paths — the Google Fonts CDN link tag does not reliably load during headless Chrome's `--print-to-pdf`, causing silent fallback to system fonts. Always check `page.get_fonts()` (PyMuPDF) after rendering a new/changed PDF to confirm the intended fonts actually embedded, not base-14 fallbacks (Times/Georgia/Helvetica).
- Signature element: the "board ledger" — each board as a row with an uppercase deep-red role label and pill tags for committee assignments. Keep this pattern if adding/editing boards.

## Content source

All copy derives from the client's board resume docx (`Bd_Resume_SMIKLE_1_2025.docx`). Boards listed: Saybrook University (Trustee; Chair, Institutional Advancement), American Brain Foundation (Director, Governance Cmte), Heritage Ministry Charitable Care Network (Director), Maryland Oversight Committee on Quality of Care (gubernatorial appointment), ElevateMeD (National Advisory Board), Bridges to Housing Stability (past, three terms; Secretary). Do not add claims not present in the source doc without client sign-off.
