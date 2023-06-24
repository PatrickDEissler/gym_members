# Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TrainerPlanSubscription(Document):
	pass

def disallow_early_ratings(doc, event):
	# if the doc.start is less than 7 days ago
	if doc.start < frappe.utils.add_days(frappe.utils.nowdate(), 7):
		frappe.throw("You can only rate a trainer after 7 days of starting a plan.")

def check_existing_subscription(doc, event):
	if frappe.db.exists("Trainer Plan Subscription", {"gym_member": doc.gym_member}):
		frappe.throw("This member already has a subscription.")

def new_rating(doc, event):
	# create a new Trainer Rating document
	trainer_rating = frappe.new_doc("Trainer Rating")
	trainer_rating.trainer_plan_subscription = doc.name
	trainer_rating.rating = doc.rating
	trainer_rating.date = frappe.utils.nowdate()
	trainer_rating.insert()
	return trainer_rating.name

	# if frappe.db.exists("Trainer Rating", {"trainer_plan_subscription": doc.name}):
	# 	frappe.set_value("Trainer Rating", {"trainer_plan_subscription": doc.name}, "rating", doc.rating)
	# 	frappe.set_value("Trainer Rating", {"trainer_plan_subscription": doc.name}, "date", doc.date)
	# else:
	# 	trainer_rating = frappe.new_doc("Trainer Rating")
	# 	trainer_rating.trainer_plan_subscription = doc.name
	# 	trainer_rating.rating = doc.rating
	# 	trainer_rating.date = frappe.utils.nowdate()
	# 	trainer_rating.insert()