# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ws_wharf_parts_to_where(models.Model):
    _name = 'ws_wharf_parts_to_where'
    _rec_name = 'to_where_name'

    to_where_name = fields.Char(string='去向')
    to_where_description = fields.Text(string="描述")

    to_where_id = fields.One2many('ws_wharf_parts_record', 'to_where', string='去向')
