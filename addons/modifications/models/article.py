from odoo import api, fields, models, _


class Article(models.Model):   
    _inherit='product.template'
    


class Livraison(models.Model):   
    _inherit='stock.picking'
    
    camion=fields.Char('Camion')
    matricule=fields.Char('matricule')
    chauffeur=fields.Char('Chauffeur')
    
# class Camion(models.Model):   
#     _inherit='stock.picking'
#     
#     name=fields.Char('Camion')
#     camion_id=fields.Many2one('stock.picking','chauffeur_id')
#    
#     
# class Chauffeur(models.Model):   
#     _inherit='stock.picking'    
#     
#     name =fields.Char('Chauffeur')
#     chauffeur_id=fields.One2many('stock.picking','camion_id','Camion_chauffeur')