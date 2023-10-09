/** @odoo-module **/

import { renderToElement } from "@web/core/utils/render";
import { formatDate, parseDate } from "@web/core/l10n/dates"
import publicWidget from "@web/legacy/js/public/public_widget";

const WeatherSnippet = publicWidget.Widget.extend({
    selector: ".s_weather",
    disabledInEditableMode: false,
    init() {
        this._super(...arguments);
        this.rpc = this.bindService("rpc");
    },
    /**
     * @override
     */
    async willStart() {
        await this._super(...arguments);
        const longitude = this.$target[0].dataset.longitude;
        const latitude = this.$target[0].dataset.latitude;
        if (longitude === undefined && latitude === undefined) {
            this.days = [];
            return;
        }
        this.weatherData = await this.rpc("/oxp_2023/get_weather");
        this.days = this.weatherData.daily.temperature_2m_max.map((temperature, index) => {
            const weathercode = this.weatherData.daily.weathercode[index];
            let img = "rain";
            if (weathercode === 0) {
                img = "sun";
            } else if (weathercode < 3) {
                img = "sun_clouds";
            } else if (weathercode <= 20) {
                img = "clouds";
            } else {
                img = "rain";
            }
            return {
                date: formatDate(parseDate(this.weatherData.daily.time[index]), { format: "EEEE d MMM" }),
                temp: temperature,
                img,
            };
        }).splice(0, 5);
    },
    async start() {
        this.weatherElement = renderToElement("oxp_2023.s_weather", { widget: this });
        const daysContainer = this.$target[0].querySelector(".days_container");
        if (this.editableMode && this.days.length === 0) {
            this.weatherElement.querySelector(".missing_option_warning").classList.remove("d-none");
        }
        daysContainer.append(this.weatherElement);
    },
    destroy() {
        this.weatherElement.remove();
    }
});

publicWidget.registry.s_weather = WeatherSnippet;
