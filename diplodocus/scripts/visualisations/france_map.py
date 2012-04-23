#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kartograph


opts = {
    "proj": {
        "id": "sattelite",
        "lon0": 3.0,
        "lat0": 48.0,
        },
    "bounds": {
        "mode": "bbox",
        "data": [-100, 30, -60, 60]
        },
    "layers": [{
        "src": "shp/ne_50m_admin_0_countries.shp",
        }],
    "export": {
        "width": 800,
        "height": "auto",
        },
    }


k = kartograph.Kartograph()
k.generate(opts, outfile='map.svg')
