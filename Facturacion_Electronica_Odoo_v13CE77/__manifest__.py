# -*- coding: utf-8 -*-

{
    'name': 'Odoo Integración Facturación Electrónica',
    'version': '1.0',
    'category': 'Invoice',
    'summary': 'Integración con proveedor de tecnológio Dataico',
    'description': """
Este módulo permite el envío de facturas generadas por Odoo a un webservice el cual se 
encarga de enviar a su vez, la factura a un webservice de un proveedor tecnológico.
    """,
    'depends': ['base', 'account'],
    'data': ['views/inherited_account_move.xml',
    ],
    'installable': True,
    'auto_install': False
}
