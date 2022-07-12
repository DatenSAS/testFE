# -*- coding: utf-8 -*-
from openerp import fields, models, api
import logging
import datetime
import json

_logger = logging.getLogger(__name__)

class account_move(models.Model):
    _inherit = 'account.move'

    nombre = fields.Char(string="NombreFE")
    trabajo = fields.Char(string="TrabajoFE")

    def action_post(self):
        _logger.critical('***************** Hello Again *****************')
