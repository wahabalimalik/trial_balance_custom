# -*- coding: utf-8 -*-
{
    'name': "trial_balance_custom",

    'summary': """
        Extending Trial Balance Report and shows the relavent group and its 
        total before showing actual GL""",

    'description': """
        Extending Trial Balance Report and shows the relavent group and its 
        total before showing actual GL
    """,

    'author': "Axiom",
    'website': "http://www.axiomworld.net",
    'category': 'Reports',
    'version': '0.1',
    'depends': ['account'],
    'data': [
        'views/templates.xml',
    ],
}