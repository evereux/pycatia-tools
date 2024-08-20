from flask import render_template
from flask import url_for

from application import app

with app.app_context():

    m_dict_part = {
        'title': 'Part Tools',
        'menu_items': [
            {
                'url': url_for('part_new'),
                'title': 'New Part'
            },
            {
                'url': url_for('part_points'),
                'title': 'Points'
            },
            {
                'url': url_for('part_bounding_box'),
                'title': 'Bounding Box'
            },
        ]
    }

    m_dict_product = {
        'title': 'Product Tools',
        'menu_items': [
            {
                'url': url_for('product_new'),
                'title': 'New Product'
            },
            {
                'url': url_for('product_reorder'),
                'title': 'Reorder Product Tree'
            },
            {
                'url': url_for('product_renumber_instances'),
                'title': 'Rename Instances'
            },
            {
                'url': url_for('product_attributes'),
                'title': 'Edit Product Attributes'
            },
        ]
    }

    m_dict_drafting = {
        'title': 'Drafting Tools',
        'menu_items': [
            {
                'url': url_for('drafting_views'),
                'title': 'Views'
            },
            {
                'url': url_for('drafting_save_as'),
                'title': 'Save As'
            },
            {
                'url': url_for('drafting_insert_template'),
                'title': 'Insert Template'
            },
        ]
    }


def render_menu(option: str):

    m_dict = None

    if option == 'part':
        m_dict = m_dict_part
    if option == 'product':
        m_dict = m_dict_product
    if option == 'drafting':
        m_dict = m_dict_drafting

    return render_template('partials/menu.html', m_dict=m_dict)
