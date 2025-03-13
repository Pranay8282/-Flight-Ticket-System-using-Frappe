import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "source_airport_code", "label": "Source Airport Code", "fieldtype": "Data", "width": 150},
        {"fieldname": "total_revenue", "label": "Total Revenue", "fieldtype": "Currency", "width": 150},
    ]
    
    filters = filters or {}

    # SQL query to sum the flight prices per source_airport_code
    data = frappe.db.sql("""
        SELECT source_airport_code, SUM(flight_price) as total_revenue
        FROM `tabAirplane Ticket`
        GROUP BY source_airport_code
        HAVING SUM(flight_price) > 0  # Ensure no rows with zero total revenue
        ORDER BY source_airport_code
    """, as_dict=True)

    # Prepare data for the chart (donut chart)
    labels = [row["source_airport_code"] for row in data]
    revenue_values = [row["total_revenue"] for row in data]
    
    chart = {
        "data": {
            "labels": labels,
            "datasets": [{"name": "Revenue", "values": revenue_values}]
        },
        "type": "donut"  # Donut chart type
    }

    return columns, data, None, chart
	