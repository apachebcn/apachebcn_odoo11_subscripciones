# -*- coding: utf-8 -*-
from odoo import fields, models, api

class prr_subscripciones_datos(models.Model):

    _name = 'prr_subscripciones_datos'
    _order = 'cliente_id, servicio_id, url, username'

    cliente_id = fields.Many2one(
        'prr_subscripciones_clientes',
        string =        "Cliente",
        required =      False
    )

    servicio_id = fields.Many2one(
        'prr_subscripciones_servicios',
        string =        "Servicio",
        required =      False
    )

    url = fields.Char(string="Url")

    username = fields.Char(string="Usuario")

    password = fields.Char(string="Password")

    observaciones = fields.Html(string="Observaciones")
