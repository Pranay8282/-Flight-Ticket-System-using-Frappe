import frappe

def execute(filters=None):
    columns, data = [
        {
            "label": "Name",
            "fieldname": "name",
            "fieldtype": "Link",
            "options": "Airplane Flight Ticket",
            "width": 150
        },
    ], [
        {
            "name": "T001"
        },
        {
            "name": "T002"
        },
        {
            "name": "T003"
        },
        {
            "name": "T004"
        },
        {
            "name": "T005"
        }
    ]
    return columns, data
