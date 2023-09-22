# -*- coding: utf-8 -*-
{
    'name': "Weather Forecast Snippet",

    'summary': """
        App for the website presentation of OXP 2023 for dev demo""",

    'description': """
        Provides a snippet to display the weather forecast
    """,

    'author': "Odoo S.A",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/snippets/s_weather.xml',
        'views/snippets/snippets.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
