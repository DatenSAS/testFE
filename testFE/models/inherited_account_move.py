# -*- coding: utf-8 -*-
from openerp import fields, models, api
from datetime import datetime
from odoo.exceptions import ValidationError

class account_move(models.Model):
    _inherit = 'account.move'

    nombre = fields.Char(string="NombreFE")
    trabajo = fields.Char(string="TrabajoFE")