frappe.listview_settings['Airplane Flight'] = {
    add_fields: ["airplane", "source", "destination", "date_of_departure", "time_of_departure", "duration"],
    get_indicator: function(doc) {
        return [__("Flight"), "blue", "status,=,Active"];
    },
    formatters: {
        airplane: function(value, doc) {
            return `<strong>${doc.airplane}</strong>`;
        },
        source: function(value, doc) {
            return `<span>${doc.source} → ${doc.destination}</span>`;
        },
        date_of_departure: function(value, doc) {
            return `<span>${frappe.datetime.str_to_user(value)} | ${doc.time_of_departure} | ${doc.duration} min</span>`;
        }
    },
    onload: function(listview) {
        console.log("Custom List View Loaded for Airplane Flight");
    }
};
