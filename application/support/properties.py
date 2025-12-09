from pycatia.exception_handling import CATIAApplicationException
from pycatia.product_structure_interfaces.product import Product
from werkzeug.datastructures import ImmutableMultiDict
from win32.lib.pywintypes import com_error

from application.pycatia_scripts.settings import product_template

default_property_list = [
    'part_number',
    'revision',
    'nomenclature',
    'definition',
]

user_defined_property_list = [key for key in product_template['user_ref_properties']]


def get_properties(product: Product | None, type_: str):
    """

    :param product:
    :param type_: Must be either default or user
    :return:
    """
    property_list = []
    if type_ == 'default':
        property_list = default_property_list
    elif type_ == 'user':
        property_list = user_defined_property_list

    properties = {}

    for property in property_list:
        try:
            properties[property] = ''
            if product:
                properties[property] = getattr(product, property)
        except AttributeError:
            properties[property] = ''
            if type_ == 'user':
                # get the value from the product itself, if set, otherwise use template default.
                user_ref_properties = None
                if product:
                    user_ref_properties = product.user_ref_properties
                try:
                    if user_ref_properties:
                        cad_property = user_ref_properties.item(property)
                        properties[property] = cad_property.value
                    else:
                        properties[property] = ''
                except CATIAApplicationException:
                    properties[property] = product_template['user_ref_properties'][property]

    return properties


def update_properties(product: Product, form: ImmutableMultiDict):
    """

    :param product:
    :param form:
    :return:
    """

    for key in form.keys():
        if key in default_property_list:
            setattr(product, key, form.get(key))
        if key in user_defined_property_list:
            user_ref_properties = product.user_ref_properties
            try:
                user_ref_property = user_ref_properties.item(key)
                user_ref_property.value = form.get(key)
            except CATIAApplicationException:
                user_ref_properties.create_string(key, form.get(key))
            except com_error:
                user_ref_properties.create_string(key, form.get(key))




