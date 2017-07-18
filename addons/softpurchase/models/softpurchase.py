from odoo import api,fields,models

class softpurchase(models.Model):
    
    _inherit="purchase.order"
    
    
    monstate = fields.Selection([
        ('prepurchase', 'bon de commande brouillon'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
        ], string='Status', readonly=True, index=True, default='prepurchase',copy=False,track_visibility='onchange')
    
       
    
           
    