from pycatia.in_interfaces.documents import Documents
from pycatia.product_structure_interfaces.product_document import ProductDocument


def get_output() -> dict:

    output: dict = {
        'errors': [],
        'data': {}, # can be overwritten with a string for simple success reports otherwise use a mapping.
        'output_file': None
    }

    return output

def check_part_number_exists(documents: Documents, output: dict, part_number: str):
        """
        For creation of new parts and products ensure that the part_number 
        doesn't already exist in the session.

        :param documents:
        :param output_:
        :param part_number:
        """
 
        for doc in documents:
            filename = doc.name
            extension = filename.rsplit(".")[-1].lower()
            if extension == 'catpart' or extension == 'catproduct':
                ref_product = ProductDocument(doc.com_object).product
                if ref_product.part_number == part_number:
                    print(ref_product.part_number, part_number)
                    output['errors'].append(f'Part number must be unique in the session. "{part_number}" already in use.')
                    return output
        
        return output


