# -*- coding: utf-8 -*-
{
    'name': "odoo_basico",

    'summary': """
        Proxecto inicial odoo_basico""",

    'description': """
        Proxecto odoo diferentes vistas
    """,

    'author': "Yago",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/informacion.xml',
        'views/suceso.xml',
        'views/lineapedido.xml',
        'views/pedido.xml',
        'views/templates.xml',
        'views/menu.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
