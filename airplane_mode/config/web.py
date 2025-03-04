from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
    def get_context(self, context):
        context.no_cache = 1
