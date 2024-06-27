from odoo import api, models, _


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, body='', **kwargs):
        #send message to related partner        
        if hasattr(self, 'partner_id') and self.partner_id:
            msg = _('<b>[%(object)s]</b> %(body)s',object=self._get_html_link(), body=body)
            self.partner_id.message_post(body=msg, **kwargs)
        return super(MailThread, self).message_post(body=body, **kwargs)
    