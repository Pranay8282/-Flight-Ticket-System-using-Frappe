# Copyright (c) 2025, Sanskar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Airplane(Document):
	def validate(self):
		if self.capacity and self.capacity < 0:
			frappe.throw("Capacity cannot be negative.")
