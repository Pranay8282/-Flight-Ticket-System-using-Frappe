import frappe
from frappe.model.document import Document

class Airport(Document):
    def __init__(self, *args, **kwargs):
        super(Airport, self).__init__(*args, **kwargs)

    def validate(self):

        if not self.name:
            frappe.throw(   ("Airport Code is required"))

    def on_update(self):

        if not hasattr(self, "skip_shop_update"):
            self.skip_shop_update = True
            self.update_shop_counts()
            del self.skip_shop_update

    def update_shop_counts(self):
        """Update the count of available and occupied shops linked to the airport."""

        airport_code = self.code  


        available_shops_count = frappe.db.sql("""
            SELECT COUNT(*) 
            FROM `tabShop` 
            WHERE airport = %s
            AND status = %s
        """, (airport_code, 'Available'), as_dict=False)


        occupied_shops_count = frappe.db.sql("""
            SELECT COUNT(*) 
            FROM `tabShop` 
            WHERE airport = %s
            AND status = %s
        """, (airport_code, 'Occupied'), as_dict=False)


        available_count = available_shops_count[0][0] if available_shops_count else 0
        occupied_count = occupied_shops_count[0][0] if occupied_shops_count else 0


        self.int_lnxb = available_count
        self.occupied_shops = occupied_count


        frappe.db.commit()

