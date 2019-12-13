# HTTP Serverless Backend

## Delpoy cloud functions

```bash
gcloud functions deploy hello_get --runtime python37 --trigger-http
```

## Trigger cloud functions

```bash
curl "https://REGION-PROJECT_ID.cloudfunctions.net/hello_get"
```
