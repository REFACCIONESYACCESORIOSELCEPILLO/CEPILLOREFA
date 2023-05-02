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
        'reports/custom_label_template.xml',
        'reports/custom_label_template_product.xml',
        'views/sale_order_views.xml',
        'views/product_template_view.xml',
        'views/website_view.xml',
        'views/templates.xml',
        'wizards/product_label_layout_view.xml',
    ],
    # 'auto_install': True,
    'application': False,
    'installable': True,
    'assets': {
        'web.assets_frontend': [
            'product_extesion_ref/static/src/js/website_sale.js',
        ],
    },
}
