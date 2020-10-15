from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    internal_note = fields.Text(string="Internal Note")

#    origin_m2o = fields.Many2one(
#        comodel_name='sale.order',
#        compute='_compute_origin',
#    )
#
#    @api.one
#    @api.depends('origin')
#    def _compute_origin(self):
#        self.origin_m2o = self.env['sale.order'].search([('name', '=', self.origin)], limit=1).id

    @api.onchange('internal_note')
    def _onchange_internal_note(self):
        so = self.env['sale.order'].search([('name', '=', self.origin)], limit=1)
        so.write({'internal_note' : self.internal_note})