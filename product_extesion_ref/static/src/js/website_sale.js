/** @odoo-module **/

import { WebsiteSale } from '@website_sale/js/website_sale';

WebsiteSale.include({
    /**
     * @private
     * @param {Event} ev
     */
    _onSubmitSaleSearch: function (ev) {
        if (!this.$('.dropdown_sorty_by').length) {
            return;
        }
        var $this = $(ev.currentTarget);
        if (!ev.defaultPrevented && !$this.is(".disabled")) {
            ev.preventDefault();
            var oldurl = $this.attr('action');
            oldurl += (oldurl.indexOf("?")===-1) ? "?" : "";
            if ($this.find('[name=noFuzzy]').val() === "true") {
                oldurl += '&noFuzzy=true';
            }
            var search = $this.find('input.search-query');

            var brand = $this.find('input.search-brand');
            var year = $this.find('input.search-year');
            var model = $this.find('input.search-model');
            var piece = $this.find('input.search-piece');

            var originalURL = oldurl + '&' + search.attr('name') + '=' + encodeURIComponent(search.val())
            var brandQuery = '&' + brand.attr('name') + '=' + encodeURIComponent(brand.val())
            var yearQuery = '&' + year.attr('name') + '=' + encodeURIComponent(year.val())
            var modelQuery = '&' + model.attr('name') + '=' + encodeURIComponent(model.val())
            var pieceQuery = '&' + piece.attr('name') + '=' + encodeURIComponent(piece.val())

            window.location = oldurl + '&' + search.attr('name') + '=' + encodeURIComponent(search.val());
        }
    },
});