from odoo import api, fields, models, _

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    internal_note = fields.Text(string="Internal Note")

    @api.onchange('internal_note')
    def _onchange_internal_note(self):
        po = self.env['account.invoice'].search([('origin', '=', self.name)])
        po.write({'internal_note' : self.internal_note})

    def action_view_invoice(self):
        result = super(PurchaseOrder, self). action_view_invoice()
        result["context"]['default_internal_note'] = self.internal_note
        return result