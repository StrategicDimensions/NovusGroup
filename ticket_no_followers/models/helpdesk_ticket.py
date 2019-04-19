# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Helpdesk_Ticket(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.model
    def create(self, vals):
        res = super(Helpdesk_Ticket, self).create(vals)
        SQL = "delete from mail_followers where res_model = 'helpdesk.ticket' and res_id = %s"%(res.id)
        self._cr.execute(SQL)
        return res