import frappe
# from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        self.calculate_total_amount()
        self.remove_duplicate_add_ons()

    def calculate_total_amount(self):
        """Calculates Total Amount = Flight Price + Sum of Add-on Amounts"""
        total_add_on_amount = sum([item.amount for item in self.get("add_ons")])
        self.total_amount = self.flight_price + total_add_on_amount

    def remove_duplicate_add_ons(self):
        """Ensures that no duplicate add-ons are added"""
        unique_items = {}
        cleaned_add_ons = []

        for item in self.get("add_ons"):
            if item.item not in unique_items:  # Use the correct field name 'item'
                unique_items[item.item] = True
                cleaned_add_ons.append(item)

        self.set("add_ons", cleaned_add_ons)
