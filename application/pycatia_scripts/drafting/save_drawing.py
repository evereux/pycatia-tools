import os
from pathlib import Path
import random
import string

from pypdf import PdfWriter

from application.pycatia_scripts.common import get_output
from application.support.documents import get_drawing_document


def random_str(length: int = 8):

    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def save_as_pdf(exclude_sheets: str | None = None, target_directory: str | None = None):
    """
    :param str include_sheets: a comma delimited str of sheet names
    """

    pt_drawing_document, errors = get_drawing_document()

    output = get_output()

    output['errors'] = output['errors'] + errors

    if not target_directory:
        target_directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    if not Path(target_directory).is_dir():
        output['errors'].append(f'"{target_directory}" is not a directory.')

    if output['errors']:
        return output

    excluded = [o.strip() for o in exclude_sheets.split(",") if o]

    drawing_doc = pt_drawing_document.drawing_document
    random_prefix = random_str()
    temp_name = random_prefix + drawing_doc.name
    pdf_name = Path(target_directory, temp_name).with_suffix('.pdf')

    drawing_doc.export_data(pdf_name, 'pdf', overwrite=True)

    # find all the temp named pdfs files and combine them
    pdfs = sorted(Path(target_directory).glob(f'{random_prefix}*.*'))

    target_pdf = Path(target_directory, drawing_doc.name).with_suffix('.pdf')
    delete_files = []
    merger = PdfWriter()
    for pdf in pdfs:
        if not any(i in str(pdf) for i in excluded):
            merger.append(pdf)
        delete_files.append(pdf)

    try:
        merger.write(target_pdf)
        merger.close()
        for f in delete_files:
            f.unlink()
        output['data'] = f'PDF "{target_pdf}" created.'
    except:
        output['errors'].append('There was a problem creating PDF or deleting source PDFS.')

    return output


def save_as_dxf(include_sheets: str | None, target_directory: str | None = None):
    """
    :param str include_sheets: a comma delimited str of sheet names
    """

    pt_drawing_document, errors = get_drawing_document()

    output = get_output()

    output['errors'] = output['errors'] + errors

    if not target_directory:
        target_directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    if not Path(target_directory).is_dir():
        output['errors'].append(f'"{target_directory}" is not a directory.')

    if output['errors']:
        return output

    included = [o.strip() for o in include_sheets.split(",") if o]

    drawing_doc = pt_drawing_document.drawing_document
    dxf_name = Path(target_directory, drawing_doc.name).with_suffix('.dxf')

    drawing_doc.export_data(dxf_name, 'dxf', overwrite=True)

    # todo: deleted sheets not included.
    sheets = drawing_doc.sheets
    # get the sheet names and replace any "." with "_" as CATIA does this to the output filenames.
    sheet_names = [sheet.name.replace('.', '_') for sheet in sheets]
    drawing_name = drawing_doc.name.rsplit('.', 1)[0]
    # generate a list of dxf sheet names
    dxf_sheets = [Path(target_directory, f"{drawing_name}_{s}.dxf") for s in sheet_names]
    output_sheets = []
    for d in dxf_sheets:
        if d.exists:
            for i in included:
                if i not in d.stem:
                    os.remove(d)
                else:
                    output_sheets.append(d)
    dxfs = ', '.join([str(s) for s in output_sheets])
    output['data'] = f'DXFs "{dxfs}" created.'

    return output
