// Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
// For license information, please see license.txt

frappe.ui.form.on("Class Booking", {
	refresh(frm) {
        frm.set_query("booked_class", function () {
            return {
                filters: {
                    status: "Available",
                },
            };
        },);
	},
});
