# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ws_wharf_parts_bulk(models.Model):
    _name = 'ws_wharf_parts_bulk'
    _rec_name = 'bulk_name'

    bulk_name = fields.Char(string='散粮堆场')
    bulk_description = fields.Text(string="描述")

    bulk_id = fields.One2many('ws_wharf_parts_record', 'bulk', string='散粮堆场')
