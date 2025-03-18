import frappe

@frappe.whitelist()
def get_shop_counts(airport_code):
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
    
    return {
        "available": available_count,
        "occupied": occupied_count
    }