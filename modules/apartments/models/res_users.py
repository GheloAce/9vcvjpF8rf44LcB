# ODOO
from openerp import models, fields, api
# ADDONS
import openerp.addons.decimal_precision as dp


class Users(models.Model):
    _inherit = "res.users"

    # FIELDS
    name = fields.Char("First Name")
    last_name = fields.Char("Last Name")

    # RELATE
    apartment_ids = fields.One2many("space.apartments", "user_id", "Apartments")

    # SEARCH
    view_users_search = fields.Char("Name or Email", store=False, search="_search_general")

    # CALC
    apartment_balance = fields.Float(
        "Apartment Balance", digits=dp.get_precision('Account'), compute="_compute_apartment_balance")
    total_rented_area = fields.Float(
        "Total Area Rented", compute="_compute_total_area")

    @api.model
    def _search_general(self, operator, value):
        return ['|', ('name', operator, value), '|', ('last_name', operator, value), ('email', operator, value)]

    @api.one
    def _compute_apartment_balance(self):
        apartment_balances = self.apartment_ids.mapped('balance_eur')
        self.apartment_balance = sum(apartment_balances)

    @api.one
    def _compute_total_area(self):
        floar_area_list = self.apartment_ids.mapped('floor_area')
        self.total_rented_area = sum(floar_area_list)