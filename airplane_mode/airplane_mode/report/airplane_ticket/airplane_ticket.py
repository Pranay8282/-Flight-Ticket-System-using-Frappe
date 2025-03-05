import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {
            "fieldname": "airline",
            "label": _("Airline"),
            "fieldtype": "Link",
            "options": "Airplane Flight",
            "width": 150
        },
        {
            "fieldname": "revenue",
            "label": _("Revenue"),
            "fieldtype": "Currency",
            "width": 150
        }
    ]
    
    # Apply filters if any (for example, filter by date, status, etc.)
    filter_conditions = {}
    if filters.get('start_date') and filters.get('end_date'):
        filter_conditions.update({
            'departure_date': ['between', [filters['start_date'], filters['end_date']]]
        })
    
    if filters.get('status'):
        filter_conditions.update({
            'status': filters['status']
        })

    # Fetch total revenue based on filters
    total_revenue = frappe.db.get_value('Airplane Ticket', filter_conditions, 'sum(total_amount)')
    
    # Use query builder to get all airlines and their total revenue
    revenue_data = frappe.get_all(
    'Airplane Ticket',
    fields=['flight', 'sum(total_amount) as revenue'],
    filters=filter_conditions,
    group_by='flight',
    as_dict=1  # Use 1 instead of as_dict=True
)

    
    result = []
    for row in revenue_data:
        airline = frappe.get_value('Airplane Flight', row['flight'], 'airline')  # Assuming 'airline' field in Airplane Flight
        result.append({
            'airline': airline,
            'revenue': row['revenue']
        })
    
    # Include airlines with 0 revenue
    airlines_with_0_revenue = frappe.get_all('Airplane Flight', filters={'airline': ('!=', None)}, as_dict=True)
    for airline in airlines_with_0_revenue:
        if airline['airline'] not in [row['airline'] for row in result]:
            result.append({
                'airline': airline['airline'],
                'revenue': 0
            })
    
    # Add total row at the end
    result.append({
        'airline': _('Total Revenue'),
        'revenue': total_revenue
    })
    
    # Donut chart data
    chart_data = [{
        'name': row['airline'],
        'value': row['revenue']
    } for row in result if row['revenue'] > 0]
    
    chart = {
        'type': 'donut',
        'data': chart_data
    }
    
    return columns, result, chart
