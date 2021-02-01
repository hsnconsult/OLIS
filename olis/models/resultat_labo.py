# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Colabo_resultat_labo(models.Model):
    _name = 'teste.resultat_labo'
    _rec_name = ''

    num_echantillon = fields.Char('N° Ech.')
    code_univ_result_lab = fields.Char('Code universel')#
    lib_test_lab = fields.Char('Test')# Nom à afficher dans le rapport d'impression
    type_protocole_rasult_lab = fields.Char('Protocole')# Méthodologie utilisée pour onbténir un résultat (Dilution, manuel, CMI, Diffusion...)
    valeur_test = fields.Char('Résultat')# Résultat du test (Numérique, "positif", "Négatif"...)
    lot_reactif_result_lab = fields.Char('N° Lot')# Lot du réctif
    lot_cq_result_lab = fields.Char('N° lot CQ')# Lot du CQ
    seq_reactif_result_lab = fields.Char('N° séq réactif')#Id unique d'une cartouhe de réctif
    type_resul_lab = fields.Char('Type résultat')# F = Resultat patient ou CQ, P = Résulats préliminaire, I= Résulata intermédiaire
    unite_result_labo = fields.Char('Unité')
    val_ref_result_labo = fields.Char('val ref')
    alerte_result_labo = fields.Char('alerte') #b, bb, H, HH
    statut_result_labo = fields.Char('Statu')
    dateheure_debut_result_labo = fields.Char('Début')# date et heure de début
    dateheure_fin_result_labo = fields.Datetime('Fin')#date et heure de fin
    num_serie_instrument_result_lab = fields.Datetime('N serie instrument')
    commentaire_result_labo = fields.Html('Commentaire')