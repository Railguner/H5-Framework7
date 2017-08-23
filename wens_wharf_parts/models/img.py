# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ws_wharf_parts_img(models.Model):
    _name = 'ws_wharf_parts_img'
    _rec_name = 'img'

    img_name = fields.Char(string="图片名")
    img = fields.Binary(string='图片', required=True)
    small_img = fields.Binary(string='缩略图')
    img_id = fields.Many2one('ws.wharf.checking', string='图片')
