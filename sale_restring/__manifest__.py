{
    'name' : 'Sale Locked Create',
    'version' : '1.0',
    'depends' :[
        'sale'
    ],
    'author' : 'Ing. Gustavo',
    'category' : 'Sales/Sales',
    'description' : '''
        Módulo para gestionar bloquear las ventas creadas en estado borrador y ya con codigo
    ''',
    'website' : 'jumataqui.com',
    'data': [
        'security/res_groups.xml',
        'views/sale_order_view.xml'
    ],
    'summary' : '''Funciones adicionales en Ventas
    ''',
    'post_init_hook': '_update_order_lock_drat',
    'license': 'LGPL-3',
}
