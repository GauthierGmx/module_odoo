# -*- coding: utf-8 -*-
{
    'name': "postal",

    'summary': "Addon for postal informations in France",

    'description': """
Addon used to manage postal informations in France such as: region, department, city and zip code.
    """,

    'author': "Gauthier GOUMEAUX",
    'website': "https://gauthiergmx.github.io/mon-portfolio/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Localization',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

