# -*- coding: utf-8 -*-
{
    'name': 'Hotel Management',
    'version': '1.0',
    'description': """ Module for room management in hotels. """,
    'summary': """ Module for room management in hotels. """,
    'author': 'luismdp05, aDogdev',
    'website': '',
    'category': '',
    'depends': ['base'],
    "data": [
        "security/ir.model.access.csv",
        "views/hotel_room_views.xml",
        "views/hotel_facility_views.xml",
        "views/hotel_chain_views.xml"
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
