import frappe
from frappe.desk.query_report import get_chart

def execute(filters=None):
    filters = filters or {}

    # Initialize dictionary to store revenue by airline prefix
    revenue_by_airline_prefix = {}

    try:
        # Query to get relevant ticket data (only necessary fields)
        tickets = frappe.get_all('Airplane Ticket', fields=['flight', 'total_amount'], filters=filters)

        # If no tickets are found, return an empty result
        if not tickets:
            return {
                "columns": [],
                "rows": [],
                "chart": None
            }

        # Process the ticket data
        for ticket in tickets:
            # Ensure that 'flight' is not empty or None
            if ticket.get('flight'):
                # Extract airline prefix (before the first hyphen '-')
                airline_prefix = ticket['flight'].split('-')[0] if '-' in ticket['flight'] else ticket['flight']
                
                # Ensure 'total_amount' is a valid number
                revenue = ticket.get('total_amount') or 0  # Default to 0 if total_amount is missing or None
                
                # Add revenue to the corresponding airline prefix
                if airline_prefix not in revenue_by_airline_prefix:
                    revenue_by_airline_prefix[airline_prefix] = 0
                revenue_by_airline_prefix[airline_prefix] += revenue
            else:
                # Handle case where 'flight' is missing or invalid
                frappe.log_error(f"Invalid or missing flight data for ticket: {ticket}")

        # Prepare columns for the report
        columns = [
            {"label": "Airline", "fieldname": "airline", "fieldtype": "Data", "width": 300},
            {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 200}
        ]

        # Prepare rows for the report
        rows = [[airline_prefix, revenue] for airline_prefix, revenue in revenue_by_airline_prefix.items()]

        # Add a total row for revenue
        total_revenue = sum(revenue_by_airline_prefix.values())
        rows.append(['Total', total_revenue])

        # Prepare chart data (Pie chart)
        chart_data = {
            'labels': list(revenue_by_airline_prefix.keys()),  # Airline prefixes
            'datasets': [{
                'name': 'Revenue',
                'values': list(revenue_by_airline_prefix.values())  # Corresponding revenue values
            }]
        }

        # Debugging: Log the chart data to ensure it's being structured correctly
        print("Chart Data:", chart_data)

        # Create the chart using get_chart (using Pie chart type, based on your second example)
        chart = get_chart(
            chart_type="pie",  # Pie chart type
            chart_data=chart_data,  # Data for the chart
            height=250,  # Height of the chart
            title="Revenue by Airline"  # Title of the chart
        )

        # Debugging: Ensure chart is generated and check the result
        print("Generated Chart:", chart)

        # Return the columns, rows, and chart data
        return {
            "columns": columns,
            "rows": rows,
            "chart": chart
        }

    except Exception as e:
        # Log any unexpected errors and return a failure response
        frappe.log_error(f"Error executing report: {str(e)}")
        return {
            "columns": [],
            "rows": [],
            "chart": None
        }
