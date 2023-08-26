import os
from PIL import Image, ImageDraw
import json

# input file path
image_folder = './imag'
geojson_folder = './json'
output_folder = './output'

# get the image list
image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    
   
    last_dot_index = image_file.rfind('.png')
    geojson_file = image_file[:last_dot_index] + '.geojson'
    geojson_path = os.path.join(geojson_folder, geojson_file)
  
    # load image and convert to "RGB"
    image = Image.open(image_path)
    image = image.convert("RGB")


    # load the geojson file
    if os.path.exists(geojson_path):
        print
        with open(geojson_path, 'r') as geojson_file:
            geojson_data = json.load(geojson_file)
            
            # 
            coordinates = geojson_data['features'][0]['geometry']['coordinates'][0]
            draw = ImageDraw.Draw(image)

            for i in range(len(coordinates) - 1):
                start = coordinates[i]
                end = coordinates[i + 1]
                pixel_start = (int(start[0]), int(start[1]))
                pixel_end = (int(end[0]), int(end[1]))
                draw.line([pixel_start, pixel_end], fill='yellow', width=2)

    output_image_path = os.path.join(output_folder, image_file)
  
    image.save(output_image_path)

    print(f"Processed: {image_file}")

print("Processing complete.")
