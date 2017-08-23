# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wens_training_manager_teacher(models.Model):
    _name = 'wens_training_manager_teacher'
    _rec_name = 'uid'

    uid = fields.Many2one('res.users', string='老师')
    teacher_phone = fields.Char(string='老师电话')

    teacher_course_id = fields.One2many('wens_training_manager_course', 'course_teacher_id', string='课程')

    # 自动获取老师电话
    @api.multi
    @api.onchange('uid')
    def on_io_user_change(self):
        for item in self:
            item.teacher_phone = item.uid.mobile



