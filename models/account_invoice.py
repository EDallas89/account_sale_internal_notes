from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    internal_note = fields.Text(string="Internal Note")

    @api.onchange('internal_note')
    def _onchange_internal_note(self):
    # Change internal_note field on all its origins and any other invoice with the same origin
        if self.origin:
            origin_split = self.origin.split(", ")
            for origin in origin_split:
                # sale order
                so = self.env['sale.order'].search([('name', '=', origin)], limit=1)
                so.write({'internal_note' : self.internal_note})
    
                so_inv = self.env['account.invoice'].search([('origin', '=', origin)])
                so_inv.write({'internal_note' : self.internal_note})
    
                #purchase order
                po =  self.env['purchase.order'].search([('name', '=', origin)], limit=1)
                po.write({'internal_note' : self.internal_note})
    
                po_inv = self.env['account.invoice'].search([('origin', '=', origin)])
                po_inv.write({'internal_note' : self.internal_note})
