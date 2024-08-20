import random
import string

from pycatia.product_structure_interfaces.product import Product
from pycatia.product_structure_interfaces.products import Products

from application.pycatia_scripts.the_document import PTProductDocument


def tmp_string(size=6, chars: str = string.ascii_letters) -> str:
    """

    :param size:
    :param chars:
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))


def renumber_instances(
        reference_products: Products,
        tmp_name: str or False = False
):
    """
    :param Products reference_products:
    :param str or False tmp_name:
    :return:
    """
    collection_counter = {}
    for product in reference_products:
        part_number = product.part_number
        keys = collection_counter.keys()
        if part_number not in keys:
            collection_counter[part_number] = 1
        else:
            collection_counter[part_number] += 1
        new_name = part_number
        if tmp_name:
            new_name = new_name + '.' + tmp_name
        new_name = new_name + '.' + str(collection_counter[part_number])
        product.name = new_name


def main() -> bool:

    try:
        pt_product_doc = PTProductDocument()
    except AttributeError:
        return False
    product_document = pt_product_doc.product_document
    product = pt_product_doc.product

    ref_product = product.reference_product
    reference_products = ref_product.products

    tmp_str = tmp_string()
    # We need to run this function twice.
    # The first time renames the instances with temporary names.
    renumber_instances(reference_products, tmp_str)
    renumber_instances(reference_products)

    return True
