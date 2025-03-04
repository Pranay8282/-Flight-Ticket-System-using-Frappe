import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):

    def autoname(self):
        """Generate a unique name based on Flight, Source, and Destination"""
        if not self.flight or not self.source_airport_code or not self.destination_airport_code:
            frappe.throw("Flight, Source Airport Code, and Destination Airport Code are required for naming.")

        # Get last ticket with the same Flight, Source, and Destination
        last_ticket = frappe.db.sql(
            """
            SELECT name FROM `tabAirplane Ticket`
            WHERE flight=%s AND source_airport_code=%s AND destination_airport_code=%s
            ORDER BY creation DESC LIMIT 1
            """,
            (self.flight, self.source_airport_code, self.destination_airport_code),
            as_dict=True
        )

        last_seq = 1  # Default sequence number

        if last_ticket:
            last_name = last_ticket[0]['name']
            parts = last_name.split("-")

            # Extract the last numeric part if it exists
            if parts[-1].isdigit():
                last_seq = int(parts[-1]) + 1

        self.name = f"{self.flight}-{self.source_airport_code}-to-{self.destination_airport_code}-{str(last_seq).zfill(3)}"

    def validate(self):
        self.calculate_total_amount()
        self.remove_duplicate_add_ons()

    def calculate_total_amount(self):
        """Calculates Total Amount = Flight Price + Sum of Add-on Amounts"""
        total_add_on_amount = sum([item.amount for item in self.get("add_ons", [])])
        self.total_amount = self.flight_price + total_add_on_amount

    def remove_duplicate_add_ons(self):
        """Ensures that no duplicate add-ons are added"""
        unique_items = set()
        cleaned_add_ons = []

        for item in self.get("add_ons", []):
            if item.item not in unique_items:
                unique_items.add(item.item)
                cleaned_add_ons.append(item)

        self.set("add_ons", cleaned_add_ons)
