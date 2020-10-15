from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    internal_note = fields.Text(string="Internal Note")

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals["internal_note"] = self.internal_note
        return invoice_vals

#    origin_o2m = fields.One2many(
#        comodel_name='account.invoice', 
#        inverse_name='origin_m2o',
#        string="Facturas"
#    )
    
    @api.onchange('internal_note')
    def _onchange_internal_note(self):
        so = self.env['account.invoice'].search([('origin', '=', self.name)], limit=1)
        so.write({'internal_note' : self.internal_note})