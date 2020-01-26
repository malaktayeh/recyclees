# Recyclees

## Project description
An app with routes which performs CRUD operations on a Heroku PSQL database.


## API Endpoints

### POST '/api/donors'
Returns the posted donor and a message

#### Sample curl

```shell
curl -H "Content-Type: application/json" -X POST \
-d '{"user_name":"peter_smith", "first_name": "Peter", "last_name": "Smith", "state": "New Jersey", "city": "Jersey City"}' \
--header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UZEJPVFV3TlVKRlJqZEdPRFpDUlRBNU56VTBPRE01TlRsQ05EQkdNRVUxUVVORU1rUTJOdyJ9.eyJpc3MiOiJodHRwczovL3JlY3ljbGVlcy5hdXRoMC5jb20vIiwic3ViIjoiWlI0U0RjV0Z5YzdEMm1DMWc1TDRzdHlGY08zZmdJSWZAY2xpZW50cyIsImF1ZCI6InJlY3ljbGVlcyIsImlhdCI6MTU3OTM4MjcwNiwiZXhwIjoxNTgxMTEwNzA2LCJhenAiOiJaUjRTRGNXRnljN0QybUMxZzVMNHN0eUZjTzNmZ0lJZiIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbXX0.PBstHG8MuXhiopPP-HsQpoUkBaqopaAWy_gItwzqitbQvpPEUxK7cLOrjA0Age2WyJPx2jJs6giVb8cMnQipf0MZ0eFnixKV9QxFq3HhGOUyzlIymwWhg4H7VGBeYzENLiyDjDR2WJV2JKZoAUdOyws2tKpySg1juN6cqdUnYgGcxcDhS_IsR3AjXs17MoWUYYJEWKZDEBMPh05f9TcoKTMbfudxHmVhfhGcnAw3vU4qHYzTFl9YiQHHOR31IBsr0-H5E1CDQ98qx-3kbKrXWctGvRnLxTaidNrObyYmck-rmSRt6obM2673Ysbmo9VEZXajlGAw1VBvCP7HpoS5pQ' \
https://recyclees.herokuapp.com/api/donors

```

Result:

```json
{"donor":{"city":"Jersey City","first_name":"Peter","id":1,"items":[],"last_name":"Smith","state":"New Jersey","user_name":"peter_smith"},"success":true}

```

### POST '/api/donees'
Returns the posted donee and a message

#### Sample curl

```shell
curl -H "Content-Type: application/json" -X POST \
-d '{"user_name":"HSCT", "first_name": "Melissa", "last_name": "Grant", "state": "Connecticut", "city": "Hartford", "organization": "Homeless Shelter in Hartford, CT"}' \
--header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UZEJPVFV3TlVKRlJqZEdPRFpDUlRBNU56VTBPRE01TlRsQ05EQkdNRVUxUVVORU1rUTJOdyJ9.eyJpc3MiOiJodHRwczovL3JlY3ljbGVlcy5hdXRoMC5jb20vIiwic3ViIjoiWlI0U0RjV0Z5YzdEMm1DMWc1TDRzdHlGY08zZmdJSWZAY2xpZW50cyIsImF1ZCI6InJlY3ljbGVlcyIsImlhdCI6MTU3OTM4MjcwNiwiZXhwIjoxNTgxMTEwNzA2LCJhenAiOiJaUjRTRGNXRnljN0QybUMxZzVMNHN0eUZjTzNmZ0lJZiIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbXX0.PBstHG8MuXhiopPP-HsQpoUkBaqopaAWy_gItwzqitbQvpPEUxK7cLOrjA0Age2WyJPx2jJs6giVb8cMnQipf0MZ0eFnixKV9QxFq3HhGOUyzlIymwWhg4H7VGBeYzENLiyDjDR2WJV2JKZoAUdOyws2tKpySg1juN6cqdUnYgGcxcDhS_IsR3AjXs17MoWUYYJEWKZDEBMPh05f9TcoKTMbfudxHmVhfhGcnAw3vU4qHYzTFl9YiQHHOR31IBsr0-H5E1CDQ98qx-3kbKrXWctGvRnLxTaidNrObyYmck-rmSRt6obM2673Ysbmo9VEZXajlGAw1VBvCP7HpoS5pQ' \
https://recyclees.herokuapp.com/api/donees
```

Result:

```json
{"donor":{"city":"Hartford","first_name":"Melissa","id":1,"items":[],"last_name":"Grant","organization":"Homeless Shelter in Hartford, CT","state":"Connecticut","user_name":"HSCT"},"success":true}
```