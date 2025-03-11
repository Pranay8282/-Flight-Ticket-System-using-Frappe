// Copyright (c) 2025, Sanskar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Rent Payment', {
    // Trigger when the payment method changes
    payment_method: function(frm) {
        // Check if the selected payment method is Cash
        if (frm.doc.payment_method === 'Cash') {
            frm.fields_dict['reciept'].toggle(false); // Hide the receipt field
        } else {
            frm.fields_dict['reciept'].toggle(true); // Show the receipt field
        }
    },
    // Trigger form load to apply visibility logic on page load
    onload: function(frm) {
        if (frm.doc.payment_method === 'Cash') {
            frm.fields_dict['reciept'].toggle(false); // Hide the receipt field if payment method is cash
        } else {
            frm.fields_dict['reciept'].toggle(true); // Show the receipt field
        }
    }
});
