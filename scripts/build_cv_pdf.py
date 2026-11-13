#!/usr/bin/env python3
"""Optionally export the current website CV. Never run automatically on deploy."""
from pathlib import Path
from html import escape
import argparse
import yaml
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, default=ROOT / 'assets/pdf/Jiho_Hwang_CV.pdf')
args = parser.parse_args()
cv = yaml.safe_load((ROOT / '_data/cv.yml').read_text())
font_root = Path('/usr/share/fonts/truetype/dejavu')
for name, filename in [('CVSerif','DejaVuSerif.ttf'),('CVSerifBold','DejaVuSerif-Bold.ttf'),('CVSerifItalic','DejaVuSerif-Italic.ttf')]:
    path = font_root / filename
    if not path.is_file():
        raise SystemExit('Install DejaVu Serif fonts to generate the CV PDF.')
    pdfmetrics.registerFont(TTFont(name, str(path)))
pdfmetrics.registerFontFamily('CVSerif', normal='CVSerif', bold='CVSerifBold', italic='CVSerifItalic', boldItalic='CVSerifBold')
ink = colors.HexColor('#20252b')
muted = colors.HexColor('#555f69')
styles = {
    'name': ParagraphStyle('Name',fontName='CVSerifBold',fontSize=24,leading=30,textColor=ink,spaceAfter=7),
    'subtitle': ParagraphStyle('Subtitle',fontName='CVSerif',fontSize=10.4,leading=14.2,textColor=ink,spaceAfter=4),
    'contact': ParagraphStyle('Contact',fontName='CVSerif',fontSize=9,leading=13,textColor=muted,spaceAfter=5),
    'section': ParagraphStyle('Section',fontName='CVSerifBold',fontSize=11.3,leading=15,textColor=ink,spaceBefore=12,spaceAfter=4,keepWithNext=True),
    'body': ParagraphStyle('Body',fontName='CVSerif',fontSize=9.8,leading=13.5,textColor=ink,spaceAfter=4),
    'entry': ParagraphStyle('Entry',fontName='CVSerifBold',fontSize=10.0,leading=13.8,textColor=ink,spaceAfter=3),
    'period': ParagraphStyle('Period',fontName='CVSerif',fontSize=8.5,leading=12,textColor=muted),
    'bullet': ParagraphStyle('Bullet',fontName='CVSerif',fontSize=9.6,leading=13.1,leftIndent=10,firstLineIndent=-8,textColor=ink,spaceAfter=3),
}
e = lambda value: escape(str(value))
p = lambda text, style='body': Paragraph(text, styles[style])
story=[]
def section(title):
    story.extend([p(e(title),'section'), HRFlowable(width='100%',thickness=0.4,color=colors.HexColor('#aeb6be'),spaceAfter=7)])
def short_date(value):
    for month, short in [('January','Jan'),('February','Feb'),('March','Mar'),('April','Apr'),('August','Aug'),('September','Sep'),('October','Oct'),('November','Nov'),('December','Dec')]:
        value = value.replace(month, short)
    return value

def row(period,title,place='',points=(),detail=''):
    right=[p(e(title),'entry')]
    if place: right.append(p(e(place)))
    if detail: right.append(p(e(detail)))
    right.extend(p('• '+e(point),'bullet') for point in points)
    table=Table([[p(e(short_date(period)),'period'),right]],colWidths=[108,393],hAlign='LEFT')
    table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(0,0),12),('RIGHTPADDING',(1,0),(1,0),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
    story.append(table)
identity=cv['identity']
story += [p(e(identity['name']),'name'),p(e(identity['role'])+' · '+e(identity['institution']),'subtitle')]
mail=e(identity['email']); github=e(identity['github'])
story += [p(f'<link href="mailto:{mail}">{mail}</link>  ·  <link href="{github}">GitHub</link>  ·  <link href="https://jirrong.github.io/jhhwang/">Website</link>','contact'),Spacer(1,4)]
section('Education')
for entry in cv['education']:
    row(entry['dates'],entry['degree'],entry['institution'],detail=entry['detail'])
section('Research Experience')
for entry in cv['research_experience']:
    row(entry['dates'],entry['title'],entry['institution'],entry['points'])
section('Honors and Awards')
for entry in cv['awards']:
    row(entry['date'],entry['title'],entry['organization'])
story.append(PageBreak())
story += [p(e(identity['name'])+' — Curriculum Vitae','subtitle'),Spacer(1,5)]
section('Conference Presentations')
for work in cv['presentations']:
    story += [p(e(work['title']),'entry'),p(e(work['authors']))]
    for event in work['events']:
        story.append(p('• <b>'+e(event['meeting'])+'</b>, '+e(event['date'])+'. '+e(event['detail']),'bullet'))
section('Activities')
for entry in cv['activities']:
    row(entry['dates'],entry['title'],entry['institution'])
section('Professional Affiliations')
for entry in cv['affiliations']:
    story.append(p('• '+e(entry),'bullet'))
section('Skills')
skill_rows = [[p(e(entry['label']),'entry'), p(e(entry['items']))] for entry in cv['skills']]
skills_table = Table(skill_rows, colWidths=[130,371], hAlign='LEFT')
skills_table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
story.append(skills_table)
section('Research Interests')
for entry in cv['research_interests']:
    story.append(p('<b>'+e(entry['title'])+'.</b> '+e(entry['description'])))

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('CVSerif',8)
    canvas.setFillColor(muted)
    canvas.drawString(47,27,'Jiho Hwang · Curriculum Vitae')
    canvas.drawRightString(A4[0]-47,27,str(doc.page))
    canvas.restoreState()
args.output.parent.mkdir(parents=True,exist_ok=True)
doc=SimpleDocTemplate(str(args.output),pagesize=A4,leftMargin=47,rightMargin=47,topMargin=42,bottomMargin=43,title='Jiho Hwang — Curriculum Vitae',author='Jiho Hwang',subject='Academic curriculum vitae',invariant=1)
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print(args.output)
