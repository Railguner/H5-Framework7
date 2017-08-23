# -*- coding: utf-8 -*-

from odoo import models, fields, api,http


class wens_training_manager_student(models.Model):
    _name = 'wens_training_manager_student'
    _rec_name = 'student_name'

    openid = fields.Char(string='微信标志')
    student_name = fields.Char(string='学生')
    student_phone = fields.Char(string='学生电话')
    student_class = fields.Char(string='班级')

    student_course_id = fields.Many2many('wens_training_manager_course', string='课程')
    student_activity_id = fields.Many2one('wens_training_manager_project', string='项目')

    @api.model
    def create(self, vals):
        if vals['student_activity_id'] == 0:
            new_record = super(wens_training_manager_student, self).create(vals)
            return new_record
        else:
            student_activity_id = vals['student_activity_id']
            activity_model = http.request.env['wens_training_manager_project']
            activity = activity_model.sudo().search([('id', '=', student_activity_id)])
            student_course_id = []
            for item in activity:
                student_course_id = item.project_course_id
            course = []
            course_id = [6, False]
            for item in student_course_id:
                course.append(item.id)
            course_id.append(course)
            vals['student_course_id'].append(course_id)
            new_record = super(wens_training_manager_student, self).create(vals)
            return new_record



