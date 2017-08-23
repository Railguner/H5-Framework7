# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wens_training_manager_assess(models.Model):
    _name = 'wens_training_manager_assess'
    _rec_name = 'assess_course_id'

    assess_time = fields.Date(string='评价时间')
    assess_a = fields.Integer(string='评价1', required='true')
    assess_b = fields.Integer(string='评价2')
    assess_c = fields.Integer(string='评价3')
    assess_d = fields.Integer(string='评价4')
    assess_e = fields.Integer(string='评价5')
    assess_f = fields.Integer(string='评价6')
    assess_g = fields.Integer(string='评价7')
    assess_h = fields.Integer(string='评价8')
    assess_i = fields.Integer(string='评价9')
    assess_j = fields.Integer(string='评价10')

    assess_description_one = fields.Text(string='收获')
    assess_description_two = fields.Text(string='建议')

    assess_course_id = fields.Many2one('wens_training_manager_course', string='课程')
    assess_student_id = fields.Many2one('wens_training_manager_student', string='学生')
    # average_assess_one = fields.Float(string='平均值', compute='_average_assess_one')
    #
    # @api.depends('assess_one', 'assess_student_id')
    # def _average_assess_one(self):
    #     assess_sum = 0.0
    #     average_assess_student_id = 0
    #     for item in self:
    #         if not item.assess_student_id:
    #             item.average_assess_one = 0.0
    #             return 0
    #         else:
    #             assess_sum += item.assess_one
    #             average_assess_student_id += len(item.assess_student_id)
    #             item.average_assess_one = assess_sum / average_assess_student_id


