# Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ClassBooking(Document):
    pass

def validate_booking(doc, event):
    booked_class = frappe.get_doc("Gym Class", doc.booked_class)
    if booked_class.status == "Full":
        frappe.throw("This class is already full. Please choose another one.")
    if booked_class.status == "Over":
        frappe.throw("This class is already over. Please choose another one.")
    existing_bookings = frappe.get_all("Class Booking", 
                    filters={"booked_class": doc.booked_class, "gym_member": doc.gym_member, "docstatus": ("!=", 2), "date": doc.date})
    if len(existing_bookings) > 1:
        frappe.throw("You already booked this class.")

def add_new_participant(doc, event):
    booked_class = frappe.get_doc("Gym Class", doc.booked_class)

    if (booked_class.capacity - booked_class.booked_participants) == 1:
        booked_class.status = "Full"

    booked_class.booked_participants += 1
    booked_class.save()

def remove_participant(doc, event):
    booked_class = frappe.get_doc("Gym Class", doc.booked_class)
    booked_class.booked_participants -= 1
    booked_class.status = "Available"
    booked_class.save()

def create_summaries():
    bookings = frappe.get_all(
        "Class Booking",
        fields=["gym_member", "date", "booked_class"],
        filters={
            "docstatus": 1,
            "date": ["<=", frappe.utils.today(), ">=", frappe.utils.add_days(frappe.utils.today(), -6)]
        }
    )

    booking_members = list(set([data["gym_member"] for data in bookings]))

    for m in booking_members:
        summary = frappe.new_doc("Booking Summary")
        
        notification_content = r"Hi {{ doc.first_name }},"
        notification_content += "\n\nhere is your booking summary for the last 7 days:\n"
        notification_content += "<table>\n"
        notification_content += "   <tr><th>Date</th><th>Class</th></tr>\n"
        for b in bookings:
            if b["gym_member"] == m:
                notification_content += f"  <tr><td>{b.date}</td><td>{b.booked_class}</td></tr>\n"
        notification_content += "</table>"
        notification_content += "\n\nHave a good start into the new week,\nYour Team at Red Corner Gym"
 
        summary.notification = notification_content
        summary.gym_member = m
        summary.email = frappe.get_value("Gym Member", m, "custom_user")
        summary.insert()

