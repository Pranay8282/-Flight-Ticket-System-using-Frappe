import frappe

def execute(filters=None):
    # Fetching records from the Airplane Ticket Doctype
    tickets = frappe.get_all(
        'Airplane Ticket',  # Doctype name
        fields=['name']  # Fetching the 'name' field
    )
    
    if not tickets:
        return [{'message': 'No tickets found'}]
    
    # Returning the tickets fetched
    return tickets
