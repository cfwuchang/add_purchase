from odoo import api, fields, models, tools, _

class PurchasePurchase(models.Model):
    _inherit = 'purchase.order.line'

    information_attachment = fields.Many2many('ir.attachment', compute='_get_attachment_ids', string=u'附件')


    def _get_attachment_ids(self):
        att_model = self.env['ir.attachment'] #获取附件模型
        for obj in self:
            query = [('res_model', '=', 'product.template'), ('res_id', '=', obj.product_id.product_tmpl_id.id)]   #根据res_model和res_id查询附件
            obj.information_attachment = att_model.search(query) #取得附件list
