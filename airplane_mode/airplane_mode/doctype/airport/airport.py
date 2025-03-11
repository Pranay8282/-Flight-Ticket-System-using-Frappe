import frappe
from frappe.model.document import Document

class Airport(Document):
    def __init__(self, *args, **kwargs):
        super(Airport, self).__init__(*args, **kwargs)

    def validate(self):
        # Example validation logic
        if not self.name:
            frappe.throw(_("Airport Code is required"))

    def on_update(self):
        # Example action on update
        if not hasattr(self, "skip_shop_update"):
            self.skip_shop_update = True
            self.update_shop_counts()
            del self.skip_shop_update

    def update_shop_counts(self):
        """Update the count of available and occupied shops linked to the airport."""
        # Get the current airport code
        airport_code = self.code  # Assuming the airport code is the 'code' field

        # Query for counting available shops
        available_shops_count = frappe.db.sql("""
            SELECT COUNT(*) 
            FROM `tabShop` 
            WHERE airport = %s
            AND status = %s
        """, (airport_code, 'Available'), as_dict=False)

        # Query for counting occupied shops
        occupied_shops_count = frappe.db.sql("""
            SELECT COUNT(*) 
            FROM `tabShop` 
            WHERE airport = %s
            AND status = %s
        """, (airport_code, 'Occupied'), as_dict=False)

        # Extract the counts from the query results
        available_count = available_shops_count[0][0] if available_shops_count else 0
        occupied_count = occupied_shops_count[0][0] if occupied_shops_count else 0

        # Set these counts into fields in the Airport document
        self.int_lnxb = available_count
        self.occupied_shops = occupied_count

        # Use frappe.db.commit to save without triggering recursion
        frappe.db.commit()

