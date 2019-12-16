# HTTP Serverless Backend

## Delpoy cloud functions

```bash
gcloud functions deploy upload_image --runtime python37 --trigger-http
```

## Trigger cloud functions

```bash
curl -X POST "https://us-central1-datatonic-uk-research.cloudfunctions.net/upload_image" -H "Content-Type:application/json" -d '{"user": "alexaabbas", "image": "img.png"}'
```
