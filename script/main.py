from docx import Document
from docx.shared import Inches

def create_doc(title,header):
    document = Document()
    document.add_heading(title,0)
    table = document.add_table(rows=4, cols=10)
    header_cells = table.rows[0].cells
    header_cells[0].text = header
    records = (
    (1, '', 'Secondary','','Primary','','','','','',''),
    (2, '', '5hr','10hr','10hr','12hr','15hr','Total Primary','Thanksgiving Hours','Spring Hours','Christmas Hours','Summer Hours')
    )
    document.save('dd.docx')


def main():
    create_doc("The heading",'The Header')

if __name__=="__main__":
    main()
