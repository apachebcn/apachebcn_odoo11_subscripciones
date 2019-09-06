# -*- coding: utf-8 -*-
from odoo import fields, models

class prr_subscripciones_clientes(models.Model):

    _name = 'prr_subscripciones_clientes'

    name = fields.Char(string = "Nombre de cliente", required=True)

