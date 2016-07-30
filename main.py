import os

from flask import Flask, request, jsonify
from clarifai.client import ClarifaiApi

os.environ['CLARIFAI_APP_ID'] = 'sTqW-xHoMnvCcxyJAXWXbZxe3XOxtzYfsik4A218'
os.environ['CLARIFAI_APP_SECRET'] = '0OACpD2GFomsFNVzO80uFqQDvXzSX2nVAExCe-d_'

app = Flask(__name__)


@app.route("/")
def proxy():
    image_url = request.args.get('image_url')
    clarifai_api = ClarifaiApi(
        model='general-v1.3')  # assumes environment variables are set.
    result = clarifai_api.tag_image_urls(image_url)
    return jsonify(result)

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int("80"), debug=True)
