# -*- coding: utf-8 -*-
from tools.wens.models import RemoteModel
from tools.wens.fields import Many2oneChar
from odoo import api, fields


class t_hr_traincourse(RemoteModel):
    _name = 'tt_hr_traincourse'
    _description = '培训课程'
    _source_config = 'remote_base_data'
    _source_model = 't_hr_traincourse'

    fname_l2 = fields.Char(string='课程')
    fid = fields.Char(string='ID')
