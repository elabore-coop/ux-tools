# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models

class IrActionsServer(models.Model):
    """ Add activity plan option in server actions. """
    _inherit = 'ir.actions.server'

    state = fields.Selection(selection_add=[('generate_activities', 'Generate activities from a plan')],
                             ondelete={'generate_activities': 'cascade'})

    plan_id = fields.Many2one('mail.activity.plan', string='Available plans', help='choose a plan to add in server action options')

    def _run_action_generate_activities_multi(self, eval_context=None):
        '''
        Function called automaticly when lauching action server
        See ir_actions._get_runner()
        '''
        records = self.env[self.model_name].browse(self._context.get('active_ids', self._context.get('active_id')))
        for record in records :
            for mail_activity_template in self.plan_id.mail_activity_template_ids:
                date_deadline = self.env['mail.activity']._calculate_date_deadline(mail_activity_template.mail_activity_type_id)
                record.activity_schedule(
                    activity_type_id=mail_activity_template.mail_activity_type_id.id,
                    summary=mail_activity_template.summary,
                    note=mail_activity_template.note,
                    user_id=mail_activity_template.user_id.id,
                    date_deadline=date_deadline
                )   
        return False

