frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {

            $('.custom-website-link').remove();
            

            let website_link = $(`<a class="custom-website-link"
                href="${frm.doc.website}"
                target="_blank"
                style="display:block; margin-bottom:10px; font-weight:bold;">
                Visit Website
            </a>`);

            website_link.prependTo(frm.page.sidebar.find('.form-assignments'));
        }
    }
});
