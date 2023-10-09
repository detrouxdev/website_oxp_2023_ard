# -*- coding: utf-8 -*-
from odoo import http


class Oxp2023(http.Controller):
    @http.route('/oxp_20223/weather_long_lat', type='json')
    def get_long_lat(self, **kw):
        # Data based on API call to OpenStreeMap
        return {
            "display_name": "Pl. de Belgique 1, 1020 Bruxelles",
            "lon": 50.8996474,
            "lat": 4.3351507
        }
    @http.route('/oxp_2023/get_weather', type='json')
    def get_weather(self):
        # Data based on API call to Open-Meteo.com
        return {
            "daily": {
                "time": [
                    "2023-11-03",
                    "2023-11-04",
                    "2023-11-05",
                    "2023-11-06",
                    "2023-11-07",
                    "2023-11-08",
                    "2023-11-09"
                ],
                "temperature_2m_max": [
                    11.2,
                    11.3,
                    11.6,
                    11.9,
                    10.0,
                    11.0,
                    9.6
                ],
                "weathercode": [
                    80,
                    80,
                    80,
                    3,
                    61,
                    3,
                    61
                ]
            }
        }
