# noinspection PyStatementEffect
{
    'name': "Apartment Management",
    'version': "1.0",
    'author': 'Angel Kenneth Tolentino',
    'summary': "User may get and edit information about their apartments",
    'depends': [
        'base',
        'decimal_precision',
    ],
    'description': "A module that allows users to check their Apartment Details",
    'data': [
        'views/space_apartments_views.xml',
        'views/space_apartments_action.xml',
        'views/space_apartments_search.xml',
        'views/res_users_views.xml',
        'views/res_users_action.xml',
        'views/res_users_search.xml',
    ],
}
