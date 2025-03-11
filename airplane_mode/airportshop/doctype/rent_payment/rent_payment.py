# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime

class RentPayment(Document):
    def before_insert(self):
        # Check if the receipt_number is not already set (in case it's manually provided)
        if not self.receipt_number:
            # Generate the receipt number based on the Naming Series
            self.receipt_number = self.generate_receipt_number()

    def generate_receipt_number(self):
        # This assumes 'RCT-.YYYY.-.#####' as your naming series
        naming_series = 'RCT-.YYYY.-.#####'

        # Generate the receipt number
        receipt_number = frappe.model.naming.getseries(naming_series,5)

        # Add the current year manually (if not included by getseries)
        current_year = datetime.now().year
        formatted_receipt_number = f"RCT-{current_year}-{receipt_number}"

        return formatted_receipt_number
