from odoo import api, fields, models

class StockTransferLineNpt(models.Model):
    _name = "stock.transfer.line.npt"
    _description = "stock transfer line"

    order_id = fields.Many2one('stock.transfer.npt', string='Order Reference', required=True,
                               ondelete='cascade', index=True, copy=False)
    name = fields.Text(string='Description', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    product_id = fields.Many2one('product.product', string='Product',
        change_default=True, ondelete='restrict')
    product_uom_qty = fields.Float(string='Quantity', digits='Product Unit of Measure', required=True, default=1.0)
