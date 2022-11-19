# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Sale Extended',
    'version' : '1.0',
    'summary': 'Sale',
    'sequence': 15,
    'description': """
    This module is used for sale.
    """,
    'author': "Scorpion"
    'category': 'Sale',
    'depends' : ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_inherit_view.xml',
        'data/ir_sequence_data.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
