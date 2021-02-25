# -*- coding: utf-8 -*-

from odoo import models, fields, api


# *************** Model Domaine Labo *************** -->

class ConfigDomaineLabo(models.Model):
    _name = 'teslab.domaine_labo'
    _rec_name = 'lib_domaine_lab'
    _description = "Configuration domaine de laboratoire"

    code_dom_lab = fields.Char('Code')
    lib_domaine_lab = fields.Char('Domaine')
    commentaire_dom_lab = fields.Text('Commentaire')

    unitelabo_ids = fields.One2many(comodel_name='teslab.unite_labo', inverse_name='domainelabo_id')


# *************** Model Unité Labo *************** -->
class ConfigUniteLlabo(models.Model):
    _name = 'teslab.unite_labo'
    _rec_name = 'lib_unite_lab'
    _description = 'Configuration unité de laboratoire'
    _order = 'domainelabo_id'

    code_unit_lab = fields.Char('Code')
    lib_unite_lab = fields.Char('Unité')
    commentaire_unit_lab = fields.Text('Commentaire')

    domainelabo_id = fields.Many2one(comodel_name='teslab.domaine_labo')
    rubriquelabo_ids = fields.One2many(comodel_name='teslab.rubrique_labo', inverse_name='unitelabo_id')


# *************** Model Rubrique Labo *************** -->
class ConfigRubriqueLabo(models.Model):
    _name = 'teslab.rubrique_labo'
    _rec_name = 'lib_rubrique_lab'
    _description = "Configuration rubrique de laboratoire"

    code_rub_lab = fields.Char('Code')
    lib_rubrique_lab = fields.Char('Rubrique')
    commentaire_rub_lab = fields.Text('Commentaire')

    unitelabo_id = fields.Many2one(comodel_name='teslab.unite_labo')
    test_lab_ids = fields.One2many(comodel_name='teslab.test_labo', inverse_name='rub_lab_id')


# *************** Model Test Labo *************** -->
class ConfigTestLabo(models.Model):
    _name = 'teslab.test_labo'
    _rec_name = 'lib_test_lab'
    _description = "Configuration test de laboratoire"

    code_int_test_lab = fields.Char('Code interne')
    code_fab_test_lab = fields.Char('Code fabriquant')
    code_univ_test_lab = fields.Char('Code universel')
    lib_test_lab = fields.Char('Test')
    val_max_test_lab = fields.Float('Val max')
    val_min_test_lab = fields.Float('Val min')
    operateur = fields.Selection([('', ''), ('=', 'Egal'), ('<', 'Inf. à'), ('>', 'Sup. à')])
    commentaire_test_lab = fields.Text('Commentaire')

    rub_lab_id = fields.Many2one(comodel_name='teslab.rubrique_labo')
    valeur_result_ids = fields.Many2many('teslab.valeur_resultat', strinng='Valeur résultat')
    prestation_ids = fields.Many2many('product.template', strinng='Prestation')


# *************** Model Valeur Résultat Labo *************** -->
class ConfigValeurResultat(models.Model):
    _name = 'teslab.valeur_resultat'
    _rec_name = 'lib_val_result'
    _description = "Configuration valeur résultat de laboratoire"

    code_val_result = fields.Char('Code')
    lib_val_result = fields.Char('Nom resultat')
    type_val_result = fields.Selection(
        [('num', 'Numérique'), ('carct', 'Caratère'), ('date', 'Date'), ('dure', 'Durée')])
    commentaire_val_result = fields.Text('commentaire')

    test_labo_ids = fields.Many2many('teslab.test_labo', strinng='Tests labo')

class ProductTemplate(models.Model):
    _name = "product.template"
    _description = "Product Template"
    _inherit = "product.template"
    _order = "name"
    testlab_ids = fields.Many2many('teslab.test_labo', string='Tests Labo')