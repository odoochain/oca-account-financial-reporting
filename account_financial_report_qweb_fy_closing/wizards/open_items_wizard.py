# -*- coding: utf-8 -*-
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, models


class OpenItemsReportWizard(models.TransientModel):
    _inherit = 'open.items.report.wizard'

    @api.multi
    def button_export_pdf(self):
        obj = self.with_context(
            exclude_closing_types=['opening', 'closing']
        )
        return super(OpenItemsReportWizard, obj).button_export_pdf()

    @api.multi
    def button_export_xlsx(self):
        obj = self.with_context(
            exclude_closing_types=['opening', 'closing']
        )
        return super(OpenItemsReportWizard, obj).button_export_xlsx()
