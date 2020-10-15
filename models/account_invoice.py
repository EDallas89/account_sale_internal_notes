from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    internal_note = fields.Text(string="Internal Note")

    @api.onchange('internal_note')
    def _onchange_internal_note(self):
        so = self.env['sale.order'].search([('name', '=', self.origin)], limit=1)
        so.write({'internal_note' : self.internal_note})