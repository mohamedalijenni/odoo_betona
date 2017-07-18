# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'soft purchase',
    'version': '1.0',
    'category': 'Purchases',
    'sequence': 60,
    'summary': 'seperation purchase and rfq',
    'description': """
Manage goods requirement by Purchase Orders easily
==================================================

Purchase management enables you to track your vendors' price quotations and convert them into purchase orders if necessary.
Odoo has several methods of monitoring invoices and tracking the receipt of ordered goods. You can handle partial deliveries in Odoo, so you can keep track of items that are still to be delivered in your orders, and you can issue reminders automatically.

Odoo's replenishment management rules enable the system to generate draft purchase orders automatically, or you can configure it to run a lean process driven entirely by current production needs.

Dashboard / Reports for Purchase Management will include:
---------------------------------------------------------
* Request for Quotations
* Purchase Orders Waiting Approval
* Monthly Purchases by Category
* Receipt Analysis
* Purchase Analysis
    """,
    'website': 'https://www.odoo.com/page/purchase',
    'depends': ['purchase'],
    'data': [
        'views/softpurchase.xml'
        
    ],
    'test': [
        
    ],
    'demo': [
        
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
