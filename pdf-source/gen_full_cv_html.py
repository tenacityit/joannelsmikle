# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '.')
from build_full_cv import (clients, faculty, civic, peer_reviewed, peer_reviewed_upcoming,
                            practitioner, presentations, academic_presentation, early_work)

FONT_DIR = "/Users/blopa/Claude/Tenacity/Websites/joannelsmikle.com/pdf-source/assets/fonts/"

CSS = """
@font-face{font-family:'Archivo';font-weight:400;src:url('assets/fonts/archivo-400.ttf') format('truetype');}
@font-face{font-family:'Archivo';font-weight:500;src:url('assets/fonts/archivo-500.ttf') format('truetype');}
@font-face{font-family:'Archivo';font-weight:600;src:url('assets/fonts/archivo-600.ttf') format('truetype');}
@font-face{font-family:'Archivo';font-weight:700;src:url('assets/fonts/archivo-700.ttf') format('truetype');}
@font-face{font-family:'Source Serif 4';font-weight:400;src:url('assets/fonts/sourceserif4-400.ttf') format('truetype');}
@font-face{font-family:'Source Serif 4';font-weight:600;src:url('assets/fonts/sourceserif4-600.ttf') format('truetype');}
:root{
  --ink:#232326; --ink-soft:#4c4c52; --paper:#faf9f6; --paper-deep:#f1efe9;
  --garnet:#a6121f; --rose:#e5959e; --muted:#8a8781; --line:#dcd8cf;
}
*{margin:0;padding:0;box-sizing:border-box;}
@page{ size: letter; margin: 44pt 54pt 42pt; }
body{
  font-family:'Source Serif 4', Georgia, serif;
  color:var(--ink); line-height:1.5; font-size:9pt; -webkit-font-smoothing:antialiased;
}
a{color:inherit;}

.pdf-header{
  background:var(--ink); border-radius:5pt; border-bottom:3pt solid var(--garnet);
  padding:14pt 20pt 12pt; margin-bottom:18pt;
}
h1{ font-family:'Archivo',sans-serif; font-weight:700; font-size:19pt; letter-spacing:-.01em; color:#fff; margin-bottom:5pt; }
.role{ font-family:'Archivo',sans-serif;font-size:7.6pt;font-weight:600;letter-spacing:.17em;text-transform:uppercase;color:var(--rose); }
.contact-line{ font-family:'Archivo',sans-serif;font-size:7.6pt;color:rgba(250,249,246,.72);margin-top:7pt; }
.contact-line a{color:rgba(250,249,246,.72);}
.contact-line .sep{color:var(--rose);}

h2{
  font-family:'Archivo',sans-serif;font-weight:600;font-size:9pt;
  letter-spacing:.14em;text-transform:uppercase;color:var(--garnet);
  border-bottom:1pt solid var(--line);padding-bottom:4pt;margin:20pt 0 9pt;
  break-after:avoid;
}
h2:first-of-type{margin-top:0;}
.section-note{font-size:8.6pt;color:var(--ink-soft);margin-bottom:8pt;font-style:italic;}

.section p{ font-size:9pt;line-height:1.5;color:var(--ink); }

.prof-list{ list-style:none;margin-top:6pt; }
.prof-list li{ font-size:9pt;color:var(--ink);padding:3pt 0 3pt 14pt;position:relative;line-height:1.42; }
.prof-list li::before{content:"\\2022";color:var(--garnet);position:absolute;left:2pt;font-weight:700;}

.detail-list{list-style:none;margin-top:8pt;}
.detail-list li{font-size:8.8pt;color:var(--ink-soft);padding:3pt 0 3pt 14pt;position:relative;line-height:1.45;}
.detail-list li::before{content:"\\2022";color:var(--garnet);position:absolute;left:2pt;font-weight:700;}

.client-grid{ column-count:3; column-gap:24pt; font-size:8.3pt;color:var(--ink-soft);margin-top:4pt; }
.client-grid div{ break-inside:avoid; padding:2.5pt 0; border-bottom:1pt solid var(--line); }

.role-block{ padding:9pt 0;border-bottom:1pt solid var(--line);break-inside:avoid; }
.role-block:last-child{border-bottom:none;}
.role-head{display:flex;justify-content:space-between;gap:12pt;align-items:baseline;}
.role-main{font-family:'Archivo',sans-serif;font-weight:700;font-size:9.4pt;}
.role-org{font-size:8.6pt;color:var(--ink-soft);margin-top:1.5pt;}
.role-years{font-family:'Archivo',sans-serif;font-size:7.6pt;font-weight:600;color:var(--garnet);white-space:nowrap;text-align:right;}
.role-desc{font-size:8.6pt;color:var(--ink-soft);margin-top:4pt;line-height:1.45;}
.course-list{margin-top:5pt;font-size:8pt;color:var(--ink-soft);}
.course-list .lbl{font-family:'Archivo',sans-serif;font-weight:600;font-size:6.8pt;letter-spacing:.1em;text-transform:uppercase;color:var(--garnet);margin-bottom:3pt;}
.course-list span{display:inline;}

.civic-row{padding:8pt 0;border-bottom:1pt solid var(--line);break-inside:avoid;}
.civic-row:last-child{border-bottom:none;}
.civic-head{display:flex;justify-content:space-between;gap:12pt;align-items:baseline;}
.civic-role{font-family:'Archivo',sans-serif;font-weight:700;font-size:9pt;}
.civic-years{font-family:'Archivo',sans-serif;font-size:7.4pt;font-weight:600;color:var(--garnet);white-space:nowrap;}
.civic-desc{font-size:8.6pt;color:var(--ink-soft);margin-top:3pt;line-height:1.45;}

.edu-row{padding:5pt 0;border-bottom:1pt solid var(--line);font-size:9pt;}
.edu-row:last-child{border-bottom:none;}
.edu-row strong{font-family:'Archivo',sans-serif;font-weight:700;}
.edu-row .note{display:block;font-size:8.3pt;color:var(--ink-soft);margin-top:2pt;}

.pub-list{list-style:none;}
.pub-list li{font-size:8.4pt;color:var(--ink-soft);padding:3pt 0 3pt 14pt;line-height:1.42;border-bottom:1pt solid var(--line);position:relative;}
.pub-list li:last-child{border-bottom:none;}
.pub-list li::before{content:"\\2022";color:var(--garnet);position:absolute;left:2pt;font-weight:700;}

.pub-year-group{margin-top:9pt;break-inside:avoid;}
.pub-year-group:first-child{margin-top:4pt;}
.pub-year{font-family:'Archivo',sans-serif;font-weight:700;font-size:8.6pt;color:var(--garnet);margin-bottom:3pt;}
.pub-year-items{list-style:none;}
.pub-year-items li{font-size:8.4pt;color:var(--ink-soft);padding:2.5pt 0 2.5pt 14pt;line-height:1.42;position:relative;}
.pub-year-items li::before{content:"\\2022";color:var(--garnet);position:absolute;left:2pt;font-weight:700;}

.pres-row{display:flex;gap:10pt;padding:4pt 0;border-bottom:1pt solid var(--line);break-inside:avoid;}
.pres-row:last-child{border-bottom:none;}
.pres-year{font-family:'Archivo',sans-serif;font-size:7.6pt;font-weight:700;color:var(--garnet);width:32pt;flex-shrink:0;padding-top:1pt;}
.pres-body{font-size:8.4pt;color:var(--ink-soft);line-height:1.45;}
.pres-body .venue{color:var(--ink);font-family:'Archivo',sans-serif;font-weight:600;font-size:8pt;}
.pres-body .titles em{font-style:italic;}

.inquiries{ background:var(--ink);border-radius:6pt;padding:11pt 16pt;margin-top:16pt; }
.inquiries .label{font-family:'Archivo',sans-serif;font-size:7pt;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--rose);margin-bottom:6pt;}
.inquiries .line{font-family:'Archivo',sans-serif;font-size:8.4pt;color:var(--paper);}
.inquiries .line a{color:var(--paper);text-decoration:none;}
.inquiries .line .sep{color:var(--rose);}

.doc-note{
  margin-top:18pt;padding-top:10pt;border-top:1pt dashed var(--line);
  font-size:7.6pt;color:var(--muted);font-style:italic;
}
"""

