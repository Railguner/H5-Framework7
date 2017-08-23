# -*- coding: utf-8 -*-

import logging
import os
import sys
import json
from jinja2 import Environment, FileSystemLoader
from odoo import http,api
from odoo.http import request
import datetime
import time
import base64
from odoo.tools import image
import traceback

reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
templateLoader = FileSystemLoader(searchpath=BASE_DIR + "/templates")
env = Environment(loader=templateLoader)


class WSTrain(http.Controller):
    # 接收老师登录信息
    @http.route('/wens_training_manager/teacher_login', type='http', auth='public', csrf=False)
    def login(self, **kwargs):
        # 使用io登录
        login = kwargs.get('login', None)
        password = kwargs.get('password', None)
        uid = request.session.authenticate(request.session.db, login, password)
        # res_users_model = http.request.env['wens_training_manager_teacher']
        # teacher = res_users_model.sudo().sudo().search([('uid', '=', uid)])
        # for item in teacher:
        #     phone = item.teacher_phone
        if uid:
            return http.Response('1', 200)
        else:
            return http.Response('0', 200)

    # 界面index.html
    @http.route('/wens_training_manager/index', type='http', auth='public', csrf=False)
    def index(self, **kwargs):
        template = env.get_template("index.html")
        print "look session!"
        print request.session
        print "session_id",request.session.session_id
        print request.session.get("is_admin")
        print request.session.get("is_superuser")
        print request.session.get("user_context")
        print "db",request.session.get("db")
        print request.session.get("server_version")
        print request.session.get("server_version_info")
        print "name",request.session.get("name")
        print request.session.get("username")
        print request.session.get("company_id")
        print request.session.get("currencies")
        return template.render()


    #-------------------------------------------得到该学生上的课程，by lwl------------------------------------------#
    @http.route('/wens_training_manager/student', type='http', auth='public', csrf=False)
    def student(self, **kwargs):
        data = [] #列表里面存放数组
        #学生课程名,开始,结束sj,教师名,
        openid = kwargs.get("id")
        student_model = http.request.env['wens_training_manager_student']
        student_list = student_model.sudo().search([('openid', '=', openid)])  # 得到一个列表
        student_true_id = 0 #真实的存储在后端的id
        for item in student_list:
            student_true_id = item.id
        student_true_id = 1 ##############################测试用！！！！！！！！！1
        course_id_list = student_model.search([('id', '=', student_true_id)])
        course_list =[]
        for item in course_id_list:
            course_list =  item.student_course_id
        for course in course_list:
            dict = {
                "course":course.course_name,
                "course_start_time":course.course_start_time,
                "course_end_time":course.course_end_time
            }
            data.append(dict)
        template = env.get_template("student.html")
        return template.render(data=data)
    #-------------------------------------------得到该学生上的课程，by lwl------------------------------------------#


    #-------------------------------------------学生对课程进行评价，by lwl------------------------------------------#
    @http.route('/wens_training_manager/student_assess', type='http', auth='public', csrf=False)
    # 学生评价,收到10个分数,收获,建议
    def student_assess(self,**kwargs):
        course_name = kwargs.get("course")
        course_model = http.request.env['wens_training_manager_course']
        course_list = course_model.sudo().search([('course_name', '=', course_name)])#得到一个列表
        course_id = 0
        for item in course_list:
            course_id = item.id
        #得到这个课程名字对应的课程id
        vals = {
            "assess_time": datetime.datetime.now(),
            "assess_course_id":course_id,
            "assess_a":int(kwargs.get("assessa")),
            "assess_b":int(kwargs.get("assessb")),
            "assess_c":int(kwargs.get("assessc")),
            "assess_d": int(kwargs.get("assessd")),
            "assess_e" : int(kwargs.get("assesse")),
            "assess_f": int(kwargs.get("assessf")),
            "assess_g":int(kwargs.get("assessg")),
            "assess_h":int(kwargs.get("assessh")),
            "assess_i":int(kwargs.get("assessi")),
            "assess_j":int(kwargs.get("assessj")),
            "assess_description_one": kwargs.get("achievement"),
            "assess_description_two": kwargs.get("advice"),
            "assess_student_id":1,   #kwargs.get("assess_student_id"),
        }
        print vals
        assess_model = http.request.env['wens_training_manager_assess']
        record_id = assess_model.create(vals)
        print "what  ",record_id
        kwargs = {"id":vals.get("assess_student_id"),}
        return self.student(**kwargs)
    #-------------------------------------------学生对课程进行评价，by lwl------------------------------------------#


    #--------------------------------------------老师查看课程和对应的评价 by zw -------------------------------------#
    @http.route('/wens_training_manager/teacher', type='http', auth='public', csrf=False)
    def teacher(self, **kwargs):
        teacher_uid = request.session["uid"]
        # 项目,课程,开始时间,结束时间,平均分10个(已评人数),
        # teacher_activity_model = http.request.env['wens_training_manager_project']
        teacher_course_model = http.request.env['wens_training_manager_course']
        teacher_model = http.request.env['wens_training_manager_teacher']
        teacher = teacher_model.sudo().sudo().search([('uid', '=', teacher_uid)])
        course_id = 0
        course_sum = []
        data = []
        o = []
        for item in teacher:
            course_id = item.id
        course = teacher_course_model.sudo().search([('course_teacher_id', '=', course_id)])
        for item in course:
            for i in item.course_activity_id:
                if data:
                    for r in data:
                        if r['activity'] not in o:
                            o.append(r['activity'])
                if not data or (i.project_name not in o):
                    course_per = {
                        'course_name': item.course_name,
                        'course_start_time': item.course_start_time,
                        'course_end_time': item.course_start_time,
                        'average_assess': self.average_assess_core(item.id)
                    }
                    course_sum.append(course_per)
                    activity_per = {
                        'activity': i.project_name,
                        'course': course_sum
                    }
                    course_sum = []
                    data.append(activity_per)
                    break
                else:
                    #
                    for r in data:
                        if i.project_name == r['activity']:
                            course_per = {
                                'course_name': item.course_name,
                                'course_start_time': item.course_start_time,
                                'course_end_time': item.course_start_time,
                                'average_assess': self.average_assess_core(item.id)
                            }
                            r['course'].append(course_per)
                            break
                        break
        template = env.get_template("teacher.html")
        return template.render(data=data)
    #--------------------------------------------老师查看课程和对应的评价 by zw -------------------------------------#


    @http.route('/wens_training_manager/student_login', type='http', auth='public', csrf=False)
    def student_login(self, **kwargs):
        # 收到手机号,姓名
        student_name = kwargs.get('student_name')
        student_phone = kwargs.get('student_phone')
        student_model = http.request.env['wens_training_manager_student']
        val = {
            'student_name': student_name,
            'student_phone': student_phone,
            'student_activity_id': 0,
            'openid': "23"#datetime.datetime.now()
        }
        print val
        student_model.sudo().create(val)
        openid =  val.get("openid")
        return http.Response(openid, 200)

    #-----------------------返回已绑定的项目,已有项目列表，by lwl-----------------------------------#
    @http.route('/wens_training_manager/bind', type='http', auth='public', csrf=False)
    def bind(self, **kwargs):
        openid = int(kwargs.get("id"))
        student_model = http.request.env['wens_training_manager_student']
        student_list = student_model.sudo().search([('openid', '=', openid)]) #得到一个列表
        bind_activity_id = None
        for item in student_list:
            bind_activity_id = item.student_activity_id
        project_model = http.request.env['wens_training_manager_project']
        project_list = project_model.sudo().search([])
        project_name_list = []
        for item in project_list:
            project_name_list.append(item.project_name)
        data = {
            "binded":bind_activity_id,
            "bindlist":project_name_list
        }
        template = env.get_template("bind.html")
        return template.render(data=data)
    #-----------------------返回已绑定的项目,已有项目列表，by lwl-----------------------------------#

    #---------------------------修改已绑定的项目，by lwl--------------------------------------#
    @http.route('/wens_training_manager/bind_change', type='http', auth='public', csrf=False)
    def bind_change(self, **kwargs):
        # 收到绑定项目名
        new_project_name = kwargs.get("bindchange")
        openid = 23
        student_model = http.request.env['wens_training_manager_student']
        student_list = student_model.sudo().search([('openid', '=', openid)]) #得到一个列表
        for item in student_list:
            item.student_activity_id = new_project_name
        kwargs = {"id": openid, }
        return self.bind(**kwargs)
    #---------------------------修改已绑定的项目，by lwl--------------------------------------#

    def average_assess_core(self,course_id):
        assess_model = http.request.env['wens_training_manager_assess']
        assess = assess_model.sudo().search([('assess_course_id', '=', course_id)])
        assess_description_one = []
        assess_description_two = []
        average = []
        i = 'a'
        for r in range(10):
            assess_core = 0.0
            assess_person = 0
            for item in assess:
                assess_core += item[('assess_' + i)]
                assess_person += len(item.assess_student_id)
            if assess_person == 0:
                average.append(0)
            else:
                average.append(round((assess_core / assess_person), 2))
            i = chr(ord(i) + 1)
        for item in assess:
            assess_description_one.append(item.assess_description_one)
            assess_description_two.append(item.assess_description_two)
        average.append(assess_description_one)
        average.append(assess_description_two)
        return average




