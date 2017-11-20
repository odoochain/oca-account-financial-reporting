from openerp import api, models


class GeneralLedgerReportCompute(models.TransientModel):
    _inherit = 'report_general_ledger_qweb'

    def _get_account_sub_subquery_sum_amounts(self, include_initial_balance,
                                              date_included):
        res = super(
            GeneralLedgerReportCompute, self,
        )._get_account_sub_subquery_sum_amounts(
            include_initial_balance, date_included,
        )
        if self.env.context.get('exclude_closing_types'):
            index = res.find("GROUP BY")
            res = (
                res[:index] + """
                INNER JOIN account_move am
                ON am.id = ml.move_id
                AND am.closing_type NOT IN %s
                """ % str(tuple(self.env.context['exclude_closing_types'])) +
                res[index:]
            )
        return res

    def _get_partner_sub_subquery_sum_amounts(
            self, only_empty_partner, include_initial_balance, date_included
    ):
        res = super(
            GeneralLedgerReportCompute, self,
        )._get_partner_sub_subquery_sum_amounts(
            only_empty_partner, include_initial_balance, date_included,
        )
        if self.env.context.get('exclude_closing_types'):
            index = res.find("GROUP BY")
            res = (
                res[:index] + """
                INNER JOIN account_move am
                ON am.id = ml.move_id
                AND am.closing_type NOT IN %s
                """ % str(tuple(self.env.context['exclude_closing_types'])) +
                res[index:]
            )
        return res
