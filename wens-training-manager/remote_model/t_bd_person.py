# -*- coding: utf-8 -*-
from tools.wens.models import RemoteModel
from tools.wens.fields import Many2oneChar
from odoo import api, fields


class t_bd_person(RemoteModel):
    _name = 't_bd_person'
    _description = '员工个人信息'
    _source_config = 'remote_base_data'
    _source_model = 't_bd_person'

    fid = fields.Char(string='ID')
    fname_l2 = fields.Char(string='讲师')


