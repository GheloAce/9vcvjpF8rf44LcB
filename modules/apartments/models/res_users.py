# ODOO
from openerp import models, fields, api


class Users(models.Model):
    _inherit = "res.users"

    # FIELDS
    name = fields.Char("First Name")
    last_name = fields.Char("Last Name")

    # RELATE
    apartment_ids = fields.One2many("space.apartments", "user_id", "Apartments")