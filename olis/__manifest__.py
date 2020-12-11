# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'olis',
    'version' : '1.1',
    'summary': 'Gestion des centres hospitaliers',
    'sequence': 100,
    'description': """
Gestion des centres hospitaliers
====================
    """,
    'category': 'Accounting',
    'author': 'HSN Consult',
    'website': 'http://www.hsnconsult.com',
    'depends': ['account','point_of_sale',],
    'data': [
        'data/ir_sequence_data.xml',
        'security/clinic_security.xml',
        'report_views/report_recucaisse.xml',
        'report_views/report_recurecettegarde.xml',
        'report_views/report_recucaution.xml',
        'report_views/report_recureghospi.xml',
        'report_views/report_transfert.xml',
        'report_views/report_etatjour.xml',
        'report_views/report_etatjourbis.xml',
        'report_views/report_etatcloture.xml',
        'report_views/report_etatrecette.xml',
        'report_views/report_etatrecettedet.xml',
        'report_views/report_etatechant.xml',
        #'report_views/report_resultatlab.xml',
        'report_views/report_facture.xml',
        'report_views/report_factureas.xml',
        'report_views/clinic_report.xml',
        'views/clinic_view.xml',
        'views/pos_view.xml',
        'views/labo_view.xml',
        'security/ir.model.access.csv',
        ],
    'installable': True,
    'application': True,
    'auto_install': False
}
