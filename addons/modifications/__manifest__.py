# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Modification',
    'version': '2.0',
    'category': 'module interne',
    'description': """

==================================================

Formation technque odoo
    """,
    'summary': 'Formation odoo',
    'website': 'https://www.targa-consult.com',
    'depends': ['account','sale','purchase','product','sales_team'],
    'data': [
        'views/client_view.xml',
        'views/achat_view.xml',
        'views/article_view.xml',
        'report/invoice_report_view.xml'
        
       
        
       
       
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 105,
}
