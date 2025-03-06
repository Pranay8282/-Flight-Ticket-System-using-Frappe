// Copyright (c) 2025, Sanskar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airport", {
	refresh(frm) {
        if(!frappe.user.has_role("Airport Authority Personnel")){
            frm.set_df_property("initial_audit_completed","hidden",1)
        }else{
            frm.set_df_property("initial_audit_completed","hidden",0)
        }
	},
});
