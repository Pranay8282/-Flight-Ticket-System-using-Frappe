frappe.ready(function() {
    // Get flight ID from URL
    let flight_id = frappe.utils.get_url_arg("flight");

    if (flight_id) {
        // Fetch flight details
        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "Airplane Flight",
                name: flight_id
            },
            callback: function(response) {
                if (response.message) {
                    let flight = response.message;
                    
                    // Auto-fill Flight and Price
                    $('[data-fieldname="flight"]').val(flight.name).trigger("change");
                    $('[data-fieldname="flight_price"]').val(flight.price).trigger("change");
                }
            }
        });
    }
});
	