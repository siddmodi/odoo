{
    'name': 'Travel Management',
    'summary': """This module manages travel data of employees""",
    'version': '1.0',
    'description': """This module will let managers know the traveling details of employees""",
    'author': 'Siddharth Modi',
    'company': 'SecurEyes',
    'website': '',
    'category': 'Travel',
    'depends': ['base'],
    'license': '',
    'data': [
        # 'wizards/mark_lost.xml',
        'views/travel.xml',
        'security/ir.model.access.csv',
        # 'security/security.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application':True
}