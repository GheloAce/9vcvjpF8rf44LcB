# ODOO
from openerp import models, fields, api, exceptions


class SpaceApartments(models.Model):
    _name = "space.apartments"

    # FIELDS
    name = fields.Char("Address", required=True)
    floor_area = fields.Float(u"Area (m\u00B2)", required=True)
    balance_eur = fields.Float("Balance (EUR)")
    user_id = fields.Many2one("res.users", "Client")

    @api.one
    @api.constrains('floor_area')
    def _check_floor_area(self):
        if self.floor_area <= 0.0:
            raise exceptions.ValidationError("Floor Area needs to be greater than zero.")
