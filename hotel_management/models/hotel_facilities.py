# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class HotelFacilities(models.Model):
    _name = "hotel.facilities"
    _description = _("Hotel Facilities")
    _rec_name = "hotel_name"

    # Fields for hotel-specific information
    hotel_name = fields.Char(string="Hotel Name")
    hotel_chain_id = fields.Many2one(
        "res.partner", string="Hotel Chain", help="Select the hotel chain"
    )
    hotel_type = fields.Selection(
        [
            ("boutique", "Boutique"),
            ("resort", "Resort"),
            ("economy", "Economy"),
            ("luxury", "Luxury"),
        ],
        string="Hotel Type",
    )
    hotel_category = fields.Selection(
        [
            ("1_star", "1 Star"),
            ("2_star", "2 Stars"),
            ("3_star", "3 Stars"),
            ("4_star", "4 Stars"),
            ("5_star", "5 Stars"),
        ],
        string="Hotel Category",
    )
    number_of_rooms = fields.Integer(string="Number of Rooms")
    hotel_address = fields.Char(string="Hotel Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State/Province")
    country = fields.Char(string="Country")
    postal_code = fields.Char(string="Postal Code")
    website = fields.Char(string="Website")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    image = fields.Binary(string="Hotel Photo")
    description = fields.Text(string="Description")
