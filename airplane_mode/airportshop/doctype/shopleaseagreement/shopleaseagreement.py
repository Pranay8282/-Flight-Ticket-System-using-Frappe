# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class ShopLeaseAgreement(Document):
    def before_insert(self):
        self.contract_number = generate_contract_number()

def generate_contract_number():
    # Fetch the last contract document
    last_contract = frappe.get_all(
        'ShopLeaseAgreement', 
        fields=["contract_number"], 
        limit_page_length=1, 
        order_by="contract_number desc"
    )
    
    # If no contracts exist, start from 1000 (or any desired number)
    if not last_contract:
        return 'C1000'
    
    # Extract the last contract number and increment it
    last_contract_number = last_contract[0].contract_number
    last_number = int(last_contract_number[1:])  # Assuming 'C' is used as a prefix
    
    # Increment the number
    new_number = last_number + 1
    
    # Return the new contract number with the prefix 'C'
    return f'C{new_number}'
