# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wens_training_manager_project(models.Model):
    _name = 'wens_training_manager_project'
    _rec_name = 'project_name'

    project_name = fields.Char(string='项目')
    project_course_id = fields.One2many('wens_training_manager_course', 'course_activity_id', string='课程')
    project_organizer_id = fields.Many2one('wens_training_manager_organizer', string='组织者')
