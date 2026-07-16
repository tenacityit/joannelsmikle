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
:root{
  --ink:#232326; --ink-soft:#4c4c52; --paper:#faf9f6; --paper-deep:#f1efe9;
  --garnet:#f50603; --inquiry-label:#e5959e; --footer-muted:#8a8781; --line:#dcd8cf;
}
*{margin:0;padding:0;box-sizing:border-box;}
@page{ size: letter; margin: 46pt 54pt 44pt; }
body{
  font-family:'Archivo', Helvetica, Arial, sans-serif; font-weight:400;
  color:var(--ink); line-height:1.5; font-size:9pt; -webkit-font-smoothing:antialiased;
}
a{color:inherit;}
.pdf-header{ padding-bottom:8pt;margin-bottom:14pt;border-bottom:3pt solid var(--garnet); }
h1{ font-family:'Archivo',sans-serif; font-weight:700; font-size:19pt; letter-spacing:-.005em; margin-bottom:5pt; }
.role{ font-family:'Archivo',sans-serif;font-size:8.5pt;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--garnet); }
.contact-line{ font-family:'Archivo',sans-serif;font-size:8pt;color:var(--ink-soft);margin-top:6pt; }
.contact-line a{color:var(--ink-soft);}

h2{
  font-family:'Archivo',sans-serif;font-weight:700;font-size:12.5pt;color:var(--ink);
  border-bottom:1pt solid var(--line);padding-bottom:4pt;margin:20pt 0 8pt;
  break-after:avoid;
}
h2:first-of-type{margin-top:0;}
.section-note{font-size:8.6pt;color:var(--ink-soft);margin-bottom:8pt;}

.section p{ font-size:9pt;line-height:1.42;color:var(--ink-soft); }

.prof-list{ list-style:none;margin-top:6pt; }
.prof-list li{ font-size:9pt;color:var(--ink);padding:3pt 0 3pt 13pt;position:relative;border-bottom:1pt solid var(--line); }
.prof-list li:last-child{border-bottom:none;}
.prof-list li::before{content:"\\2014";color:var(--garnet);position:absolute;left:0;}

.detail-list{list-style:none;margin-top:8pt;}
.detail-list li{font-size:8.8pt;color:var(--ink-soft);padding:3pt 0 3pt 13pt;position:relative;line-height:1.4;}
.detail-list li::before{content:"\\2022";color:var(--garnet);position:absolute;left:0;font-weight:700;}

.client-grid{ column-count:3; column-gap:24pt; font-size:8.3pt;color:var(--ink-soft);margin-top:4pt; }
.client-grid div{ break-inside:avoid; padding:2.5pt 0; border-bottom:1pt solid var(--line); }

.role-block{ padding:9pt 0;border-bottom:1pt solid var(--line);break-inside:avoid; }
.role-block:last-child{border-bottom:none;}
.role-head{display:flex;justify-content:space-between;gap:12pt;align-items:baseline;}
.role-main{font-family:'Archivo',sans-serif;font-weight:600;font-size:9.4pt;}
.role-org{font-size:8.6pt;color:var(--ink-soft);margin-top:1pt;}
.role-years{font-family:'Archivo',sans-serif;font-size:7.6pt;font-weight:600;color:var(--ink-soft);white-space:nowrap;text-align:right;}
.role-desc{font-size:8.6pt;color:var(--ink-soft);margin-top:4pt;line-height:1.4;}
.course-list{margin-top:5pt;font-size:8pt;color:var(--ink-soft);}
.course-list .lbl{font-family:'Archivo',sans-serif;font-weight:600;font-size:7pt;letter-spacing:.06em;text-transform:uppercase;color:var(--garnet);margin-bottom:3pt;}
.course-list span{display:inline;}

.civic-row{padding:8pt 0;border-bottom:1pt solid var(--line);break-inside:avoid;}
.civic-row:last-child{border-bottom:none;}
.civic-head{display:flex;justify-content:space-between;gap:12pt;align-items:baseline;}
.civic-role{font-family:'Archivo',sans-serif;font-weight:600;font-size:9pt;}
.civic-years{font-family:'Archivo',sans-serif;font-size:7.6pt;font-weight:600;color:var(--garnet);white-space:nowrap;}
.civic-desc{font-size:8.6pt;color:var(--ink-soft);margin-top:3pt;line-height:1.4;}

.edu-row{padding:5pt 0;border-bottom:1pt solid var(--line);font-size:9pt;}
.edu-row:last-child{border-bottom:none;}
.edu-row strong{font-family:'Archivo',sans-serif;font-weight:600;}
.edu-row .note{display:block;font-size:8.3pt;color:var(--ink-soft);margin-top:2pt;}

