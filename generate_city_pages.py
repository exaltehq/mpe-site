#!/usr/bin/env python3

import os
import json

# City data - you can extend this list
CITIES = [
    {
        "name": "Laval",
        "slug": "laval", 
        "latitude": "45.5867",
        "longitude": "-73.6929",
        "map_zoom": "40000"
    },
    {
        "name": "Longueuil",
        "slug": "longueuil",
        "latitude": "45.5362",
        "longitude": "-73.5123", 
        "map_zoom": "40000"
    },
    {
        "name": "Terrebonne",
        "slug": "terrebonne",
        "latitude": "45.6929",
        "longitude": "-73.6329",
        "map_zoom": "40000"
    },
    {
        "name": "Montréal",
        "slug": "montreal",
        "latitude": "45.5017",
        "longitude": "-73.5673",
        "map_zoom": "40000"
    },
    {
        "name": "Boisbriand",
        "slug": "boisbriand", 
        "latitude": "45.6134",
        "longitude": "-73.8339",
        "map_zoom": "40000"
    },
    {
        "name": "Blainville",
        "slug": "blainville",
        "latitude": "45.6759",
        "longitude": "-73.8874",
        "map_zoom": "40000"
    },
    {
        "name": "Sainte-Thérèse",
        "slug": "sainte-therese",
        "latitude": "45.6325",
        "longitude": "-73.8322",
        "map_zoom": "40000"
    },
    {
        "name": "Rosemère",
        "slug": "rosemere",
        "latitude": "45.6300",
        "longitude": "-73.8000",
        "map_zoom": "40000"
    },
    {
        "name": "Bois-des-Filion",
        "slug": "bois-des-filion",
        "latitude": "45.6683",
        "longitude": "-73.7511",
        "map_zoom": "40000"
    },
    {
        "name": "Lorraine",
        "slug": "lorraine",
        "latitude": "45.6780",
        "longitude": "-73.7652",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Eustache",
        "slug": "saint-eustache",
        "latitude": "45.5613",
        "longitude": "-73.9016",
        "map_zoom": "40000"
    },
    {
        "name": "Deux-Montagnes",
        "slug": "deux-montagnes",
        "latitude": "45.5436",
        "longitude": "-73.8875",
        "map_zoom": "40000"
    },
    {
        "name": "Mirabel",
        "slug": "mirabel",
        "latitude": "45.6500",
        "longitude": "-74.0833",
        "map_zoom": "40000"
    },
    {
        "name": "Mascouche",
        "slug": "mascouche",
        "latitude": "45.7501",
        "longitude": "-73.6004",
        "map_zoom": "40000"
    },
    {
        "name": "Repentigny",
        "slug": "repentigny",
        "latitude": "45.7420",
        "longitude": "-73.4506",
        "map_zoom": "40000"
    },
    {
        "name": "L'Assomption",
        "slug": "l-assomption",
        "latitude": "45.8333",
        "longitude": "-73.4167",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Sulpice",
        "slug": "saint-sulpice",
        "latitude": "45.8281",
        "longitude": "-73.3808",
        "map_zoom": "40000"
    },
    {
        "name": "Sainte-Julienne",
        "slug": "sainte-julienne",
        "latitude": "45.9628",
        "longitude": "-73.7157",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Jérôme",
        "slug": "saint-jerome",
        "latitude": "45.7760",
        "longitude": "-74.0033",
        "map_zoom": "40000"
    },
    {
        "name": "Joliette",
        "slug": "joliette",
        "latitude": "46.0167",
        "longitude": "-73.4500",
        "map_zoom": "40000"
    },
    {
        "name": "Brossard",
        "slug": "brossard",
        "latitude": "45.4753",
        "longitude": "-73.4538",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Lambert",
        "slug": "saint-lambert",
        "latitude": "45.4945",
        "longitude": "-73.5106",
        "map_zoom": "40000"
    },
    {
        "name": "Boucherville",
        "slug": "boucherville",
        "latitude": "45.5953",
        "longitude": "-73.4333",
        "map_zoom": "40000"
    },
    {
        "name": "La Prairie",
        "slug": "la-prairie",
        "latitude": "45.4165",
        "longitude": "-73.4997",
        "map_zoom": "40000"
    },
    {
        "name": "Candiac",
        "slug": "candiac",
        "latitude": "45.3853",
        "longitude": "-73.5162",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Constant",
        "slug": "saint-constant",
        "latitude": "45.3743",
        "longitude": "-73.5667",
        "map_zoom": "40000"
    },
    {
        "name": "Sainte-Catherine",
        "slug": "sainte-catherine",
        "latitude": "45.4031",
        "longitude": "-73.5809",
        "map_zoom": "40000"
    },
    {
        "name": "Delson",
        "slug": "delson",
        "latitude": "45.3694",
        "longitude": "-73.5496",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Bruno-de-Montarville",
        "slug": "saint-bruno-de-montarville",
        "latitude": "45.5319",
        "longitude": "-73.3450",
        "map_zoom": "40000"
    },
    {
        "name": "Sainte-Julie",
        "slug": "sainte-julie",
        "latitude": "45.5817",
        "longitude": "-73.3336",
        "map_zoom": "40000"
    },
    {
        "name": "Carignan",
        "slug": "carignan",
        "latitude": "45.4636",
        "longitude": "-73.3072",
        "map_zoom": "40000"
    },
    {
        "name": "Chambly",
        "slug": "chambly",
        "latitude": "45.4436",
        "longitude": "-73.2929",
        "map_zoom": "40000"
    },
    {
        "name": "Varennes",
        "slug": "varennes",
        "latitude": "45.6833",
        "longitude": "-73.4333",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Jean-sur-Richelieu",
        "slug": "saint-jean-sur-richelieu",
        "latitude": "45.3073",
        "longitude": "-73.2629",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Basile-le-Grand",
        "slug": "saint-basile-le-grand",
        "latitude": "45.5340",
        "longitude": "-73.2786",
        "map_zoom": "40000"
    },
    {
        "name": "Marieville",
        "slug": "marieville",
        "latitude": "45.4363",
        "longitude": "-73.1665",
        "map_zoom": "40000"
    },
    {
        "name": "Richelieu",
        "slug": "richelieu",
        "latitude": "45.4400",
        "longitude": "-73.2469",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Césaire",
        "slug": "saint-cesaire",
        "latitude": "45.4167",
        "longitude": "-72.9500",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Hyacinthe",
        "slug": "saint-hyacinthe",
        "latitude": "45.6300",
        "longitude": "-72.9500",
        "map_zoom": "40000"
    },
    {
        "name": "Contrecoeur",
        "slug": "contrecoeur",
        "latitude": "45.8531",
        "longitude": "-73.2317",
        "map_zoom": "40000"
    },
    {
        "name": "Sorel-Tracy",
        "slug": "sorel-tracy",
        "latitude": "46.0354",
        "longitude": "-73.1173",
        "map_zoom": "40000"
    },
    {
        "name": "Yamaska",
        "slug": "yamaska",
        "latitude": "46.0381",
        "longitude": "-72.9611",
        "map_zoom": "40000"
    },
    {
        "name": "Berthierville",
        "slug": "berthierville",
        "latitude": "46.0833",
        "longitude": "-73.1833",
        "map_zoom": "40000"
    },
    {
        "name": "Vaudreuil-Dorion",
        "slug": "vaudreuil-dorion",
        "latitude": "45.3970",
        "longitude": "-74.0322",
        "map_zoom": "40000"
    },
    {
        "name": "Hudson",
        "slug": "hudson",
        "latitude": "45.4609",
        "longitude": "-74.1437",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Lazare",
        "slug": "saint-lazare",
        "latitude": "45.4001",
        "longitude": "-74.1284",
        "map_zoom": "40000"
    },
    {
        "name": "Coteau-du-Lac",
        "slug": "coteau-du-lac",
        "latitude": "45.2792",
        "longitude": "-74.1792",
        "map_zoom": "40000"
    },
    {
        "name": "Les Coteaux",
        "slug": "les-coteaux",
        "latitude": "45.2632",
        "longitude": "-74.2173",
        "map_zoom": "40000"
    },
    {
        "name": "Salaberry-de-Valleyfield",
        "slug": "salaberry-de-valleyfield",
        "latitude": "45.2532",
        "longitude": "-74.1329",
        "map_zoom": "40000"
    },
    {
        "name": "Beauharnois",
        "slug": "beauharnois",
        "latitude": "45.3168",
        "longitude": "-73.8690",
        "map_zoom": "40000"
    },
    {
        "name": "Kahnawake",
        "slug": "kahnawake",
        "latitude": "45.4090",
        "longitude": "-73.6653",
        "map_zoom": "40000"
    },
    {
        "name": "Châteauguay",
        "slug": "chateauguay",
        "latitude": "45.3617",
        "longitude": "-73.7499",
        "map_zoom": "40000"
    },
    {
        "name": "Mercier",
        "slug": "mercier",
        "latitude": "45.3257",
        "longitude": "-73.7483",
        "map_zoom": "40000"
    },
    {
        "name": "Sainte-Martine",
        "slug": "sainte-martine",
        "latitude": "45.2618",
        "longitude": "-73.7505",
        "map_zoom": "40000"
    },
    {
        "name": "Granby",
        "slug": "granby",
        "latitude": "45.3967",
        "longitude": "-72.7324",
        "map_zoom": "40000"
    },
    {
        "name": "Bromont",
        "slug": "bromont",
        "latitude": "45.3167",
        "longitude": "-72.6500",
        "map_zoom": "40000"
    },
    {
        "name": "Cowansville",
        "slug": "cowansville",
        "latitude": "45.2059",
        "longitude": "-72.7435",
        "map_zoom": "40000"
    },
    {
        "name": "Saint-Sauveur",
        "slug": "saint-sauveur",
        "latitude": "45.8933",
        "longitude": "-74.1572",
        "map_zoom": "40000"
    },
    {
        "name": "Sainte-Adèle",
        "slug": "sainte-adele",
        "latitude": "45.9516",
        "longitude": "-74.1325",
        "map_zoom": "40000"
    }
]

def ensure_directory(path):
    """Ensure the output directory exists"""
    if not os.path.exists(path):
        os.makedirs(path)

def generate_city_pages():
    """Generate city-specific landing pages from template"""
    # Read template
    with open('templates/city-landing.html', 'r', encoding='utf-8') as template_file:
        template = template_file.read()
    
    # Generate pages for each city
    for city in CITIES:
        # Create directory path
        dir_path = f"nettoyage-{city['slug']}"
        ensure_directory(dir_path)
        
        # Replace placeholders
        page_content = template\
            .replace('{{city}}', city['name'])\
            .replace('{{city-slug}}', city['slug'])\
            .replace('{{latitude}}', city['latitude'])\
            .replace('{{longitude}}', city['longitude'])\
            .replace('{{map-zoom}}', city['map_zoom'])
        
        # Write city-specific file
        output_path = os.path.join(dir_path, "index.html")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_content)
        print(f"Generated landing page for {city['name']} at {dir_path}/")

if __name__ == "__main__":
    generate_city_pages() 