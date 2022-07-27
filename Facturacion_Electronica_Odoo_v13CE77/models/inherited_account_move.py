# -*- coding: utf-8 -*-
from openerp import fields, models, api
import logging
import requests
import datetime
import json

class account_move(models.Model):
    _inherit = 'account.move'

    #Creación de campos que hacen falta en Maidensoft para tener todos los campos de la API
    #TODO: Incluir estos campos en la vista de 'account_move'

    send_mail = fields.Boolean(sting="Enviar Correo")
    send_dian = fields.Boolean(string="Enviar DIAN")

    ambiente = fields.Selection(
           [('Produccion', 'Produccion'), ('Pruebas', 'Pruebas'),],
           'Ambiente'
    )

    dataico_account_id = fields.Char(string="ID Dataico")

    #Se crea variable para almacenar el código de respuesta
    respuesta = fields.Char(string="Respuesta API")


    #TODO: Hacer la equivalencia entre la forma como estan configurados los campos en Maidensoft y como los espera la API de Dataico
    #TODO: Hacer todas las verificaciones necesarias del tipo de factura que se esta trabajando antes de pasar los valores al JSON

    def action_post(self):

         #TODO: En esta primera prueba se envian los datos de la factura "quemados"
         #TODO: En esta prueba se hace 'override' de la función 'action_post' de Odoo sin hacer 'super', por lo cual no se publican asientos por el momento

         url = "https://api.dataico.com/direct/dataico_api/v2/invoices"
         factura = {
             "actions": {
                 "send_dian": False,
                 "send_email":False
             },
             "invoice": {
                 "env": "PRODUCCION",
                 "dataico_account_id": "002979c5-7c23-43ab-aa98-3fa7dce6e4d0",
                 "number": 10,
                 "issue_date": "13/08/2021",
                 "payment_date": "23/09/2021 13:22:43",
                 "order_reference": "YR2603",
                 "invoice_type_code": "FACTURA_VENTA",
                 "payment_means": "DEBIT_CARD",
                 "payment_means_type": "DEBITO",
                 "numbering": {
                     "resolution_number": "18760000001",
                     "prefix": "YR",
                     "flexible": False
                 },
                 "notes": [
                     "Pagar a Bancolombia"
                 ],
                 "customer": {
                     "email": "correo1@datico.com",
                     "phone": "42112315",
                     "party_identification_type": "NIT",
                     "party_identification": "900555556",
                     "party_type": "PERSONA_JURIDICA",
                     "tax_level_code": "COMUN",
                     "regimen": "ORDINARIO",
                     "department": "73",
                     "city": "001",
                     "address_line": "Carrera 41B # 51B Nº 9, Chapinero",
                     "country_code": "CO",
                     "company_name": "NOMBRE_EMPRESA",
                     "first_name": "Pedro",
                     "family_name": "Perez"
                 },
                 "items": [
                     {
                         "sku": "YR-001",
                         "quantity": 10,
                         "description": "Descripcion del Producto",
                         "measuring_unit": "94",
                         "price": 2000,
                         "discount_rate": 10,
                         "taxes": [
                             {
                                 "tax_category": "IVA",
                                 "tax_rate": 19
                             }
                         ],
                         "retentions": [
                             {
                                 "tax_category": "RET_FUENTE",
                                 "tax_rate": 1
                             }
                         ]
                     }
                 ]
             }
         }
         self.respuesta = requests.post(url, data=json.dumps(factura))