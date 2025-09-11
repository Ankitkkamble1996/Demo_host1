{
    'name': 'School Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage students, classes and teachers',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/student_views.xml',
    ],
    'installable': True,
    'application': True,
}