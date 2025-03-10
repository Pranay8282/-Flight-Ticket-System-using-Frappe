# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

# airport.py

import frappe
from frappe.model.document import Document

class Airport(Document):
    def __init__(self, *args, **kwargs):
        super(Airport, self).__init__(*args, **kwargs)

    def validate(self):
        # Example validation logic
        if not self.airport_name:
            frappe.throw(_("Airport Name is required"))
    
    def on_update(self):
        # Example action on update
        frappe.msgprint(f"Airport {self.airport_name} has been updated!")

    # Add any additional methods you need for this Doctype
