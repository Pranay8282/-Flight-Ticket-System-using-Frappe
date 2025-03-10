# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class RentReceip(Document):
      def create_rent_receipt(doc, method):
             rent_receipt = frappe.get_doc({
        		"doctype": "Rent Receipt",
        		"tenant": doc.tenant,
        		"shop": doc.shop,
        		"amount_paid": doc.amount_paid,  # Updated field name
        		"payment_date": doc.payment_date,
        		"status": "Generated"
            })
             rent_receipt.insert()
             frappe.msgprint(f"Rent Receipt {rent_receipt.name} has been generated.")

