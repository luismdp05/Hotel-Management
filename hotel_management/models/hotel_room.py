# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = _('Module for room management in hotels.')

    name = fields.Char(string='Número de Habitación', required=True)
    room_type = fields.Selection([
        ('single', 'Individual'),
        ('double', 'Doble'),
        ('suite', 'Suite'),
        ('penthouse', 'Penthouse')], 
        string='Tipo de Habitación', default='single', required=True)
    availability = fields.Selection([
        ('available', 'Disponible'),
        ('occupied', 'Ocupada'),
        ('maintenance', 'Mantenimiento')],
        string='Estado de la Habitación', default='available', required=True)
    # hotel_id = fields.Many2one('hotel.hotel', string='Hotel')
    bed_type = fields.Selection([
        ('single', 'Individual'),
        ('double', 'Doble'),
    ], string='Tipo de Cama', required=True)
    room_size = fields.Float(string='Tamaño de la Habitación (m²)', required=True)
    room_capacity = fields.Integer(string='Capacidad de la Habitación', required=True)
    room_description = fields.Text(string='Descripción de la Habitación')
    services_included = fields.Text(string='Servicios Incluidos')
    room_amenities = fields.Text(string='Comodidades de la Habitación')
    base_price = fields.Float(string='Precio Base por Noche', required=True)
    discount_rate = fields.Float(string='Tasa de Descuento (%)')
    special_rate = fields.Float(string='Precio Especial por Noche')
    service_requests = fields.Text(string='Solicitudes de Servicio')
    inventory_items = fields.Text(string='Elementos de Inventario')
    maintenance_schedule = fields.Text(string='Programación de Mantenimiento')
    last_cleaning_date = fields.Date(string='Fecha de Última Limpieza')
    facilities = fields.Many2many('hotel.facility', string='Instalaciones')
    number_of_beds = fields.Integer(string='Número de Camas')
    floor = fields.Integer(string='Piso')
    room_code = fields.Char(string='Código de la Habitación')
    image = fields.Binary(string='Imagen')
    comments = fields.Text(string='Comentarios')
    last_occupation_date = fields.Date(string='Fecha de Última Ocupación')

class HotelFacility(models.Model):
    _name = 'hotel.facility'
    _description = 'Instalación del Hotel'

    
    name = fields.Char(string='Nombre de la Instalación', required=True)

