import kartograph

opts = {
    "proj": {
        "id": "satellite",
        "lon0": 0,
        "lat0": 47.50,
        "dist": 1.035,
        "up": 0,
        "tilt": 0
        },
    "bounds": {
        "padding": 0.02,
        },
    "layers": [
        {
          "special": "sea",
          "styles": {
            "fill": "lightblue"
          }
        },
        {
          "special": "graticule",
          "latitudes": 10,
          "longitudes": 10,
          "styles": {
            "stroke-width": "0.4px"
          }
        },
        {
            "id": "country",
            "src": "shp/10m_cultural/ne_10m_admin_0_countries.shp",
        },
        {
            "id": "regions",
            "src": "shp/10m_cultural/ne_10m_admin_1_states_provinces_shp.shp",
            "filter": ["ISO", "is", "FRA"],
        },
    ],
    "export": {
        "width": 768,
        "height": "auto",
        },
    }

k = kartograph.Kartograph()
k.generate(opts, outfile='map.svg')
