from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    internal_note = fields.Text(string="Internal Note")

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
                    po = self.env['purchase.order'].search([('name', '=', origin)])
                    po.write({'internal_note' : self.internal_note})

    def action_view_invoice(self):
        result = super(PurchaseOrder, self). action_view_invoice()
        result["context"]['default_internal_note'] = self.internal_note
        return result