from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = "sale.order"

    internal_note = fields.Text(string="Internal Note")

    @api.multi
    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['internal_note'] = self.internal_note
        return invoice_vals

#    @api.multi
#    def _prepare_invoice(self):
#        invoice_vals = super(SaleOrder, self)._prepare_invoice()
#        invoice_vals["internal_note"] = self.internal_note or False
#    return internal_note
#    #        res = super().prepare_invoice
#    #        res["internal_note"] = self.internal_note
#    return res


#    @api.multi
#    def _prepare_invoice(self):
#        invoice_vals = super(<your_class_name>, self)._prepare_invoice()
#        invoice_vals['condition'] = self.condition  or False
#        return invoice_vals

# i got this function
#   @api.multi
#   def _prepare_invoice(self):
#        invoice_vals = super(SaleOrder, self)._prepare_invoice()
#        invoice_vals['incoterms_id'] = self.incoterm.id or False
#        return invoice_vals
#
# do i change it as
#
#   @api.multi
#    def _prepare_invoice(self):
#        invoice_vals = super(SaleOrder, self)._prepare_invoice()
#        invoice_vals['incoterms_id'] = self.incoterm.id or False
#        invoice_vals['x_conditions'] = self.x_conditions or False
#        return invoice_vals