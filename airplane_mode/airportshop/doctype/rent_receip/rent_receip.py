# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_datetime

class RentReceip(Document):
    
    def before_insert(self):
        # Generate receipt number before the document is inserted
        self.receipt_number = self.generate_receipt_number()

    def generate_receipt_number(self):
        # Get the current year in YYYY format
        current_year = get_datetime().strftime('%Y')
        
        # Define the prefix for the receipt number
        prefix = "RCP-" + current_year
        
        # Fetch the last receipt number for the current year
        last_receipt = frappe.get_all('Rent Receip', filters={'receipt_number': ['like', f'{prefix}%']}, 
                                      fields=['receipt_number'], order_by='receipt_number desc', limit=1)
        
        # If there is a last receipt number, extract the number and increment it
        if last_receipt:
            last_number = int(last_receipt[0]['receipt_number'].split('-')[-1])  # Extract the last number
            new_number = last_number + 1
        else:
            # If no receipts found for the current year, start from 1
            new_number = 1
        
        # Format the new receipt number with leading zeros to a fixed length
        receipt_number = f"{prefix}-{str(new_number).zfill(5)}"
        
        return receipt_number
