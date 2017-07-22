# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'sale_price',
    'version' : '1.0',
    'summary': 'make sale price independely',
    'sequence': 30,
    'description': """
   """,
    'category': 'sale',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : ['sales_team'],
    'data': [
        'views/voder_price.xml',
        'views/account_vente_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
