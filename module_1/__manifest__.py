# -*- coding: utf-8 -*-
{
    'name': 'Model to El Cepillo',
    'version': '1.0',
    'description': '',
    'author': 'Gabriel Lopez',
    'license': 'LGPL-3',
    'category': 'stock',
    'depends': [
        'stock',
        'product',
        'l10n_mx_edi',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_location_view.xml',
        'views/product_template_view.xml',
        'report/report_account_move.xml',
    ],
    # 'auto_install': True,
    'application': False,
    'installable': True,
} 
