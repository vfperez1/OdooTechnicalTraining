# -*- coding: utf-8 -*-

{
    "name": "Starship",
    
    "summary": """Academy app to manage Training""",
    
    "description": """
        Module to practice the mission to mars
    """,
    
    "author": "vfperez",
    
    "website": "https://ampsoftware.com",
    
    "category": "Training",
    "version": "0.1",
    
    "depends": ["contacts"],
    
    "data": [
        "security/spaceship_security.xml",
        "security/ir.model.access.csv",
        "views/starship.xml",
        "views/starship_menuitems.xml",
        "views/contacts_views_inherit.xml",
    ],
    
    "demo": [
        "demo/starship_demo.xml",
    ],
    
}