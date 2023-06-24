# Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LockerAssignment(Document):
	pass

def check_locker_assignment(doc, event):
	if frappe.db.exists("Locker Assignment", {"gym_member": doc.gym_member}):
		frappe.throw("This member already has a locker assigned.")

def new_locker_assignment(doc, event):
	frappe.db.set_value("Gym Locker", doc.gym_locker, "status", "Booked")
	return doc.gym_locker
