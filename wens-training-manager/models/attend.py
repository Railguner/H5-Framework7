# -*- coding: utf-8 -*-

from odoo import models, fields, api

class wens_training_manager_attend(models.Model):
    _name = 'wens_training_manager_attend'

    attend_time = fields.Date(string='签到时间')
    attend_description = fields.Text(string='备注')

    attend_student_id = fields.Many2one('wens_training_manager_student', string='学员')
    attend_course_id = fields.Many2one('wens_training_manager_course', string='课程')
    test = fields.Many2one('t_hr_trainactivity', string=u'test')

    # @api.multi
    # @api.onchange('test')
    # def onchange_test(self):
    #     for i in self:
    #         print i.test.id
    #         print i.test.fname_l2
    #         print '========='
