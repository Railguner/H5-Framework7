# -*- coding: utf-8 -*-
{
    'name': "wens-wharf-parts",

    'summary': """
        码头散粮""",

    'description': """
        码头散粮
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
        'views/record_views.xml',
        'views/wharf_views.xml',
        'views/ship_views.xml',
        'views/car_views.xml',
        'views/bulk_views.xml',
        'views/place_views.xml',
        'views/to_where_views.xml',
        'views/img_views.xml',
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