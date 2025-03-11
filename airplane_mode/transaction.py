# transaction.py

# import frappe
# from airplane_mode.airportshop.doctype.shop.shop import Shop
# from airplane_mode.doctype.airport.airport import Airport

# def create_airport_shop_transition():
#     # Example dynamic transition logic: create an airport and dynamically link it to shops
#     # Airport creation
#     airport = frappe.get_doc({
#         'doctype': 'Airport',
#         'code': 'A001',  # Airport code
#         'city': 'Test City',
#         'country': 'Test Country'
#     })
#     airport.insert()

#     # Create shops linked to the airport
#     shop_data = [
#         {"shop_name": "Shop 1", "status": "Available"},
#         {"shop_name": "Shop 2", "status": "Occupied"},
#         {"shop_name": "Shop 3", "status": "Available"},
#         {"shop_name": "Shop 4", "status": "Occupied"}
#     ]

#     for data in shop_data:
#         shop = frappe.get_doc({
#             'doctype': 'Shop',
#             'shop_name': data["shop_name"],
#             'status': data["status"],
#             'airport': airport.name  # Linking the shop to the airport
#         })
#         shop.insert()

#     # Commit the transaction to save records
#     frappe.db.commit()

#     # Update the Airport's occupied and available shop counts
#     update_airport_shop_counts(airport)

#     return airport


# def update_airport_shop_counts(airport):
#     # Count occupied and available shops linked to the airport
#     occupied_count = frappe.db.count('Shop', filters={'airport': airport.name, 'status': 'Occupied'})
#     available_count = frappe.db.count('Shop', filters={'airport': airport.name, 'status': 'Available'})

#     # Update the airport document with these counts
#     airport.db_set('occupied_shops', occupied_count)
#     airport.db_set('int_lnxb', available_count)

#     # Commit the changes to the airport
#     frappe.db.commit()

#     print(f"Updated Airport: {airport.name} with {occupied_count} occupied shops and {available_count} available shops.")


# if __name__ == "__main__":
#     airport = create_airport_shop_transition()
#     print(f"Airport {airport.name} created and shops linked.")
