// Copyright (c) 2023, Patrick Eissler (ALYF GmbH) and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Locker Assignment", {
// 	refresh(frm) {

// 	},
// });s

frappe.ui.form.on('Locker Assignment', {
    refresh(frm) {
        frm.set_query('gym_locker', () => {
            return {
                filters: {
                    status: 'Free'
                }
            }
        })
    }
})