.pub-list{list-style:none;}
.pub-list li{font-size:8.4pt;color:var(--ink-soft);padding:3pt 0;line-height:1.4;border-bottom:1pt solid var(--line);}
.pub-list li:last-child{border-bottom:none;}

.pub-year-group{margin-top:9pt;break-inside:avoid;}
.pub-year-group:first-child{margin-top:4pt;}
.pub-year{font-family:'Archivo',sans-serif;font-weight:700;font-size:8.6pt;color:var(--garnet);margin-bottom:3pt;}
.pub-year-items{list-style:none;}
.pub-year-items li{font-size:8.4pt;color:var(--ink-soft);padding:2.5pt 0;line-height:1.4;}

.pres-row{display:flex;gap:10pt;padding:4pt 0;border-bottom:1pt solid var(--line);break-inside:avoid;}
.pres-row:last-child{border-bottom:none;}
.pres-year{font-family:'Archivo',sans-serif;font-size:7.6pt;font-weight:700;color:var(--garnet);width:32pt;flex-shrink:0;padding-top:1pt;}
.pres-body{font-size:8.4pt;color:var(--ink-soft);line-height:1.4;}
.pres-body .venue{color:var(--ink);}
.pres-body .titles em{font-style:italic;}

.inquiries{ background:var(--ink);border-radius:6pt;padding:9pt 14pt;margin-top:16pt; }
.inquiries .label{font-family:'Archivo',sans-serif;font-size:7.5pt;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--inquiry-label);margin-bottom:5pt;}
.inquiries .line{font-family:'Archivo',sans-serif;font-size:8.6pt;color:var(--paper);}
.inquiries .line a{color:var(--paper);text-decoration:underline;text-decoration-color:rgba(250,249,246,.45);}

.doc-note{
  margin-top:18pt;padding-top:10pt;border-top:1pt dashed var(--line);
  font-size:7.6pt;color:var(--footer-muted);font-style:italic;
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
html.append('<div class="contact-line">joanne@smiklespeaks.com &nbsp;&middot;&nbsp; 410.707.8512 &nbsp;&middot;&nbsp; linkedin.com/in/joannesmikle &nbsp;&middot;&nbsp; joannelsmikle.com</div>')
html.append('</div>')

# Professional experience
html.append('<h2>Professional Experience</h2>')
html.append('<p>I bring significant and sustained experience providing consulting to executives and leaders in many industry sectors. I partner with executives to implement sound initiatives that positively impact a range of business issues. I deliver advice and counsel to executives concerned with reaching the organization&rsquo;s most positive, powerful potential. Areas of expertise follow:</p>')
html.append('<ul class="prof-list">')
for item in ["Strategy Formulation, Implementation and Evaluation",
             "Human Capital Utilization, Succession Planning, Workforce Best Practices",
             "Executive &amp; Leadership Development",
             "Organizational Effectiveness, Organizational Development, Organizational Change &amp; Organizational Culture"]:
    html.append(f'<li>{item}</li>')
html.append('</ul>')

detail_bullets = [
 "I design an array of customized interactive learning experiences curated to meet each client&rsquo;s individual needs.",
 "I am instrumental in developing and implementing organizational change initiatives. I devise programmatic interventions to change corporate culture while enhancing performance and productivity. I help clients develop and refine the competencies required to meet current and anticipated business demands, with particular emphasis on strategically improving stakeholder relations.",
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
html.append('<a href="mailto:joanne@smiklespeaks.com">joanne@smiklespeaks.com</a> &nbsp;&middot;&nbsp; ')
html.append('<a href="tel:+14107078512">410.707.8512</a> &nbsp;&middot;&nbsp; ')
html.append('<a href="https://www.linkedin.com/in/joannesmikle/" target="_blank" rel="noopener">linkedin.com/in/joannesmikle</a> &nbsp;&middot;&nbsp; ')
html.append('<a href="https://joannelsmikle.com" target="_blank" rel="noopener">joannelsmikle.com</a>')
html.append('</div></div>')

html.append('<div class="doc-note">This is the complete, unabridged version of Dr. Smikle\'s CV, for internal comparison against the condensed 3-page resume. Not yet linked from the live site.</div>')

html.append('</body></html>')

out = "\n".join(html)
outpath = "/Users/blopa/Claude/Tenacity/Websites/joannelsmikle.com/pdf-source/full-cv-complete.html"
with open(outpath, "w", encoding="utf-8") as f:
    f.write(out)
print("wrote", outpath, len(out), "chars")
