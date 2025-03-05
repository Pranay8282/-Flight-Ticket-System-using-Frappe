# Example: Check if the condition is met for the notification
from frappe.utils import nowdate, add_days

flight = frappe.get_doc("Airplane Flight", "YOUR_FLIGHT_NAME")
condition = flight.status == "Scheduled" and flight.date_of_departure == add_days(nowdate(), 1)
print(condition)  # Check if it returns True
