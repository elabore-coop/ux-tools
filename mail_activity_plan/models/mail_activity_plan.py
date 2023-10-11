# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class MailActivityTemplate(models.Model):
    '''
    Describe activities to run when lauching the associated plan
    '''
    _name = 'mail.activity.template'
    _description = 'Mail activity template'

    mail_activity_plan_ids = fields.Many2many('mail.activity.plan', string='Activities plan', ondelete='restrict')

    mail_activity_type_id = fields.Many2one(
        'mail.activity.type', 'Activity Type',
        default=lambda self: self.env.ref('mail.mail_activity_data_todo'),
        ondelete='restrict'
    )
    summary = fields.Char('Summary', compute="_compute_default_summary", store=True, readonly=False)
    user_id = fields.Many2one('res.users', string='Assigned to', required=True)
    note = fields.Html('Note')

    @api.depends('mail_activity_type_id')
    def _compute_default_summary(self):
        for mail_activity_template in self:
            if not mail_activity_template.summary and mail_activity_template.mail_activity_type_id and mail_activity_template.mail_activity_type_id.summary:
                mail_activity_template.summary = mail_activity_template.mail_activity_type_id.summary

class MailActivityPlan(models.Model):
    '''
    Create a plan
    A plan is linked to many templates of mail activity (mail.activity.template)

    '''
    _name = 'mail.activity.plan'
    _description = 'Mail activity plan'

    name = fields.Char('Name', required=True)
    mail_activity_template_ids = fields.Many2many('mail.activity.template', string='Activity template', ondelete='restrict')
    active = fields.Boolean(default=True)
