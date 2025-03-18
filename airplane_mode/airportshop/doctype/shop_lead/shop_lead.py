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
    

    def after_save(self):
        if self.shop and self.status == "Shop Allocated":
            shop_doc = frappe.get_doc("Shop", self.shop)


        if shop_doc.status != "Occupied":
            shop_doc.status = "Occupied"
            shop_doc.save()
        
        # Add a comment to the shop document
        frappe.get_doc({
            "doctype": "Comment",
            "comment_type": "Info",
            "reference_doctype": "Shop",
            "reference_name": self.shop,
            "content": f"Shop allocated to lead: {self.lead_name}"
        }).insert()
        
        frappe.msgprint(f"Shop {self.shop} status updated to 'Occupied'")