import frappe
from frappe import _


def after_install():
    create_notification_document()

def create_notification_document():
    doc_info = {
        "name": "Weekly Class Summary for Members",
        "enabled": 1,
        "channel": "Email",
        "subject": "Well done! You were active this week :)",
        "document_type": "Booking Summary",
        "event": "New",
        "sender": "_Test Email Account 1",
        "message": r"{{ doc.notification }}",
        "doctype": "Notification",
        "recipients": [
            {
                "receiver_by_document_field": "email",
                "parent": "Weekly Class Summary for Members",
                "parentfield": "recipients",
                "parenttype": "Notification",
                "doctype": "Notification Recipient",
            }
        ],
    }
    new_doc = frappe.new_doc("Notification")
    new_doc.update(doc_info)
    new_doc.insert()
