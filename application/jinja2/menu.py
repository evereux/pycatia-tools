from flask import render_template
from flask import url_for

from application import app

with app.app_context():
    m_dict_home = {
        'title': 'home',
        'url': url_for('home'),
        # 'menu_items': [
        #     {
        #         'url': url_for('part_new'),
        #         'title': 'New Part'
        #     },
        # ]
    }

    m_dict_documents = {
        'title': 'Documents',
        'url': url_for('documents'),
        # 'menu_items': [
        #     {
        #         'url': url_for('part_new'),
        #         'title': 'New Part'
        #     },
        # ]
    }

    m_dict_part = {
        'title': 'Part',
        'url': url_for('part'),
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
        'title': 'Product',
        'url': url_for('product'),
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
                'title': 'Renumber Instances'
            },
            {
                'url': url_for('product_properties'),
                'title': 'Edit Product Properties'
            },
        ]
    }

    m_dict_drafting = {
        'title': 'Drafting',
        'url': url_for('drafting'),
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

    m_list = [
        m_dict_home,
        m_dict_documents,
        m_dict_part,
        m_dict_product,
        m_dict_drafting,
    ]


def render_menu_header():
    return render_template('partials.menu_header.html', m_list=m_list)


def render_menu(option: str):
    m_dict = None

    if option == 'part':
        m_dict = m_dict_part
    if option == 'product':
        m_dict = m_dict_product
    if option == 'drafting':
        m_dict = m_dict_drafting

    return render_template('partials.menu.html', m_dict=m_dict)
