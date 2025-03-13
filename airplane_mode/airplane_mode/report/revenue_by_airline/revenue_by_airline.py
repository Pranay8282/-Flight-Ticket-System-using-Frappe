import frappe

def execute(filters=None):
    # Define columns to be displayed in the report
    columns = [
        {"fieldname": "airport", "label": "Airport", "fieldtype": "Data", "width": 150},
        {"fieldname": "date", "label": "Date", "fieldtype": "Date", "width": 120},
        {"fieldname": "total_revenue", "label": "Total Revenue", "fieldtype": "Float", "width": 150}
    ]

    filters = filters or {}

    conditions = []
    values = {}

    # Apply filter for airport
    if filters.get("airport"):
        conditions.append("airport = %(airport)s")
        values["airport"] = filters["airport"]

    # Apply date range filter
    if filters.get("from_date") and filters.get("to_date"):
        conditions.append("departure_date BETWEEN %(from_date)s AND %(to_date)s")
        values["from_date"] = filters["from_date"]
        values["to_date"] = filters["to_date"]

    where_clause = " AND ".join(conditions) if conditions else "1=1"

    # Fetch the revenue data from the Airplane Ticket Doctype (or relevant table)
    data = frappe.db.sql(f"""
        SELECT airport, departure_date as date, SUM(flight_price) as total_revenue
        FROM `tabAirplane Ticket`
        WHERE {where_clause}
        GROUP BY airport, departure_date
        ORDER BY departure_date DESC
    """, values, as_dict=True)

    # Prepare data for chart
    airports = list(set(row["airport"] for row in data))
    dates = list(set(row["date"] for row in data))

    datasets = []
    for date in dates:
        dataset_values = [next((row["total_revenue"] for row in data if row["airport"] == airport and row["date"] == date), 0) for airport in airports]
        datasets.append({"name": str(date), "values": dataset_values})

    # Create the chart
    chart = {
        "data": {
            "labels": airports,
            "datasets": datasets   
        },
        "type": "bar"  # You can use 'pie' or 'line' as well depending on the visualization you prefer
    }

    # Return columns, data, and chart
    return columns, data, None, chart
