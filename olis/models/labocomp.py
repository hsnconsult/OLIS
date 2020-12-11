# -*- coding: utf-8 -*-

import logging
from datetime import timedelta
from datetime import datetime
from functools import partial
from odoo.osv import expression

import psycopg2
import pytz

from odoo import api, fields, models, tools, _
from odoo.tools import float_is_zero
from odoo.exceptions import UserError
from odoo.http import request
from odoo.addons import decimal_precision as dp
from odoo.tools.enlettres import convlettres

class clinic_echantillon(models.Model):
    _name = "clinic.echantillon"
    _description = "Echantillon"

    def valider(self):
        for record in self.idexamen:
            record.state = 'reculabo'
        company_id = self.env.user.company_id
        for frais in self:
            if frais.name == '':
                frais.name = str(datetime.now().year)+frais.idreception.name+company_id.sequenceechantillon.next_by_id()+'H'
        self.write({'state':'valide'})

    idreception = fields.Many2one('clinic.recepechant','Reception', required=True)
    name = fields.Char('Référence',copy=False, readonly=True, index=True, default='')
    idexamen = fields.Many2many('clinic.opcaisse.ligne', string='Examens')
    state = fields.Selection([('brouillon','Brouillon'),('valide','Validé'),('rejete','Rejeté')], string='Etat', size=64, default='brouillon' ,track_visibility='onchange', readonly=True, required=True)
    

