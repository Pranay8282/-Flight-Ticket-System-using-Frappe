import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):

    def before_submit(self):
        """Prevent submission if status is not 'Boarded'."""
        if self.status != "Boarded":
            frappe.throw("You can only submit the Airplane Ticket if the status is 'Boarded'.")

    def autoname(self):
        """Generate a unique name based on Flight, Source & Destination Airport, and Ticket Number"""
        if not self.flight or not self.source_airport_code or not self.destination_airport_code:
            frappe.throw("Flight, Source Airport Code, and Destination Airport Code are required for naming.")

        # Get the number of passengers already booked for this flight
        passenger_count = self.get_passenger_count()

        # Naming format: <Flight Name>-<Source Airport Code>-to-<Destination Airport Code>-<No. of Passengers>
        self.name = f"{self.flight}-{self.source_airport_code}-to-{self.destination_airport_code}-{passenger_count}"

    def get_passenger_count(self):
        """Count the number of passengers already booked for the same flight"""
        count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})
        return count + 1  # Increment by 1 for the new entry

    def validate(self):
        self.calculate_total_amount()
        self.remove_duplicate_add_ons()
        self.assign_seat()

    def calculate_total_amount(self):
        """Calculates Total Amount = Flight Price + Sum of Add-on Amounts"""
        total_add_on_amount = sum([item.amount for item in self.get("add_ons")])
        self.total_amount = self.flight_price + total_add_on_amount

    def remove_duplicate_add_ons(self):
        """Ensures that no duplicate add-ons are added"""
        unique_items = {}
        cleaned_add_ons = []

        for item in self.get("add_ons"):
            if item.item not in unique_items:
                unique_items[item.item] = True
                cleaned_add_ons.append(item)

        self.set("add_ons", cleaned_add_ons)

    def assign_seat(self):
        """Auto-assign a random seat from available ones"""
        available_seats = [
            f"{row}{col}" for row in range(1, 31) for col in "ABCDEF"
        ]
        self.seat = random.choice(available_seats)
