import frappe

def get_context(context):
    flight_name = frappe.form_dict.name  # Get the flight name from URL
    if flight_name:
        flight = frappe.get_doc("Airplane Flight", flight_name)
        context.flight = flight  # Pass flight object to template
    else:
        frappe.throw("Flight not found!")
