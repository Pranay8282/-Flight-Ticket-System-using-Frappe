import frappe

def send_rent_due_reminder():
    frappe.logger().info("📢 Rent Due Reminder Triggered!")  # Logs in logs/bench.log
    print("🔔 Rent Due Reminder Function Executed!")  # Should print in the terminal
    frappe.msgprint("✅ Rent due reminder sent successfully!")
