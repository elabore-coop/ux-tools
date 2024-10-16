# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models


class MailActivityTemplate(models.Model):
    '''
    Describe activities to run when lauching the associated plan
    '''
    _name = 'mail.activity.template'
    _description = 'Mail activity template'
    _order = 'sequence'
    _rec_name = 'summary'

    mail_activity_plan_id = fields.Many2one('mail.activity.plan', ondelete='restrict')

    mail_activity_type_id = fields.Many2one(
        'mail.activity.type', 'Activity Type',
        default=lambda self: self.env.ref('mail.mail_activity_data_todo'),
        ondelete='restrict'
    )

    sequence = fields.Integer('Sequence', default=1, help="Used to order activities.")
    summary = fields.Char('Summary')
    user_id = fields.Many2one('res.users', string='Assigned to')
    note = fields.Html('Note')

class MailActivityPlan(models.Model):
    '''
    Create a plan
    A plan is linked to many templates of mail activity (mail.activity.template)

    '''
    _name = 'mail.activity.plan'
    _description = 'Mail activity plan'

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {},
                       name=_("%s (copy)", self.name))
        return super(MailActivityPlan, self).copy(default=default)

    name = fields.Char('Name', required=True)
    mail_activity_template_ids = fields.One2many('mail.activity.template', 'mail_activity_plan_id', string='Template Activities', copy=True)
    active = fields.Boolean(default=True)
