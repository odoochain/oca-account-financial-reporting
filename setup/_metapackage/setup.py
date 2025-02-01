import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-account-financial-reporting",
    description="Meta package for oca-account-financial-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-account_financial_report>=15.0dev,<15.1dev',
        'odoo-addon-account_financial_report_sale>=15.0dev,<15.1dev',
        'odoo-addon-account_move_line_report_xls>=15.0dev,<15.1dev',
        'odoo-addon-account_purchase_stock_report_non_billed>=15.0dev,<15.1dev',
        'odoo-addon-account_sale_stock_report_non_billed>=15.0dev,<15.1dev',
        'odoo-addon-account_tax_balance>=15.0dev,<15.1dev',
        'odoo-addon-mis_builder_cash_flow>=15.0dev,<15.1dev',
        'odoo-addon-mis_template_financial_report>=15.0dev,<15.1dev',
        'odoo-addon-partner_statement>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
