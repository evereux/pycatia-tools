import os
from pathlib import Path
import random
import string

from pycatia.exception_handling.exceptions import CATIAApplicationException
from pypdf import PdfWriter

from application.pycatia_scripts.the_document import PTDrawingDocument


def random_str(length: int = 8):

    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def save_as(exclude_sheets: str = None, target_directory: str = None):

    output = {
        'errors': [],
        'data': None,
    }

    try:
        pt_drawing_document = PTDrawingDocument()
        if not pt_drawing_document.is_drafting_document():
            output['errors'].append('Active document is not CATPart.')
            return output
    except CATIAApplicationException:
        output['errors'].append('No active document.')
        return output

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
