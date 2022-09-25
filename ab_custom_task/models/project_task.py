# -*- coding: utf-8 -*-
##############################################################################
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
#    Copyright (C) 2021 Serincloud S.L. All Rights Reserved
#    PedroGuirao pedro@serincloud.com
##############################################################################
from odoo import api, fields, models, _

class ProjectTask(models.Model):
    _inherit = "project.task"

    is_closed = fields.Boolean(store=True)

    @api_depends('timesheet_ids.date_time', 'timesheet_ids.date_time_end')
    def get_ab_stage(self):
        hidden = True
        for li in record.timesheet_ids:
            if li.date_time and not li.date_time_end:
                hidden = False
        record.ab_stage = hidden

    ab_stage = fields.Boolean('ab_stage', store=True, compute=get_ab_stage)

    def button_task_done(self):
        for record in self:
            state_done = self.env['project.task.type'].search([('is_closed','=',True),('id','in',record.project_id.type_ids.ids)])[0]
            if stage_done:
                record.stage_id = state_done.id
            # else mensaje "no hay etapa de cierre"

    def button_start_work_task_user(self):
        for record in self:
            self.env['account.analytic.line'].create({'name': record.name,
                                                 'account_id': record.project_id.analytic_account_id.id,
                                                 'task_id': record.id,
                                                 'set_start_stop': True,
                                                 'employee_id': record.user_id.employee_id.id,
                                                 'user_id': record.user_id.id})
