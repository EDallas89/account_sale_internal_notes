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
                ## sale order
                # search quotations
                so = self.env['sale.order'].search([('name', '=', origin)], limit=1)
                so.write({'internal_note' : self.internal_note})
                # search others invoices
                so_inv = self.env['account.invoice'].search([('origin', '=', origin)])
                so_inv.write({'internal_note' : self.internal_note})
    
                ## purchase order
                # search purchase orders
                po =  self.env['purchase.order'].search([('name', '=', origin)], limit=1)
                po.write({'internal_note' : self.internal_note})
                # search others invoices
                po_inv = self.env['account.invoice'].search([('origin', '=', origin)])
                po_inv.write({'internal_note' : self.internal_note})

                ## credit note
                # search credit notes
                cn = self.env['account.invoice'].search([('origin', '=', self.number)])
                cn.write({'internal_note' : self.internal_note})

        # search invoices
        cn = self.env['account.invoice'].search([('number', '=', self.origin)])
        cn.write({'internal_note' : self.internal_note})

    @api.model
    def refund(self, date_invoice=None, date=None, description=None, journal_id=None):
        values = super(AccountInvoice, self).refund()
        values['internal_note'] = self.internal_note
        return values