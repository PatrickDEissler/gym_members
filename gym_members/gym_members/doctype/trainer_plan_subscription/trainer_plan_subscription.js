// Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
// For license information, please see license.txt

frappe.ui.form.on("Trainer Plan Subscription", {
	refresh(frm) {
        // custom button that opens a quick dialog to enter a date. This date will then be fetched into the field "end"
        frm.add_custom_button(__('End Subscription'), () => {
            // existing date field "end" will be overwritten and form will be saved
            frappe.prompt([
                {
                    fieldname: 'end',
                    label: 'End',
                    fieldtype: 'Date',
                    reqd: 1,
                    default: frappe.datetime.add_months(frm.doc.end, 1)
                }
            ], (values) => {
                frappe.model.set_value(frm.doctype, frm.docname, 'end', values.end)
                frm.save()
            }
            )
        })
	},
    // This custom script will prevent members creating ratings within the first 7 days of their subscription
    start(frm) {
        frm.toggle_display('rating', frappe.datetime.get_day_diff(frappe.datetime.nowdate(), frm.doc.start) >= 7)
    }
});


// Custom buttons
