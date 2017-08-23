# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wens_training_manager_organizer(models.Model):
    _name = 'wens_training_manager_organizer'
    _rec_name = 'organizer_uid'

    organizer_uid = fields.Many2one('res.users', string='组织者')
    organizer_project_id = fields.One2many('wens_training_manager_project', 'project_organizer_id', string='项目')