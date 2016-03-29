import StringIO
import xlsxwriter
from django.utils.translation import ugettext

from .models import Person

def WriteToExcel(person_list):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("People")

    #excel styles
    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    cell = workbook.add_format({
        'align': 'left',
        'valign': 'top',
        'text_wrap': True,
        'border': 1
    })
    cell_center = workbook.add_format({
        'align': 'center',
        'valign': 'top',
        'border': 1
    })

    #write title
    person_text = ugettext("everyone")
    title_text = u"{0} {1}".format(ugettext("Information for"), person_text)
    #merge cells
    worksheet_s.merge_range('B2:I2', title_text, title)

    #write header
    worksheet_s.write(4, 0, ugettext("No"), header)
    worksheet_s.write(4, 1, ugettext("Name"), header)
    worksheet_s.write(4, 2, ugettext("Service"), header)
    worksheet_s.write(4, 3, ugettext("Bio"), header)
    worksheet_s.write(4, 4, ugettext("Country"), header)
    worksheet_s.write(4, 5, ugettext("State"), header)
    worksheet_s.write(4, 6, ugettext("City"), header)
    worksheet_s.write(4, 7, ugettext("MeetupID"), header)
    worksheet_s.write(4, 8, ugettext("URL"), header)

    #column widths
    bio_col_width = 25

    #add data to the table
    for idx, data in enumerate(person_list):
        row = 5 + idx
        worksheet_s.write_number(row, 0, idx + 1, cell_center)
        worksheet_s.write_string(row, 1, data.name, cell)
        worksheet_s.write_string(row, 2, data.service, cell)
        worksheet_s.write_string(row, 3, data.bio, cell)
        worksheet_s.write_string(row, 4, data.country, cell)
        worksheet_s.write_string(row, 5, data.state, cell)
        worksheet_s.write_string(row, 6, data.city, cell)
        worksheet_s.write_number(row, 7, data.meetupID, cell)
        worksheet_s.write_string(row, 8, data.url, cell)

    workbook.close()
    xlsx_data = output.getvalue()           #xlsx_data contains the Excel file
    return xlsx_data