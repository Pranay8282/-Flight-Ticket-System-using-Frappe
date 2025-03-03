# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Airline(Document):
    def validate(self):
        # Ensure Founding Year is non-negative
        if self.founding_year and self.founding_year < 0:
            frappe.throw("Founding Year cannot be negative.")
