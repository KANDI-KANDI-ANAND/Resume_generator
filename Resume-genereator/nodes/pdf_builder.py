from schemas import ResumeClass
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap

def PDF_builder_node(state: ResumeClass):

    optimized_resume_text = state["optimized_resume"]

    file_path = "optimized_resume.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)

    width, height = letter

    left_margin = 35
    right_margin = width - 35
    usable_width = right_margin - left_margin

    y = height - 50
    line_height = 13

    def new_page():
        nonlocal y
        c.showPage()
        y = height - 50
        c.setFont("Helvetica",10)

    def draw_line():
        nonlocal y
        c.line(left_margin, y, right_margin, y)
        y -= 11

    def draw_section_heading(text):
        nonlocal y
        c.setFont("Helvetica-Bold", 11)
        c.drawString(left_margin, y, text)
        y -= 8
        draw_line()

    def draw_paragraph(text):
        nonlocal y
        c.setFont("Helvetica", 10)

        wrapped = textwrap.wrap(text, width=110)

        for line in wrapped:
            if y < 60:
                new_page()

            c.setFont("Helvetica",10)
            c.drawString(left_margin, y, line)
            y -= (line_height + 4) 

    def draw_bullet(text):
        nonlocal y
        c.setFont("Helvetica", 10)

        wrapped = textwrap.wrap(text, width=105)

        for i, line in enumerate(wrapped):
            if y < 60:
                new_page()

            if i == 0:
                c.drawString(left_margin + 5, y, "• " + line)
            else:
                c.drawString(left_margin + 18, y, line)

            y -= line_height


    lines = [l.strip() for l in optimized_resume_text.split("\n") if l.strip()]

    name = lines[0]
    contact_line = lines[1]

    c.setFont("Helvetica-Bold",20)
    c.drawCentredString(width / 2, y, name)
    c.drawCentredString(width / 2 + 0.3, y, name)
    y -= 30

    c.setFont("Helvetica",9)
    c.drawCentredString(width / 2, y, contact_line)
    y -= 18

    current_section = None

    for line in lines[2:]:

        line = line.strip()

        if not line:
            continue

        if line.startswith("PROJECTS:"):
            draw_section_heading("PROJECTS")
            line = line.replace("PROJECTS:", "").strip()

            if line:
                c.setFont("Helvetica-Bold", 11)
                c.drawString(left_margin, y, line)
                y -= line_height

            current_section = "PROJECTS"
            continue

        if line.isupper() or line.endswith(":"):

            draw_section_heading(line)

            current_section = line
            continue

        if line.startswith("•"):

            draw_bullet(line[1:].strip())
            continue

        if ":" in line and current_section == "TECHNICAL SKILLS":

            category, skills = line.split(":", 1)

            c.setFont("Helvetica-Bold", 11)
            c.drawString(left_margin, y, category + ":")

            c.setFont("Helvetica", 10)

            wrapped = textwrap.wrap(skills.strip(), width=90)

            first_line = True

            for w in wrapped:

                if y < 60:
                    new_page()

                if first_line:
                    c.drawString(left_margin + 120, y, w)
                    first_line = False
                else:
                    c.drawString(left_margin + 120, y, w)

                y -= line_height

            continue

        if current_section == "PROJECTS" and not line.startswith("•") and not line.startswith("http"):
            c.setFont("Helvetica-Bold",11)
            c.drawString(left_margin, y, line)
            y -= line_height
            continue

        if current_section in ["WORK EXPERIENCE:", "INTERNSHIPS:"] and not line.startswith("•"):
            c.setFont("Helvetica-Bold", 11)
            c.drawString(left_margin, y, line)
            y -= line_height
            continue
        
        draw_paragraph(line)

    c.save()

    return {
        "pdf_path": file_path,
    }