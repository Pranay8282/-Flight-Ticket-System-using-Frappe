import frappe
from frappe.website.website_generator import WebsiteGenerator
from datetime import datetime
from frappe.model.document import Document

class AirplaneFlight(WebsiteGenerator):
    def after_save(self):
            self.route = self.name
            self.save()

    def autoname(self):
        """Generate a unique name for Airplane Flight based on the given format"""

        if not self.airplane or not self.date_of_departure:
            frappe.throw("Airplane and Date of Departure are required for naming.")

        try:
            if " " in self.date_of_departure: 
                date_obj = datetime.strptime(self.date_of_departure, "%Y-%m-%d %H:%M:%S")
            else:
                date_obj = datetime.strptime(self.date_of_departure, "%Y-%m-%d")
        except ValueError:
            frappe.throw("Invalid Date Format for Date of Departure")


        month = date_obj.strftime("%m")
        year = date_obj.strftime("%Y")


        self.name = f"{self.airplane}-001-{month}-{year}-{self.get_new_sequence(date_obj)}"

    def get_new_sequence(self, date_obj):
        """Get the next sequence number for the given month and year"""
        first_day = date_obj.strftime("%Y-%m-01")
        last_day = date_obj.strftime("%Y-%m-31")

        last_flight = frappe.db.sql(
            """
            SELECT name FROM `tabAirplane Flight`
            WHERE airplane=%s AND date_of_departure BETWEEN %s AND %s
            ORDER BY creation DESC LIMIT 1
            """,
            (self.airplane, first_day, last_day),
            as_dict=True
        )

        if last_flight:
            last_name = last_flight[0]['name']
            last_seq = last_name.split("-")[-1]
            last_seq = int(last_seq) + 1 if last_seq.isdigit() else 1
        else:
            last_seq = 1

        return str(last_seq).zfill(5)

    def on_submit(self):
        """Set the status of the flight to 'Completed' after submission."""
        self.status = "Completed"
        self.db_update()  
        frappe.msgprint("Flight status has been set to Completed.", alert=True)
        
	
import frappe

def get_context(context):
    if frappe.form_dict.name:
        flight = frappe.get_doc("Airplane Flight", frappe.form_dict.name)
        context.flight = flight
    else:
        frappe.throw("Flight not found!")
