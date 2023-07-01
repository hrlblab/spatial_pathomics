import os
import json
import argparse
from PIL import Image, ImageDraw
from shapely.geometry import Polygon, Point

def process_image_with_geojson(image_path, geojson_path):
    img = Image.open(image_path)


    with open(geojson_path) as f:
        geojson = json.load(f)
        polygons = [Polygon(feature['geometry']['coordinates'][0]) for feature in geojson['features']]
        new_img = Image.new('RGB', (img.width, img.height), color='white')
        new_draw = ImageDraw.Draw(new_img)

        for x in range(img.width):
            for y in range(img.height):
                point = Point(x, y)
                if any(poly.contains(point) for poly in polygons):
                    new_img.putpixel((x, y), img.getpixel((x, y)))
                else:
                    new_draw.point((x, y), fill='black')


    new_img.save('./output.jpg', 'JPEG')


parser = argparse.ArgumentParser(description='Process image with GeoJSON')
parser.add_argument('image_path', type=str, help='Path to the image file')
parser.add_argument('geojson_path', type=str, help='Path to the GeoJSON file')


args = parser.parse_args()
process_image_with_geojson(args.image_path, args.geojson_path)