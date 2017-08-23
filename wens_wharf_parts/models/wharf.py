# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ws_wharf_parts_wharf(models.Model):
    _name = 'ws_wharf_parts_wharf'
    _rec_name = 'wharf_name'

    wharf_name = fields.Char(string='码头', required=True)
    wharf_description = fields.Text(string="描述")

    wharf_id = fields.One2many('ws_wharf_parts_record', 'wharf', string='码头')
