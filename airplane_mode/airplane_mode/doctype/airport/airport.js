// Copyright (c) 2025, Sanskar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airport', {
    refresh: function(frm) {
        frappe.call({
            method: 'airplane_mode.airplane_mode.airplane_mode.get_shop_counts',
            args: {
                airport_code: frm.doc.code
            },
            callback: function(r) {
                if (r.message) {
                    frm.set_value('int_lnxb', r.message.available);
                    frm.set_value('occupied_shops', r.message.occupied);
                    frm.refresh_fields(['int_lnxb', 'occupied_shops']);
                }
            }
        });
    }
});