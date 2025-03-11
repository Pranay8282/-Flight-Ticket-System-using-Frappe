# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_datetime

class RentReceip(Document):
    def generate_receipt_number(self):
        """
    Generates the receipt number in the format:
    RR-{tenant}-{payment_date}-{serial_number}
    """
        tenant = self.tenant  # Get tenant name from the doc
        payment_date = self.payment_date.strftime('%Y-%m-%d')  # Get payment date in YYYY-MM-DD format

    # Base part of the receipt number (RR-{tenant}-{payment_date})
        base_receipt_number = f"RR-{tenant}-{payment_date}"

    # Set a naming series for the serial number (##### is 5 digits)
        naming_series = "#####"

    # Generate the serial number using the getseries method
        serial_number = frappe.model.naming.getseries(naming_series,5)

    # Combine the base receipt number and serial number
        receipt_number = f"{base_receipt_number}-{serial_number}"

        return receipt_number

    def before_insert(self):
        """
    This function is called before saving the document to generate the receipt number.
    """
        self.receipt_number = self.generate_receipt_number()
        self.name1=self.receipt_number
