import requests
from pprint import pprint 
BASE_ADM0_URL = "https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Detailed_Boundary_ADM0/FeatureServer/0/query"
BASE_ADM1_URL = "https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Detailed_Boundary_ADM1/FeatureServer/0/query"
BASE_ADM2_URL = "https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Detailed_Boundary_ADM2/FeatureServer/0/query"



def get_gis_data(country_code, level):
  base_url = f"https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Detailed_Boundary_{level}/FeatureServer/0/query"

  params = {
    'f': 'json',
    'where': f'ISO_2_CODE=\'{country_code}\'',
    'outFields': '*'
  };
  response = requests.get(base_url, params=params)
  data = response.json()
  features = data['features']
  return features


nat_level_features = get_gis_data("BE", "ADM0")

belgium_adm0 = nat_level_features[0]
pprint(belgium_adm0)

sub1_level_features = get_gis_data("BE", "ADM1")

belgium_adm1 = sub1_level_features[0]
pprint(belgium_adm1)

sub2_level_features = get_gis_data("BE", "ADM2")

belgium_adm2 = sub2_level_features[0]
pprint(belgium_adm2)
