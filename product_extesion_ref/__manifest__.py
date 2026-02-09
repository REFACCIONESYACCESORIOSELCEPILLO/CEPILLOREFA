{
    'name': 'Extensión de productos y relación',
    'version': '18.0.1.0.0',
    'summary': 'Extensión de productos y relación',
    'description': 'Extensión de productos y relación',
    'author': 'Gabriel Lopez',
    'license': 'LGPL-3',
    'category': 'Product',
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
            'product_extension_ref/static/src/js/website_sale.js',
        ],
    },
}