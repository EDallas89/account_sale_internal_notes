from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    internal_note = fields.Text(string="Internal Note")

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals["internal_note"] = self.internal_note
        return invoice_vals

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    @api.multi
    def _create_invoice(self, order, so_line, amount):
        res = super()._create_invoice(order, so_line, amount)
        res.update({'internal_note':order.internal_note})
        return res