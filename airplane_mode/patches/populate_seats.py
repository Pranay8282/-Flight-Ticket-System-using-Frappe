import frappe
import random

def execute():
    """Populate the seat field for all existing Airplane Ticket documents"""
    
    # Fetch all tickets where seat is not assigned (null or empty)
    tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["=", ""]}, fields=["name"])

    if not tickets:
        print("No tickets need updating.")
        return
    
    available_seats = [f"{random.randint(1, 99)}{random.choice('ABCDE')}" for _ in range(len(tickets))]

    for ticket, seat in zip(tickets, available_seats):
        frappe.db.set_value("Airplane Ticket", ticket.name, "seat", seat)

    frappe.db.commit()
    print(f"Updated {len(tickets)} tickets with seat assignments.")
