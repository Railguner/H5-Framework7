# -*- coding: utf-8 -*-
from tools.wens.models import RemoteModel
from tools.wens.fields import Many2oneChar
from odoo import api, fields


class t_hr_trainactcourse(RemoteModel):
    _name = 't_hr_trainactcourse'
    _description = '培训授课'
    _source_config = 'remote_base_data'
    _source_model = 't_hr_trainactcourse'

    ftrainactivityid = fields.Char(string='培训活动')
    ftraincourseid = fields.Char(string='培训课程')
    fid = fields.Char(string='ID')


