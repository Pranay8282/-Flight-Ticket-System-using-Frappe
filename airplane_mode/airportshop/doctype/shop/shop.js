// Copyright (c) 2025, Sanskar and contributors
// For license information, please see license.txt
frappe.ui.form.on('Shop', {
    shop_type: function(frm) {
        console.log(frm.fields_dict['shop_type']);
        frm.fields_dict['shop_type'].get_query = function(doc) {
            return {
                filters: {
                    'enable': 1 // Only show enabled Shop Types
                }
            };
        };
    }
});
