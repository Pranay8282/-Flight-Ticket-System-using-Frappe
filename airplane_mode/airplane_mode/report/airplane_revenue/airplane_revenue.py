import frappe

def execute(filters=None):
    filters = filters or {}

 
    tickets = frappe.get_all('Airplane Ticket', fields=['flight', 'total_amount'], filters=filters)
    
    print(tickets)


    revenue_by_airline_prefix = {}

    for ticket in tickets:

        airline_prefix = ticket['flight'].split('-')[0]
        revenue = ticket['total_amount']
        

        print(f"Airline Prefix: {airline_prefix}, Revenue: {revenue}")

        if airline_prefix not in revenue_by_airline_prefix:
            revenue_by_airline_prefix[airline_prefix] = 0
        
        revenue_by_airline_prefix[airline_prefix] += revenue
    

    columns = [
        {"label": "Airline", "fieldname": "airline", "fieldtype": "Data", "width": 300},
        {"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 200}
    ]


    rows = []
    for airline_prefix, revenue in revenue_by_airline_prefix.items():
        rows.append({"airline": airline_prefix, "revenue": revenue})


    total_revenue = sum(revenue_by_airline_prefix.values())
    rows.append({"airline": "Total", "revenue": total_revenue})


    chart_data = {
        'labels': list(revenue_by_airline_prefix.keys()),  
        'datasets': [{
            'name': 'Revenue',
            'values': list(revenue_by_airline_prefix.values())  
        }]
    }

    chart = {
        'type': 'donut',
        'data': chart_data,
        'height': 250,
        'title': 'Revenue by Airline'
    }


    return {
        "columns": columns,
        "rows": rows,
        "chart": chart
    }
