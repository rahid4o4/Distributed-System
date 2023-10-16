from flask import Flask, request, send_file
import os
import random

app = Flask(__name)

def search_image(object_class):
    # List all images in the specified object class directory
    image_dir = f'images/{object_class}'
    images = os.listdir(image_dir)
    if images:
        # Select a random image
        image_file = random.choice(images)
        return os.path.join(image_dir, image_file)
    else:
        return None

@app.route('/search', methods=['GET'])
def search():
    object_class = request.args.get('object_class')
    if object_class:
        image_path = search_image(object_class)
        if image_path:
            return send_file(image_path, as_attachment=True)
        else:
            return "Image not found for the specified object class."
    else:
        return "Please specify an object class."

if __name__ == '__main__':
    app.run(threaded=True)
