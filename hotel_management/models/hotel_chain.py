# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class HotelChain(models.Model):
    _inherit = "res.partner"
    _rec_name = "hotel_chain_name"

    hotel_chain_name = fields.Char(string="Hotel Chain Name")
    country_of_origin = fields.Char(string="Country of Origin")
    headquarters_address = fields.Char(string="Headquarters Address")
    total_hotels = fields.Integer(string="Total Number of Hotels")
    chain_category = fields.Selection(
        [
            ("luxury", "Luxury"),
            ("economy", "Economy"),
            ("boutique", "Boutique"),
            ("other", "Other"),
        ],
        string="Chain Category",
    )
    corporate_website = fields.Char(string="Corporate Website")
    corporate_contact_info = fields.Text(string="Corporate Contact Information")
    foundation_date = fields.Date(string="Foundation Date")
    financial_information = fields.Text(string="Financial Information")
    hotel_affiliation_status = fields.Selection(
        [("active", "Active"), ("inactive", "Inactive")],
        string="Hotel Affiliation Status",
    )
