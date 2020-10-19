from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    internal_note = fields.Text(string="Internal Note")

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals["internal_note"] = self.internal_note
        return invoice_vals
    
    @api.onchange('internal_note')
    def _onchange_internal_note(self):
    # Change internal_note field on all its invoices
        invoices = self.env['account.invoice'].search([('origin', 'like', self.name)])
        for inv in invoices:
            inv.write({'internal_note' : self.internal_note})
    # Change internal_note field on any other origins from its invoices
            origin_split = inv.origin.split(", ")
            origin_len = len(origin_split)
            if (origin_len > 1):
                for origin in origin_split:
                    so = self.env['sale.order'].search([('name', '=', origin)])
                    so.write({'internal_note' : self.internal_note})
