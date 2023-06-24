# Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMember(Document):
	pass

def full_name(doc, event):
	doc.full_name = f"{doc.first_name} {doc.last_name}"
	return doc.full_name

def create_customer(doc, event):
	# create a new customer
	customer = frappe.new_doc("Customer")
	customer.customer_name = doc.full_name
	customer.customer_type = "Individual"
	customer.customer_group = "All Customer Groups"
	customer.territory = "All Territories"
	customer.insert()
	doc.customer = customer.name
	doc.save()
	return customer