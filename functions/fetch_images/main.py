import json

import googleapiclient.discovery

BUCKET = "wardrobe-organiser"


def create_service():
    """Creates the service object for calling the Cloud Storage API."""
    # Construct the service object for interacting with the Cloud Storage API -
    # the 'storage' service, at version 'v1'.
    return googleapiclient.discovery.build("storage", "v1")


def get_bucket_metadata(bucket):
    """Retrieves metadata about the given bucket."""
    service = create_service()

    # Make a request to buckets.get to retrieve a list of objects in the
    # specified bucket.
    req = service.buckets().get(bucket=bucket)
    return req.execute()


def list_bucket(bucket):
    """Returns a list of metadata of the objects within the given bucket."""
    service = create_service()

    # Create a request to objects.list to retrieve a list of objects.
    fields_to_return = "nextPageToken,items(name,size,contentType,metadata(my-key))"
    req = service.objects().list(bucket=bucket, fields=fields_to_return)

    all_objects = []
    # If you have too many items to list in one request, list_next() will
    # automatically handle paging with the pageToken.
    while req:
        resp = req.execute()
        all_objects.extend(resp.get("items", []))
        req = service.objects().list_next(req, resp)

    return all_objects


def fetch_image(request):
    request_json = request.get_json()

    if request_json and "user" in request_json:
        user = request_json["user"]

    print(json.dumps(get_bucket_metadata(BUCKET), indent=2))
    print(json.dumps(list_bucket(BUCKET), indent=2))

    return json.dumps(get_bucket_metadata(BUCKET), indent=2)
