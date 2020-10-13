from odoo import api, fields, models, _


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        res = super()._create_invoice(order, so_line, amount)
        res.update({'internal_note':order.internal_note})
        return res