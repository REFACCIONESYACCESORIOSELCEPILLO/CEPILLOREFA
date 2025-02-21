# -*- coding: utf-8 -*-
{
    'name': 'Extención de productos y relación',
    'version': '1.0',
    'description': '',
    'author': 'Gabriel Lopez',
    'license': 'LGPL-3',
    'category': 'product',
    'depends': [
        'stock',
        'sale',
        'product',
        'website',
        'website_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'views/templates.xml',
    ],
    'application': False,
    'installable': True,
    'assets': {
        'web.assets_frontend': [
            'product_extesion_ref/static/src/js/website_sale.js'
        ],
    },
}
