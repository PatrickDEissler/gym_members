# Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class GymClass(Document):
	pass

def set_status_to_over():
	for doc in frappe.get_all("Gym Class", filters={"date": ("<", datetime.now().date()), "status": ("!=", "Over")}):
		doc.status = "Over"
		doc.save()
