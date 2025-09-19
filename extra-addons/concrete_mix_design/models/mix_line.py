from odoo import api, fields, models
from odoo.exceptions import UserError,ValidationError
import math
import io
import zipfile
import base64

class LermErtParent(models.Model):
    _name = "lerm.mix.design.parent"
    _rec_name = "name"

    name = fields.Char("Project Name")
    mix_lines = fields.One2many('mix.lines','parent_id',"Mix Lines")
    rec_date  = fields.Date("Date")


    def create_mix_design(self):
        
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mechanical.concrete.design',   # must match the target model's _name
            'target': 'current',
            'context': {
                'default_mix_parent_id':self.id
            }
        }



class LermMixLines(models.Model):
    _name = "mix.lines"  

    parent_id = fields.Many2one('lerm.mix.design.parent') 
    concrete_mix_id = fields.Many2one('mechanical.concrete.design')
