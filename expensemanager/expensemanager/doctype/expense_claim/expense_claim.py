# Copyright (c) 2024, AKshata and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):
	def before_save(self):
		total_amt = 0
		for amt in self.expense_type:
			total_amt += amt.amount
		self.total_amount = total_amt
