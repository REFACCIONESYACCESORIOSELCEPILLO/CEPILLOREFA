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
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_view.xml',
    ],
    # 'auto_install': True,
    'application': False,
    'installable': True,
} 
