from odoo import api,fields,models

class softpurchase(models.Model):
    
    _inherit="purchase.order"
    
    
    monstate = fields.Selection([
        ('prepurchase', 'bon de commande brouillon'),
        ('purchase', 'Purchase Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled')
        ], string='Status', readonly=True, index=True, default='prepurchase',copy=False,track_visibility='onchange')

    @api.multi
    def button_approve(self, force=False):
        self.write({'state': 'purchase'})
        self.write({'monstate': 'purchase'})
        self._create_picking()
        if self.company_id.po_lock == 'lock':
            self.write({'state': 'done'})
            self.write({'monstate': 'done'})
        return {}
    
       
    
           
    
