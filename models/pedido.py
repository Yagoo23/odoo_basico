from odoo import models, fields, api

class pedido(models.Model):
    _name = 'odoo_basico.pedido'
    _description = 'Exemplo de pedido'

    name = fields.Char(string="Identificador: ",required=True,size=20)
    descripcion_do_pedido = fields.Text(string="A descripción: ")
    # Os campos One2many Non se almacenan na BD
    lineapedido_ids = fields.One2many("odoo_basico.lineapedido", 'pedido_id')

    def actualizadorSexo(self):
        informacion_ids = self.env['odoo_basico.informacion'].search([('autorizado', '=', False)])
        for rexistro in informacion_ids:
            self.env['odoo_basico.informacion']._cambia_campo_sexo(rexistro)