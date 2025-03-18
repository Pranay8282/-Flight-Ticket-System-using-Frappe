import frappe
from frappe.model.document import Document

class Airport(Document):
    def __init__(self, *args, **kwargs):
        super(Airport, self).__init__(*args, **kwargs)
    
    def validate(self):
        if not self.name:
            frappe.throw("Airport Code is required")
    
    # Remove on_update and update_shop_counts methods from here
    
    # Add these as properties instead
    @property
    def available_shops(self):
        """Get real-time count of available shops."""
        airport_code = self.code
        result = frappe.db.sql("""
            SELECT COUNT(*) 
            FROM `tabShop` 
            WHERE airport = %s
            AND status = %s
        """, (airport_code, 'Available'), as_dict=False)
        return result[0][0] if result else 0
    
    @property
    def occupied_shops(self):
        """Get real-time count of occupied shops."""
        airport_code = self.code
        result = frappe.db.sql("""
            SELECT COUNT(*) 
            FROM `tabShop` 
            WHERE airport = %s
            AND status = %s
        """, (airport_code, 'Occupied'), as_dict=False)
        return result[0][0] if result else 0