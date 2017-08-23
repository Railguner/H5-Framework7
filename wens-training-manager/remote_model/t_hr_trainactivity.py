# -*- coding: utf-8 -*-
from tools.wens.models import RemoteModel
from tools.wens.fields import Many2oneChar
from odoo import api, fields


class t_hr_trainactivity(RemoteModel):
    _name = 't_hr_trainactivity'
    _description = '培训活动'
    _source_config = 'remote_base_data'
    _source_model = 't_hr_trainactivity'

    fname_l2 = fields.Char(string='活动')
    fid = fields.Char(string='ID')
