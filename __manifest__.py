# -*- coding: utf-8 -*-
{
    'name': "Internal Notes for Account, Sale and Purchase",

    'summary': """
        Add internal notes fields to tree and form views for 
        quotations, sales and purchases.
    """,
    'author': "Aresoltec Canarias S.L.",
    'website': "https://github.com/EDallas89",
    'category': 'Notes',
    'version': '11.0',
    'depends': ['account', 'sale_management', 'purchase'],
    'data': [
        'views/account_invoice.xml',
        'views/sale_order.xml',
        'views/purchase_order.xml'
    ]
}