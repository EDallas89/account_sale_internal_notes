from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    internal_note = fields.Text(string="Internal Note")
