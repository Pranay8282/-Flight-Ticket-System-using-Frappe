import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):


    def autoname(self):
        """Generate a unique name based on Flight, Source & Destination Airport, and Ticket Number"""
        if not self.flight or not self.source_airport_code or not self.destination_airport_code:
            frappe.throw("Flight, Source Airport Code, and Destination Airport Code are required for naming.")

        passenger_count = self.get_passenger_count()


        self.name = f"{self.flight}-{self.source_airport_code}-to-{self.destination_airport_code}-{passenger_count}"

    def get_passenger_count(self):
        """Count the number of passengers already booked for the same flight"""
        count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})
        return count + 1  
    def validate(self):
        """Validation before saving the record"""
        self.calculate_total_amount()
        self.remove_duplicate_add_ons()
        self.assign_seat_if_needed()
        self.check_flight_capacity()  
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

    def assign_seat_if_needed(self):
        """Auto-assign a random seat from available ones if not already assigned"""
        if not self.seat:  
            self.assign_seat()

    def assign_seat(self):
        """Assign a random seat from available ones"""
        available_seats = [
            f"{row}{col}" for row in range(1, 31) for col in "ABCDEF"
        ]
        self.seat = random.choice(available_seats) 

    def check_flight_capacity(self):
        """Prevents creation of a new Airplane Ticket if the number of tickets exceeds airplane's capacity"""
        flight_doc = frappe.get_doc("Airplane Flight", self.flight)
        airplane = frappe.get_doc("Airplane", flight_doc.airplane)  


        airplane_capacity = airplane.capacity


        booked_ticket_count = frappe.db.count("Airplane Ticket", filters={"flight": self.flight, "status": "Booked"})

        if booked_ticket_count >= airplane_capacity:
            frappe.throw(f"Cannot create ticket. The number of booked tickets for this flight ({self.flight}) has exceeded the airplane's capacity ({airplane_capacity} seats).")
