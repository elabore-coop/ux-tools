from odoo import api, models, _


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, body='', **kwargs):
        #send message to related partner        
        if hasattr(self, 'partner_id') and self.partner_id:
            msg = _('<b>[%(object)s]</b> %(body)s',object=self._get_html_link(), body=body)       

            new_kwargs = kwargs.copy()

            #new message is a note
            new_kwargs['subtype_xmlid'] = "mail.mt_note"

            #do not send anything
            new_kwargs['partner_ids'] = []            

            self.partner_id.message_post(body=msg, **new_kwargs)

        return super(MailThread, self).message_post(body=body, **kwargs)
    