def esc_join_courses(courses):
    return " &nbsp;&middot;&nbsp; ".join(courses)

html = []
html.append('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">')
html.append('<title>Joanne L. Smikle, PhD — Full CV</title>')
html.append(f'<style>{CSS}</style></head><body>')

html.append('<div class="pdf-header">')
html.append('<h1>Joanne L. Smikle, PhD</h1>')
html.append('<div class="role">Principal Consultant &middot; Speaker &middot; Faculty</div>')
html.append('<div class="contact-line">joanne@smiklespeaks.com<span class="sep"> &middot; </span>410.707.8512<span class="sep"> &middot; </span>linkedin.com/in/joannesmikle<span class="sep"> &middot; </span>joannelsmikle.com</div>')
html.append('</div>')

# Professional experience
html.append('<h2>Professional Experience</h2>')
html.append('<p>I bring significant and sustained experience providing consulting to executives in many industry sectors. I partner with leaders to implement sound initiatives that positively impact a range of business issues related to organizational effectiveness, bridging the gap between strategy and operations, succession planning, and skillful talent management. I deliver advice and counsel focused on thoughtful approaches to reaching the organization&rsquo;s long and short-range objectives. Areas of expertise follow:</p>')
html.append('<ul class="prof-list">')
for item in ["Strategy Formulation, Implementation and Evaluation",
             "Human Capital Utilization, Succession Planning, Workforce Best Practices",
             "Executive &amp; Leadership Development",
             "Organizational Effectiveness, Organizational Development, Organizational Change &amp; Organizational Culture"]:
    html.append(f'<li>{item}</li>')
