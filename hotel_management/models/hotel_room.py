# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = _('Module for room management in hotels.')

    name = fields.Char(string='Room Number')
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
        ('penthouse', 'Penthouse')],
        string='Room Type', default='single')
    availability = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance')],
        string='Room State', default='available')
    bed_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
    ], string='Bed Type')
    room_size = fields.Float(string='Room Size (m²)')
    room_capacity = fields.Integer(string='Room Capacity')
    room_description = fields.Text(string='Room Description')
    services_included = fields.Text(string='Services Included')
    room_amenities = fields.Text(string='Room Amenities')
    base_price = fields.Float(string='Base Price per Night')
    discount_rate = fields.Float(string='Discount Rate (%)')
    special_rate = fields.Float(string='Special Price per Night')
    service_requests = fields.Text(string='Service Requests')
    inventory_items = fields.Text(string='Inventory Items')
    maintenance_schedule = fields.Text(string='Maintenance Schedule')
    last_cleaning_date = fields.Date(string='Last Cleaning Date')
    facilities_id = fields.Many2one('hotel.facilities', string='Facilities')
    number_of_beds = fields.Integer(string='Number of Beds')
    floor = fields.Integer(string='Floor')
    room_code = fields.Char(string='Room Code')
    image = fields.Binary(string='Image')
    comments = fields.Text(string='Comments')
    last_occupation_date = fields.Date(string='Last Occupation Date')
