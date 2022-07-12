# -*- coding: utf-8 -*-
from openerp import fields, models, api
import logging
import requests
import datetime
import json

_logger = logging.getLogger(__name__)

class account_move(models.Model):
    _inherit = 'account.move'

    nombre = fields.Char(string="NombreFE")
    trabajo = fields.Char(string="TrabajoFE")

    def action_post(self):
        url = "https://reqres.in/api/users"
        json_data ={
            'name': self.nombre,
            'job':self.trabajo
        }
        response = requests.post(url, data=json.dumps(json_data))

        _logger.critical('**********************************')
        _logger.critical(response.content)
        _logger.critical('**********************************')

        url = "https://reqres.in/api/users/2"
        response = requests.get(url)

        _logger.critical('**********************************')
        _logger.critical(response.content)
        _logger.critical('**********************************')

