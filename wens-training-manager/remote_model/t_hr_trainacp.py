# -*- coding: utf-8 -*-
from tools.wens.models import RemoteModel
from tools.wens.fields import Many2oneChar
from odoo import api, fields


class t_hr_trainacp(RemoteModel):
    _name = 't_hr_trainacp'
    _description = '培训授课相关人员'
    _source_config = 'remote_base_data'
    _source_model = 't_hr_trainacp'

    fparentid = fields.Char(string='培训授课')
    fparticipatorid = fields.Char(string='职员')

