import frappe
from frappe.model.document import Document

class Airplane(Document):
    def autoname(self):

        airline_name = self.airline
        

        last_airplane = frappe.db.sql(
            """SELECT name FROM `tabAirplane` 
            WHERE airline=%s ORDER BY creation DESC LIMIT 1""",
            (airline_name),
            as_dict=True
        )


        if last_airplane:
            last_name = last_airplane[0]["name"]
            last_number = int(last_name.split("-")[-1])  
            new_number = last_number + 1
        else:
            new_number = 1  


        self.name = f"{airline_name}-{new_number:03d}"
