import frappe
from frappe.website.website_generator import WebsiteGenerator

class Shop(WebsiteGenerator):
    def before_save(self):
        """This method will be triggered before saving the Shop document."""
        self.check_airport_link()

    def after_save(self):
        """This method will be triggered after saving the Shop document."""
        self.after_save_action()

    def check_airport_link(self):
        """Ensure the airport field is valid before saving."""
        if not self.airport:
            frappe.throw(_("Airport link is required for the Shop."))

    def after_save_action(self):
        """Custom logic after saving the Shop."""
        # Print a message to confirm the Shop was saved
        frappe.msgprint(f'Shop "{self.shop_name}" has been saved successfully!')

        # Perform custom actions after save
        self.update_airport_status()

    def update_airport_status(self):
        """Update the status of the linked Airport."""
        if self.airport:
            try:
                airport = frappe.get_doc("airport_mode.Airport", self.airport)
                if airport:
                    if self.status == "Active":
                        airport.int_lnxb += 1  # Increase some field (custom logic)
                        airport.save()
                        frappe.msgprint(f'Airport status for {airport.name} updated to Active.')
                    else:
                        airport.occupied_shops += 1  # Increase the number of occupied shops
                        airport.save()
                        frappe.msgprint(f'Airport {airport.name} now has {airport.occupied_shops} occupied shops.')
                else:
                    frappe.throw(_("Airport not found."))  # Ensuring the airport exists
            except frappe.DoesNotExistError:
                frappe.throw(_("Invalid Airport linked to this Shop."))

        # No need for explicit commit; Frappe handles it automatically during the save lifecycle
