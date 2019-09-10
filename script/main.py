from docx import Document


def create_doc(department,account_num,s_5hr,s_10hr,p_10hr,p_12hr,p_15hr,total_primary,thanksgiving_hours,spring_hours,christmas_hours,summer_hours):
    document = Document()

    # Table Layout
    table = document.add_table(rows = 4, cols = 12)
    table.allow_autofit = False
    table.style = 'TableGrid'

    # Merging Selected Cells
    table.cell(0,0).merge(table.cell(0,11))
    table.cell(1,0).merge(table.cell(1,1))
    table.cell(1,2).merge(table.cell(1,3))
    table.cell(1,4).merge(table.cell(1,6))
    table.cell(1,7).merge(table.cell(1,11))
    table.cell(2,0).merge(table.cell(2,1))
    table.cell(3,0).merge(table.cell(3,1))

    # Setting Table Labels
    table.cell(1,3).text = "Secondary"
    table.cell(1,4).text = "Primary"
    table.cell(2,2).text = "5hr"
    table.cell(2,3).text = "10hr"
    table.cell(2,4).text = "10hr"
    table.cell(2,5).text = "12hr"
    table.cell(2,6).text = "15hr"
    table.cell(2,7).text = "Total Primary"
    table.cell(2,8).text = "Thanksgiving Hours"
    table.cell(2,9).text = "Spring Hours"
    table.cell(2,10).text = "Christmas Hours"
    table.cell(2,11).text = "Summer Hours"
    table.cell(3,0).text = "Final Allocation on AY 19-20"

    # Setting Table Data
    table.cell(0,0).text = department + " (" + str(account_num) + ")"
    table.cell(3,2).text = str(s_5hr)
    table.cell(3,3).text = str(s_10hr)
    table.cell(3,4).text = str(p_10hr)
    table.cell(3,5).text = str(p_12hr)
    table.cell(3,6).text = str(p_15hr)
    table.cell(3,7).text = str(total_primary)
    table.cell(3,8).text = str(thanksgiving_hours)
    table.cell(3,9).text = str(spring_hours)
    table.cell(3,10).text = str(christmas_hours)
    table.cell(3,11).text = str(summer_hours)

    document.save('%s-Allocation-AY19-20.docx' % department)



def main():
    pass

if __name__=="__main__":
    main()
