# -*- coding: utf-8 -*-
{
    'name': "account_sale_internal_notes",

    'summary': """
        Add internal notes fields to tree and form views for 
        quotations, sales and purchases.
    """,
    'author': "Inma Sánchez",
    'website': "http://www.yourcompany.com",
    'category': 'Notes',
    'version': '11.0',
    'depends': ['account', 'sale_management'],
    'data': [
        'views/account_invoice.xml',
        'views/sale_order.xml',
    ]
}