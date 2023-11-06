# import frappe


# def execute():
# 	PayrollEntry = frappe.qb.DocType("Payroll Entry")

# 	status = (
# 		frappe.qb.terms.Case()
# 		.when(PayrollEntry.docstatus == 0, "Draft")
# 		.when(PayrollEntry.docstatus == 1, "Submitted")
# 		.else_("Cancelled")
# 	)

# 	(frappe.qb.update(PayrollEntry).set("status", status).where(PayrollEntry.status.isnull())).run()

import frappe


def execute():
	all_customers = frappe.get_all("Customer", fields=["customer_name"])

	split_customers = [customer['customer_name'].split(" ") for customer in all_customers]

	for c in split_customers:
		new_member = frappe.new_doc("Gym Member")
		new_member.first_name = c[0]
		new_member.last_name = c[1] if len(c) > 1 else ""
		new_member.save()
	
	# change the customer_group_name of the Customer Group "Individual" to "Gym Member"
