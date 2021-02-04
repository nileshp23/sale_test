from odoo import api, fields, models, _

class StockTransferNpt(models.Model):
    _name = "stock.transfer.npt"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = "stock transfer"

    sender_id = fields.Many2one('res.partner', string="Sender", help="sender partner")
    receiver_id = fields.Many2one('res.partner', string="receiver", help="receiver partner")
    order_line = fields.One2many('stock.transfer.line.npt', 'order_id', string='Transfer Lines', copy=True,
                                 auto_join=True)
    name = fields.Char(string='Transfer Reference', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            seq_date = None
            if vals:
                #seq_date = fields.Datetime.context_timestamp(self, fields.Datetime.to_datetime(vals['date_order']))
                vals['name'] = self.env['ir.sequence'].next_by_code('stock.transfer.npt') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.order', sequence_date=seq_date) or _('New')

        # Makes sure partner_invoice_id', 'partner_shipping_id' and 'pricelist_id' are defined
        result = super(StockTransferNpt, self).create(vals)
        return result
