# -*- coding: utf-8 -*-

import logging
import os
import sys
import json
from jinja2 import Environment, FileSystemLoader
from odoo import http
from odoo.http import request
import datetime
import time
from ws_base import api_models
from odoo.tools import image
import traceback

reload(sys)
sys.setdefaultencoding('utf8')

logger = logging.getLogger(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
templateLoader = FileSystemLoader(searchpath=BASE_DIR + "/templates")
env = Environment(loader=templateLoader)


class WsWharf(http.Controller):
    # 接收登录信息
    @http.route('/wens_wharf_parts/login', type='http', auth='public', csrf=False)
    def login(self, **kwargs):
        # 使用io登录
        login = kwargs.get('login', None)
        password = kwargs.get('password', None)
        uid = request.session.authenticate(request.session.db, login, password)

        res_users_model = http.request.env['res.users']
        print res_users_model
        print 2
        users = res_users_model.sudo().search([('id', '=', uid)])
        print users.mobile
        print users.name
        print 11111111
        print users
        print users.io_user_id
        print users.io_user_id.fid
        print users.io_user_id.fid.id

        if uid:
            return http.Response('1', 200)
        else:
            return http.Response('0', 200)

    # push添加数据uid
    @http.route('/wens_wharf_parts/push', type='http', csrf=False)
    def post(self, **kwargs):
        record_model = http.request.env['ws_wharf_parts_record']
        img_model = http.request.env['ws_wharf_parts_img']
        wharf_model = http.request.env['ws_wharf_parts_wharf']
        ship_model = http.request.env['ws_wharf_parts_ship']
        car_model = http.request.env['ws_wharf_parts_car']
        bulk_model = http.request.env['ws_wharf_parts_bulk']
        place_model = http.request.env['ws_wharf_parts_place']
        to_where_model = http.request.env['ws_wharf_parts_to_where']
        time_now = datetime.datetime.now()
        number = int(time.time()*1000000)
        local = kwargs.get('local')
        wharf = kwargs.get('wharf')
        ship = kwargs.get('ship')
        car = kwargs.get('car')
        bulk = kwargs.get('bulk')
        place = kwargs.get('place')
        to_where = kwargs.get('to_where')
        wharf = wharf_model.sudo().search([('wharf_name', '=', wharf)])
        ship = ship_model.sudo().search([('ship_name', '=', ship)])
        car = car_model.sudo().search([('car_name', '=', car)])
        bulk = bulk_model.sudo().search([('bulk_name', '=', bulk)])
        place = place_model.sudo().search([('place_name', '=', place)])
        to_where = to_where_model.sudo().search([('to_where_name', '=', to_where)])
        # io账号, 密码, 数据库, UID
        uid = request.session["uid"]
        description = kwargs.get('description')
        vals = {
            'number': number,
            'time': time_now,
            'local': local,
            'wharf': wharf.id,
            'ship': ship.id,
            'car': car.id,
            'bulk': bulk.id,
            'place': place.id,
            'to_where': to_where.id,
            'uid': uid,
            'description': description
        }
        # 通过模型方法insert一条记录
        record_model.sudo().create(vals=vals)
        record = record_model.sudo().search([('number', '=', number)])
        for item in record:
            img_id = item.id
        i = '0'
        end_number = 'A'
        for item in range(9):
            img = kwargs.get('img'+i)
            if img == 'undefined':
                break
            else:
                # 压缩图片
                small_img=image.image_resize_image(img, size=(128, 128), encoding='base64', filetype=None,
                                                   avoid_if_small=False)
                # print str(number)+'A'
                # print "small size:"
                # print image.image_resize_image(img, size=(270, 270), encoding='base64',
                # filetype=None,avoid_if_small=False)
                img_model.sudo().create({'img_id': img_id, 'img': img,
                                         'img_name': str(number) + end_number, 'small_img': small_img})
                i = chr(ord(i) + 1)
                end_number = chr(ord(end_number)+1)
        return http.Response('您已登记', 200)

    # 返回界面index.html
    @http.route('/wens_wharf_parts/index', type='http', auth='public', csrf=False)
    def index(self, **kwargs):
        template = env.get_template("index.html")
        return template.render()

    # 返回界面post.html
    @http.route('/wens_wharf_parts/post', type='http')
    def get(self, **kwargs):
        # if not request.session["uid"]:
        #     template = env.get_template("index.html")
        #     return template.render()
        wharf_model = http.request.env['ws_wharf_parts_wharf']
        ship_model = http.request.env['ws_wharf_parts_ship']
        car_model = http.request.env['ws_wharf_parts_car']
        bulk_model = http.request.env['ws_wharf_parts_bulk']
        place_model = http.request.env['ws_wharf_parts_place']
        to_where_model = http.request.env['ws_wharf_parts_to_where']
        res_wharf = wharf_model.sudo().search([])
        res_ship = ship_model.sudo().search([])
        res_car = car_model.sudo().search([])
        res_bulk = bulk_model.sudo().search([])
        res_place = place_model.sudo().search([])
        res_to_where = to_where_model.sudo().search([])
        data1 = []
        data2 = []
        data3 = []
        data4 = []
        data5 = []
        data6 = []
        for item in res_wharf:
            data1.append(item.wharf_name)
        for item in res_ship:
            data2.append(item.ship_name)
        for item in res_car:
            data3.append(item.car_name)
        for item in res_bulk:
            data4.append(item.bulk_name)
        for item in res_place:
            data5.append(item.place_name)
        for item in res_to_where:
            data6.append(item.to_where_name)
        data_list = {'wharf': data1, 'ship': data2, 'car': data3, 'bulk': data4, 'place': data5, 'to_where': data6}
        template = env.get_template("post.html")
        return template.render(data=data_list)

    # 返回界面 record.html
    @http.route('/wens_wharf_parts/record', type='http', csrf=False)
    def record(self, **kwargs):
        # if not request.session["uid"]:
        #     template = env.get_template("index.html")
        #     return template.render()
        wharf_model = http.request.env['ws_wharf_parts_record']
        res_users_model = http.request.env['res.users']
        res_id = res_users_model.sudo().search([('login', '=', request.session["login"])])
        own_id = 0
        for item in res_id:
            own_id = item.id
        wharf_list = wharf_model.sudo().search([('uid', '=', own_id)])
        data_list = []
        for item in wharf_list:
            time_now = datetime.datetime.strptime(item.time, "%Y-%m-%d %H:%M:%S")+datetime.timedelta(hours=8)
            # 时区转化
            # time_now = time_now.replace(tzinfo=pytz.timezone('UTC')).astimezone(pytz.timezone('Asia/Shanghai'))
            img_image = []
            for i in item.img:
                img_image.append((i.id, i.small_img))
            data_list.append({'number': item.number,
                              'img': img_image,
                              'time': time_now,
                              'local': item.local,
                              'wharf': item.wharf.wharf_name,
                              'ship': item.ship.ship_name,
                              'car': item.car.car_name,
                              'bulk': item.bulk.bulk_name,
                              'place': item.place.place_name,
                              'to_where': item.to_where.to_where_name,
                              'description': item.description,
                              })
        template = env.get_template("record.html")
        return template.render(data=data_list)

    @http.route('/wens_wharf_parts/big_image', type='http', csrf=False)
    def big_image(self, **kwargs):
        img_id = kwargs.get('id')
        if img_id:
            img_model = http.request.env['ws_wharf_parts_img']
            img_list = img_model.sudo().search([('id', '=', img_id)])
            for item in img_list:
                img = item.img
            return http.Response(img, 200)
        else: return http.Response('0', 200)









