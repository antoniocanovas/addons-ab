# Copyright 2021 IC - Pedro Guirao
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Reports Abasto",
    "summary": "Reports Abasto",
    "version": "14.0.0.0.0",
    "category": "Reports",
    "author": "SerinCloud, ",
    "website": "https://ingeniriacloud.com",
    "license": "AGPL-3",
    "depends": ['inventory',
                "ab_custom_mrp",
                "mrp",
                ],
    "data": [
        "views/label_production_view_pdf.xml",
    ],
    "installable": True,
}
