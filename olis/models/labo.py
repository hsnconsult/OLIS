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


class clinic_recepechant(models.Model):
    _name = "clinic.recepechant"
    _description = "Reception echantillon"

    def selectionner(self):
        #suppression des anciennes lignes
        for record in self.ligne_examen:
            record.idreception = ''
        #ajout des nouvelles lignes
        for record in self.idtarif.ligne_opcaisse:
            record.idreception = self.id
    @api.depends('idpatient')
    def get_nompatient(self):
        for record in self:
            record.nompatient = record.idpatient.nom + ' ' + record.idpatient.prenom if record.idpatient.nom and record.idpatient.prenom else ''

    def valider(self):
        company_id = self.env.user.company_id
        for frais in self:
            if frais.name == '':
                frais.name = company_id.sequencereception.next_by_id()
        self.write({'state':'valide'})
    name = fields.Char('Référence',copy=False, readonly=True, index=True, default='')
    idpatient = fields.Many2one('clinic.patient', 'NDM')
    nompatient = fields.Char('Nom du patient', compute='get_nompatient')
    idtarif = fields.Many2one('clinic.opcaisse', string="N° Tarification")
    ligne_examen = fields.One2many('clinic.opcaisse.ligne','idreception','Lignes examen')
    ligne_echantillon = fields.One2many('clinic.echantillon','idreception','Lignes echantillon')
    state = fields.Selection([('brouillon','Brouillon'),('valide','Validé')], string='Etat', size=64, default='brouillon' ,track_visibility='onchange', readonly=True, required=True)

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
    

