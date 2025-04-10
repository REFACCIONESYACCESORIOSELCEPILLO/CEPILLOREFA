{
    'name': 'Sale Order Report Custom',
    'version': '1.0',
    'description': 'Sale Order Report Custom',
    'summary': 'Sale Order Report Custom',
    'author': 'MyCompany',
    'license': 'LGPL-3',
    'category': 'sale',
    'depends': [
        'base','sale_management'
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/sale_order_report.xml',
        'wizard/wizard_sorder_report.xml',
    ],
    
}