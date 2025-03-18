# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

# Import necessary modules
import frappe
from frappe.model.document import Document

class ShopLead(Document):
    def before_insert(self):
        # Automatically set date_of_inquiry to today's date if not set
        if not self.date_of_inquiry:
            self.date_of_inquiry = frappe.utils.today()

        # Automatically set status to 'Interested' if empty
        if not self.status or self.status.strip() == "":
            self.status = "Interested"