html.append('</ul>')

detail_bullets = [
 "I design an array of customized interactive learning experiences curated to meet each client&rsquo;s individual needs.",
 "I am instrumental in developing and implementing organizational change initiatives. I devise programmatic interventions to transform corporate culture while enhancing performance and productivity. I help clients develop and refine the leadership competencies required to meet current and anticipated business demands.",
 "I develop quantitative and qualitative assessments to measure organizational climate, skillfully using a variety of approaches including focus groups, surveys, and mixed-method measurement strategies. I provide comprehensive analysis of assessment results.",
 "I develop leadership and management development interventions aimed at cultivating the competencies required to meet the organization&rsquo;s strategic objectives.",
 "I assist leaders in analyzing innovations and ensuring that the range of viable options are well-aligned with organizational strategy.",
 "I create comprehensive approaches to succession planning and pipeline development so that key positions have available talent to advance the organization&rsquo;s strategic intentions.",
 "I partner with executives to design innovative, successful approaches for addressing human capital utilization issues that impact performance, productivity, and profit &mdash; partnerships that contribute to the long-term success of client organizations.",
 "I utilize the SmikleSpeaks podcast, with over 33,000 listeners globally, and the SmikleSpeaks YouTube channel to provide virtual leadership learning.",
 "I facilitate strategic planning, retreats, seminars, workshops, and educational experiences for leaders. I conduct needs analyses to plot long-term courses for organizational development, providing systematic approaches to effectively position the organization for results aligned with strategic objectives.",
]
html.append('<ul class="detail-list">')
for b in detail_bullets:
    html.append(f'<li>{b}</li>')
html.append('</ul>')

# Clients
html.append('<h2>Clients</h2>')
html.append('<div class="section-note">Representative public sector, private sector, and nonprofit clients served over three decades of consulting.</div>')
html.append('<div class="client-grid">')
for c in clients:
    html.append(f'<div>{c}</div>')
html.append('</div>')

# Faculty
html.append('<h2>Faculty Appointments</h2>')
for f in faculty:
    html.append('<div class="role-block"><div class="role-head">')
    html.append(f'<div><div class="role-main">{f["role"]}</div><div class="role-org">{f["org"]}</div></div>')
    html.append(f'<div class="role-years">{f["years"]}</div></div>')
    html.append(f'<div class="role-desc">{f["desc"]}</div>')
    if f["courses"]:
        html.append(f'<div class="course-list"><div class="lbl">Courses Taught</div><span>{esc_join_courses(f["courses"])}</span></div>')
    html.append('</div>')

