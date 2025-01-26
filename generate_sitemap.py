#!/usr/bin/env python3

import os
from datetime import datetime
from typing import List, Dict

# Import city data from generate_city_pages.py
from generate_city_pages import CITIES

def generate_sitemap_xml() -> str:
    """Generate XML sitemap content."""
    # Start XML
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    # Base URL
    base_url = "https://mpeservices.ca"
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Add main pages
    main_pages = [
        "",  # Homepage
        "/zones-desservies/",
    ]
    
    # Add main pages to sitemap
    for page in main_pages:
        xml += f"""    <url>
        <loc>{base_url}{page}</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>\n"""
    
    # Add city pages
    for city in CITIES:
        xml += f"""    <url>
        <loc>{base_url}/nettoyage-{city['slug']}/</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>\n"""
    
    # Close XML
    xml += '</urlset>'
    return xml

def main():
    """Main function to generate and save sitemap."""
    # Generate sitemap content
    sitemap_content = generate_sitemap_xml()
    
    # Save to file
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    print("✓ Generated sitemap.xml")
    
    # Also create robots.txt if it doesn't exist
    if not os.path.exists('robots.txt'):
        robots_content = f"""User-agent: *
Allow: /

Sitemap: https://mpeservices.ca/sitemap.xml"""
        
        with open('robots.txt', 'w', encoding='utf-8') as f:
            f.write(robots_content)
        print("✓ Generated robots.txt")

if __name__ == '__main__':
    main() 