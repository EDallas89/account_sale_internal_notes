from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    internal_note = fields.Text(
        string="Internal Note",
        related='origin_m2o.internal_note',
    )

    origin_m2o = fields.Many2one(
        comodel_name='sale.order',
        compute='_compute_origin',
    )

    @api.one
    @api.depends('origin')
    def _compute_origin(self):
        self.origin_m2o = self.env['sale.order'].search([('name', '=', self.origin)], limit=1).id