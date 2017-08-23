# -*- coding: utf-8 -*-
{
    'name': "wens_training_manager",

    'summary': """
        培训""",

    'description': """
        温氏学院培训管理系统
    """,

    'author': "张伟,李永骥",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/attend_views.xml',
        'views/course_views.xml',
        'views/student_views.xml',
        'views/teacher_views.xml',
        'views/assess_views.xml',
        'views/organizer_views.xml',
        'views/project_views.xml',
        'views/menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}