# Civic
html.append('<h2>Memberships, Community Service &amp; Civic Engagement</h2>')
for c in civic:
    html.append('<div class="civic-row"><div class="civic-head">')
    html.append(f'<div class="civic-role">{c["role"]}</div><div class="civic-years">{c["years"]}</div>')
    html.append('</div>')
    html.append(f'<div class="civic-desc">{c["desc"]}</div></div>')

# Education
html.append('<h2>Education</h2>')
html.append('<div class="edu-row"><strong>Doctor of Philosophy, Human and Organizational Systems</strong> &mdash; Fielding Graduate University<span class="note">Dissertation research on employee retention and commitment</span></div>')
html.append('<div class="edu-row"><strong>Master of Arts, Human and Organizational Systems</strong> &mdash; Fielding Graduate University</div>')
html.append('<div class="edu-row"><strong>Bachelor of Arts, Political Science</strong> &mdash; University of Maryland, Baltimore County</div>')

# Peer reviewed publications
html.append('<h2>Selected Peer-Reviewed Publications</h2>')
html.append('<ul class="pub-list">')
for p in peer_reviewed:
    html.append(f'<li>{p}</li>')
html.append('</ul>')
html.append('<div class="section-note" style="margin-top:8pt;">Upcoming:</div>')
html.append('<ul class="pub-list">')
for p in peer_reviewed_upcoming:
    html.append(f'<li>{p}</li>')
html.append('</ul>')

# Practitioner publications
html.append('<h2>Selected Practitioner Publications</h2>')
html.append('<div class="section-note">Author of over ninety articles for practitioner publications. Published works are listed below by year.</div>')
for year, items in practitioner:
    html.append(f'<div class="pub-year-group"><div class="pub-year">{year}</div><ul class="pub-year-items">')
    for it in items:
        html.append(f'<li>{it}</li>')
    html.append('</ul></div>')

# Presentations
html.append('<h2>Selected Presentations</h2>')
html.append('<div class="section-note">Keynote presentations, concurrent and virtual sessions at national and regional conferences.</div>')
for year, venue, titles in presentations:
    titles_html = " &nbsp;&middot;&nbsp; ".join(f'<em>&ldquo;{t}&rdquo;</em>' for t in titles)
    html.append('<div class="pres-row">')
    html.append(f'<div class="pres-year">{year}</div>')
    html.append(f'<div class="pres-body"><span class="venue">{venue}</span><br><span class="titles">{titles_html}</span></div>')
    html.append('</div>')

html.append('<h2>Selected Academic Presentations</h2>')
html.append(f'<div class="pres-row"><div class="pres-body">{academic_presentation}</div></div>')

# Early work experience
html.append('<h2>Early Work Experience</h2>')
html.append('<div class="role-block"><div class="role-head">')
html.append(f'<div><div class="role-main">{early_work["role"]}</div><div class="role-org">{early_work["org"]}</div></div>')
html.append('</div>')
html.append(f'<div class="role-desc">{early_work["desc"]}</div></div>')

# Contact
html.append('<div class="inquiries"><div class="label">Contact</div><div class="line">')
html.append('<a href="mailto:joanne@smiklespeaks.com">joanne@smiklespeaks.com</a><span class="sep"> &middot; </span>')
html.append('<a href="tel:+14107078512">410.707.8512</a><span class="sep"> &middot; </span>')
html.append('<a href="https://www.linkedin.com/in/joannesmikle/" target="_blank" rel="noopener">linkedin.com/in/joannesmikle</a><span class="sep"> &middot; </span>')
html.append('<a href="https://joannelsmikle.com" target="_blank" rel="noopener">joannelsmikle.com</a>')
html.append('</div></div>')

html.append('<div class="doc-note">This is the complete, unabridged version of Dr. Smikle\'s CV, for internal comparison against the condensed 3-page resume. Not yet linked from the live site.</div>')

html.append('</body></html>')

out = "\n".join(html)
outpath = "/Users/blopa/Claude/Tenacity/Websites/joannelsmikle.com/pdf-source/full-cv-complete.html"
with open(outpath, "w", encoding="utf-8") as f:
    f.write(out)
print("wrote", outpath, len(out), "chars")
