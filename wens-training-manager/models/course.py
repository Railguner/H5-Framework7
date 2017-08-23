# -*- coding: utf-8 -*-

from odoo import models, fields, api


class wens_training_manager_course(models.Model):
    _name = 'wens_training_manager_course'
    _rec_name = 'course_name'

    course_name = fields.Char(string='课程')
    course_start_time = fields.Date(string='开始时间')
    course_end_time = fields.Date(string='结束时间')

    course_teacher_id = fields.Many2one('wens_training_manager_teacher', string='老师')
    course_student_id = fields.Many2many('wens_training_manager_student', string='学生')
    course_activity_id = fields.Many2one('wens_training_manager_project', string='活动')
