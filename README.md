# WHO GIS API

Small repository showing how to use the WHO GIS APIn via ArcGIS REST.
This uses Python but should be easily translated in any other language.

## How to test

```bash
pip install -r requirements.txt
python who_gis_api.py
```

## Methods

Two methods are demonstrated:

- One to get a list of features based on a where clause
- One to get the feature surrounding a given GPS point given its coordinates

The second one could allow data collected at a much lower level to be "attached" to one of the three standard level - assuming GPS coordinates are available, it could be as simple as "give me the feature that contains this point".