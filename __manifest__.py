# -*- coding: utf-8 -*-
{
    'name': "abc_hms",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/abc_hms_appointments.xml',
        'views/res_config_settings.xml',
        'views/res_partner.xml',
        'views/product_template.xml',
        'views/sale_order.xml',
        'views/patient.xml',
        'views/medical_patient_disease.xml',
        'views/medical_vaccination.xml',
        ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
