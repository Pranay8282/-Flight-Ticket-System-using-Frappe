import frappe
from frappe.model.document import Document

class Airplane(Document):
    def autoname(self):
        # Fetch the Airline Name
        airline_name = self.airline
        
        # Get the last airplane record for the same airline
        last_airplane = frappe.db.sql(
            """SELECT name FROM `tabAirplane` 
            WHERE airline=%s ORDER BY creation DESC LIMIT 1""",
            (airline_name),
            as_dict=True
        )

        # Extract last number and increment
        if last_airplane:
            last_name = last_airplane[0]["name"]
            last_number = int(last_name.split("-")[-1])  # Extract last number
            new_number = last_number + 1
        else:
            new_number = 1  # Start numbering from 001

        # Set name in format: AirlineName-XXX
        self.name = f"{airline_name}-{new_number:03d}"
