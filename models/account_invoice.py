from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    internal_note = fields.Text(string="Internal Note")