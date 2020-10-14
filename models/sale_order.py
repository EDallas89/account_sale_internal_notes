from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    internal_note = fields.Text(
        string="Internal Note",
        readonly=False
    )

    origin_o2m = fields.One2many(
        comodel_name='account.invoice', 
        inverse_name='origin_m2o',
        string="Facturas")
