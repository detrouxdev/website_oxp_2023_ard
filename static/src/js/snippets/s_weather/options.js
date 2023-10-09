/** @odoo-module **/

import options from "@web_editor/js/editor/snippets.options";

options.registry.Weather = options.Class.extend({
    /**
     * @override
     */
    init() {
        this.rpc = this.bindService("rpc");
        return this._super(...arguments);
    },
    /**
     * @see options.Class.selectClass for parameters
     */
    async selectAddress(previewMode, widgetValue, params) {
        const location = await this.rpc("/oxp_20223/weather_long_lat", { locationName: widgetValue });
        this.$target[0].dataset.locationName = location.display_name;
        this.$target[0].dataset.longitude = location.lon;
        this.$target[0].dataset.latitude = location.lat;
    },
    /**
     * @override
     */
    _computeWidgetState(methodName) {
        if (methodName === "selectAddress") {
            return this.$target[0].dataset.locationName;
        }
        return this._super(...arguments);
    }
});
