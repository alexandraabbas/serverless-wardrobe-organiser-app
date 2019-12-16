import json

import googleapiclient.discovery

BUCKET = "wardrobe-organiser"


def create_service():
    """Creates the service object for calling the Cloud Storage API."""
    # Construct the service object for interacting with the Cloud Storage API -
    # the 'storage' service, at version 'v1'.
    return googleapiclient.discovery.build("storage", "v1")


def list_bucket(bucket, user):
    """Returns a list of metadata of the objects within the given bucket."""
    service = create_service()

    # Create a request to objects.list to retrieve a list of objects.
    fields_to_return = "nextPageToken,items(name,size,contentType,metadata(my-key))"
    req = service.objects().list(bucket=bucket, prefix=user, fields=fields_to_return)

    all_objects = []
    # If you have too many items to list in one request, list_next() will
    # automatically handle paging with the pageToken.
    while req:
        resp = req.execute()
        all_objects.extend(resp.get("items", []))
        req = service.objects().list_next(req, resp)

    return all_objects


def fetch_images(request):
    request_json = request.get_json()

    if request_json and "user" in request_json:
        user = request_json["user"]

    return json.dumps(list_bucket(BUCKET, user), indent=2)
