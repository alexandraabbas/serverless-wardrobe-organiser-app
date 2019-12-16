import json

from datetime import datetime

import googleapiclient.discovery

BUCKET = "wardrobe-organiser"


def upload_image(request):
    request_json = request.get_json()

    if request_json and "user" in request_json:
        user = request_json["user"]

    if request_json and "image" in request_json:
        image = request_json["image"]

    # Construct Cloud Storage file path.
    destination = user + "/" + datetime.now().strftime("%m%d%Y_%H%M%S") + ".png"

    # Service object for the interacting with the Cloud Storage API.
    service = googleapiclient.discovery.build("storage", "v1")

    # Upload the source file.
    req = service.objects().insert(media_body=image, name=destination, bucket=BUCKET)
    resp = req.execute()

    return json.dumps(resp, indent=2)
