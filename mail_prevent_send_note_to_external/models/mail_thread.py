from odoo import api, models, _


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):    
        #check subtype_xmlid and partner_ids, and remove external partners if subtype is "note"
        if kwargs.get("subtype_xmlid") == 'mail.mt_note' and "partner_ids" in kwargs:
            new_partner_ids = []
            for partner_id in kwargs["partner_ids"]:
                user = self.env["res.users"].search([('partner_id','=',partner_id)])
                if user.active and user.has_group('base.group_user'):
                    new_partner_ids.append(partner_id)
            kwargs["partner_ids"] = new_partner_ids

        message = super(MailThread, self).message_post(**kwargs)
        return message