from odoo import api, fields, models, _


class Article(models.Model):   
    _inherit='product.template'
    
    


class Livraison(models.Model):   
    _inherit='stock.picking'
    
    camion=fields.Char('Camion')
    chauffeur=fields.Char('Chauffeur')
    adresse=fields.Char('Adresse du chantier')
    reference=fields.Char('Référence')
    ouvrage=fields.Selection([('oui', 'Oui'), ('non', 'Non')], string='Ouvrage')
    pompe=fields.Selection([('oui', 'Oui'), ('non', 'Non')], string='Pompé')