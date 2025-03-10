// Copyright (c) 2025, Sanskar and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {

    source_airport:function(frm){
        frappe.db.get_value("Airport",frm.doc.source_airport,"code",function(r){
            if(r && r.code){
                frm.set_value("source_airport_code",r.code);
            }
        });
    },

    destination_airport:function(frm){
        frappe.db.get_value("Airport",frm.doc.destination_airport,"code",function(r){
            if(r && r.code){
                frm.set_value("destination_airport_code",r.code);
            }
        });
    }

});


frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        if (!frm.doc.__islocal) {  // Only show button for saved records
            frm.add_custom_button(__('Assign Seat'), function() {
                frappe.prompt([
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ], (values) => {
                    frm.set_value('seat', values.seat_number);
                    frm.save();
                }, __('Assign Seat'), __('Assign'));
            });
        }
    }
});


