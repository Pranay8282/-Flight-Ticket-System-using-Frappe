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
    },

    refresh: function(frm) {
        // Run this on initial load
        toggle_tenant_field(frm);
    },
    
    status: function(frm) {
        // Run this whenever the Status field changes
        toggle_tenant_field(frm);
    }
});


function toggle_tenant_field(frm) {
    // Get the current status value
    const status = frm.doc.status;
    
    if (status === 'Occupied') {
        // Show and make Tenant mandatory
        frm.set_df_property('tenant', 'hidden', 0);
        frm.set_df_property('tenant', 'reqd', 1);
    } else {
        // Hide and make Tenant not mandatory
        frm.set_df_property('tenant', 'hidden', 1);
        frm.set_df_property('tenant', 'reqd', 0);
        
        // Clear the tenant field if it has a value
        if (frm.doc.tenant) {
            frm.set_value('tenant', '');
        }
    }
    
    // Refresh the field to apply changes
    frm.refresh_field('tenant');
}