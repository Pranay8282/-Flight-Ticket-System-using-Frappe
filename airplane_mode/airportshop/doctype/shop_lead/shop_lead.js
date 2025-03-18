// Copyright (c) 2025, Sanskar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Lead", {
    refresh: function(frm) {
        frm.set_query('shop', function() {
            return {
                filters: {
                    'status': 'Available'
                }
            };
        });
    },


    shop: function(frm) {
        if(frm.doc.shop) {
            // When a shop is selected, show a message
            frappe.msgprint(`Shop ${frm.doc.shop} selected. Save the document to allocate this shop.`);
            
            // If you want to automatically set the status to "Shop Allocated"
            // Uncomment the following lines:
            // frm.set_value('status', 'Shop Allocated');
            // frm.save();
        }
    }
});
