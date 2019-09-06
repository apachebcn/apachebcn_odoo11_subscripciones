# -*- coding: utf-8 -*-
from odoo import fields, models

class prr_subscripciones_servicios(models.Model):

    _name = 'prr_subscripciones_servicios'

    name = fields.Char(
        string =    "Nombre del servicio",
        required =  True,
        help =      "Ftp/Ssh/etc..."
    )

    descripcion = fields.Char()
