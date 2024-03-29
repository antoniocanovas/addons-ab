# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "MRP Simple",
    "summary": "",
    "version": "14.0.1.0.0",
    "category": "Manufacturing",
    "author": "Pedro Guirao, ",
    "website": "https://github.com/OCA/account-analytic",
    "license": "AGPL-3",
    "depends": ["mrp_bom_group", "hr_timesheet", 'base_automation'],
    "data": ["views/mrp_view.xml",
             "views/product_product_view.xml",
             "views/menu_views.xml",
             "data/actualiza_lista_materiales.xml",
             "views/label_production_view_pdf.xml"],
    "installable": False,
}
