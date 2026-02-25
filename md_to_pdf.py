import os
from fpdf import FPDF
import markdown2
import re

def create_pdf(md_file, pdf_file, title):
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Clean markdown a bit for simple text PDF
    # Remove # and replace with bold header-like lines
    lines = text.split('\n')
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add a Unicode font for better symbol support if needed, 
    # but for now we'll stick to core fonts and clean the text.
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, title, ln=True, align='C')
    pdf.ln(10)
    
    pdf.set_font("Arial", size=11)
    
    for line in lines:
        try:
            if line.startswith('# '):
                pdf.set_font("Arial", 'B', 14)
                pdf.cell(0, 10, line[2:].strip(), ln=True)
                pdf.set_font("Arial", size=11)
            elif line.startswith('## '):
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(0, 8, line[3:].strip(), ln=True)
                pdf.set_font("Arial", size=11)
            elif line.startswith('### '):
                pdf.set_font("Arial", 'B', 11)
                pdf.cell(0, 7, line[4:].strip(), ln=True)
                pdf.set_font("Arial", size=11)
            elif line.strip().startswith('- '):
                # Bullet point
                pdf.set_x(15) # Fixed indent
                # Use a bullet character that is safe for core fonts
                content = line.strip()[2:]
                pdf.multi_cell(0, 6, "- " + content)
            elif line.strip() == '---':
                pdf.line(10, pdf.get_y(), 200, pdf.get_y())
                pdf.ln(5)
            else:
                # Multi-line text for paragraphs
                if line.strip():
                    # Remove common markdown symbols like **
                    clean_line = re.sub(r'\*\*(.*?)\*\*', r'\1', line)
                    clean_line = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_line)
                    # Replace symbols and sanitize for latin-1
                    clean_line = clean_line.replace('`', '"').replace('₹', 'Rs.')
                    # Sanitize for latin-1 (standard PDF font limit)
                    sanitized = ""
                    for char in clean_line:
                        try:
                            char.encode('latin-1')
                            sanitized += char
                        except UnicodeEncodeError:
                            sanitized += "?"
                    pdf.set_x(10)
                    pdf.multi_cell(0, 6, sanitized)
                else:
                    pdf.ln(4)
        except Exception as e:
            # print(f"Error on line: {line[:20]}...") 
            pass # Skip lines that cause issues

    pdf.output(pdf_file)
    print(f"Created {pdf_file}")

if __name__ == "__main__":
    create_pdf('features.md', 'features.pdf', 'Kissan Connect: Feature Guide')
    create_pdf('learning_guide.md', 'learning_guide.pdf', 'Kissan Connect: Beginner\'s Learning Guide')
