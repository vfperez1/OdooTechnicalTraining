# -*- coding: utf-8 -*-

{
    "name": "Odoo Academy",
    
    "summary": """Academy app to manage Training""",
    
    "description": """
        Academy module to manage training:
            -Courses
            -Sessions
            -Attendees
    """,
    
    "author": "vfperez",
    
    "website": "https://www.ampsoftware.com",
    
    "category": "training",
    "version": "0.1",
    
    "depends": ["sale"],
    
    "data": [
        "security/academy_security.xml",
        "security/ir.model.access.csv",
        "views/academy_menuitems.xml",
        "views/course_views.xml",
        "views/session_views.xml",
        "views/sale_views_inherit.xml",
    ],
    
    "demo": [
        "demo/academy_demo.xml",
    ],
}