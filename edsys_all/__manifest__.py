{
    'name': 'Edsys All Module Install',
    'version': '1.0',
    'category': 'Edsys Education',
    "sequence": 3,
    'summary': 'Install All edsys related modules.',
    'complexity': "easy",
    'description': """
            This module provide overall education management system over OpenERP
                                        And
            Install All Related Modules. 
            
    """,
    'author': "Edsys",
    "website": "https://www.edsys.in/",

    'images': [],
    'depends': ['base','account','account_accountant','sale',
		#'account_period',
                'account_voucher','point_of_sale','mail','hr_holidays',
                'account_asset','account_accountant','website','purchase','hr',
#                'account_advance_payment','account_anglo_saxon',
		'hr_attendance',
                'account_bank_statement_import','analytic',
#                'hr_public_holidays',
		'sale_stock','portal_sale',
                'payment_transfer','stock',
		'backend_theme_v10',
                'edsys_users_dependency',
                'edsys_edu_masters',
                'edsys_edu_fee',
                'edsys_edu',
                'openeducat_core',
                'openeducat_library',
                'edsys_fee_enhancement',
                'edsys_promotion',
                'edsys_fee',
                'edsys_fee_enhancement',
                'edsys_strike_off',
                'edsys_edu_re_registration',
                'edsys_transfer_certificate',
                'edsys_pdc',
                'edsys_capturing_online_payment',
                'edsys_paperless_registrations',
                # 'edsys_biometric',
                'edsys_hrm',
                'edsys_pos',
                'edsys_sequence',
                #'edsys_sync',
                'edsys_aged_partner_xls',
                'edsys_asset',

                'database_cleanup',
                #'report_xls',
                #'aos_report_webkit',
                #'web_responsive',
                'website_student_enquiry',
                'pdc_detail',
                'full_screen_form',

                ],
    'data': [],
    'demo': [],
    'css': [],
    'qweb': [],
    'js': [],
    'price':0,
    'currency':'EUR',
    'test': [],
    'images': [],
    'installable': True,
    'auto_install': False,
    'application': True,
}
