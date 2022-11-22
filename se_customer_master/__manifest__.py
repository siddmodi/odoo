{
    'name': 'se_customer_master',
    'summary': """This module inheritance for sales module""",
    'version': '1.0',
    'description': """This module for make some changes in sales module according to our need""",
    'author': 'Siddharth Modi',
    'company': 'SecurEyes',
    'website': '',
    'category': 'se_customer_master',
    'depends': ['base','se_customer_master'],
    'license': '',
    'data': [
        # 'security/ir.model.access.csv',
        'views/se_customer_master.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': True,
    'application':True
}