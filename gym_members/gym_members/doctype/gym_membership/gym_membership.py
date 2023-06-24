# Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymMembership(Document):
	pass

def check_existing_membership(doc, event):
	if frappe.db.exists("Gym Membership", {"gym_member": doc.gym_member}):
		frappe.throw("This member already has a membership.")