# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

# shop.py

import frappe
from frappe.model.document import Document

class Shop(Document):
    def __init__(self, *args, **kwargs):
        super(Shop, self).__init__(*args, **kwargs)

    def validate(self):
        # Example validation logic
        if not self.shop_name:
            frappe.throw(_("Shop Name is required"))
    
    def on_update(self):
        # Example action on update
        frappe.msgprint(f"Shop {self.shop_name} has been updated!")

    # Link the shop to an airport
    def link_to_airport(self, airport_name):
        airport = frappe.get_doc("Airport", airport_name)
        self.airport = airport.name
        self.save()
        frappe.db.commit()

    # Add any additional methods you need for this Doctype
