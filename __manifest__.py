# -*- coding: utf-8 -*-
{
    'name': "Internal Notes for Account and Sale",

    'summary': """
        Add internal notes fields to tree and form views for 
        quotations, sales and purchases.
    """,
    'author': "Inma Sánchez",
    'website': "https://github.com/EDallas89",
    'category': 'Notes',
    'version': '11.0',
    'depends': ['account', 'sale_management'],
    'data': [
        'views/account_invoice.xml',
        'views/sale_order.xml',
    ]
}