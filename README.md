# Recyclees
This API was written for the CAPSTONE Udacity Project for the Full-Stack nanodegree.  I got the idea from the first hackathon I attended.  Regrettably, we didn't have enough team members and had to split to a different team.  Shoutout to the guy who came up with the idea (wish I could credit you for it)!


## Introduction
An app with routes that performs CRUD operations on a Heroku PSQL database. Used [Auth0](https://auth0.com/ "Auth0's Homepage") for authentication.


## Getting started
You have the following two options: 

#### Use the hosted API

Base URL: https://recyclees.herokuapp.com/


#### Run locally

Make sure that you have the key dependencies (Python 3, pip, Flask, SQLAlchemy) installed!


1. Fork or copy this repository
2. Create a virtual environment (highly recommended, see the official [python documentation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) for help)
3. Create a Postgres Database
4. Open your terminal and run `pip install -r requirements.txt`
5. In `models.py` comment out line 6 and uncomment line 7 with the name of your local database
6. In your terminal, export TOKEN (since there is no frontend yet, feel free to ask me for an Auth0 bearer token) 
7. To run the server, execute `export FLASK_APP=api.py` following `flask run --reload`


## Roles / API Permissions / Authentication
The API has three different roles which have been set up with the help of [Auth0](https://auth0.com/ "Auth0's Homepage"):
1. Admin
2. Donor
3. Donees

These are all the permissions:
- `create:items`
- `delete:items`
- `update:items`
- `get:items`
- `create:users`

Admins have all the permissions.
Donors have the following permissions: `create:items`, `delete:items`, `update:items`, `get:items`.
Donees have the permission to do the following: `get:items`, and `update:items`.



## API Endpoints

### Public

#### GET  '/api/public'
Returns at max ten items posted for donation which have not been claimed yet and a message. No authentication required.

##### Sample curl

```shell
curl --request GET \
--url https://recyclees.herokuapp.com/api/public/items
```

Result:

```json
{
  "items": [
    {
      "brand": "Apple",
      "category": "Mobile Phones",
      "condition": "Used",
      "delivery": "True",
      "description": "Cracked screen, but still functional. Will ship with new charger!",
      "donee": null,
      "donor": 1,
      "id": 106,
      "item_name": "iPhone 4s"
    },
    {
      "brand": "Apple",
      "category": "Laptops",
      "condition": "Used",
      "delivery": "True",
      "description": "Will ship in original packaging.",
      "donee": null,
      "donor": 1,
      "id": 107,
      "item_name": "MacBook Pro"
    }
  ],
  "message": "These items are up for grabs! Sign in to claim.",
  "success": true
}
```



### Donors API routes

#### GET  '/api/donors/<USER_ID>/items
Returns a list of items a donor with `USER_ID` has added to the database.  This endpoint needs authentication and the `get:items` permission.  Make sure to replace `<INSERT BEARER TOKEN>` with your token.

##### Sample curl

```shell
curl --request GET \
--url https://recyclees.herokuapp.com/api/donors/1/items \
--header 'authorization: Bearer <INSERT BEARER TOKEN>'
```

Result:

```json
{
    "items": [
        {
            "brand": "Apple",
            "category": "Laptops",
            "condition": "Used",
            "delivery": "True",
            "description": "Will ship in original packaging.",
            "donee": null,
            "donor": 1,
            "id": 1,
            "item_name": "MacBook Pro"
        },
        {
            "brand": "Apple",
            "category": "Mobile Phones",
            "condition": "Used",
            "delivery": "True",
            "description": "Cracked screen, but still functional.",
            "donee": null,
            "donor": 1,
            "id": 2,
            "item_name": "iPhone 4"
        }
    ],
    "success": true
}
```



#### POST  '/api/donors/<USER_ID>/items
Adds an item to the database and associates it to the donor. This endpoint needs authentication and the `create:items` permission.  Returns a message and the added item upon success. Make sure to replace `<INSERT BEARER TOKEN>` with your token.

##### Sample curl

```shell
curl -X POST \
-H "Content-Type: application/json" \
--data '{"item_name":"MacBook Pro" ,"brand":"Apple" ,"category":"Laptops" ,"condition":"Used" ,"description":"Will ship in original packaging." ,"delivery":"True"}' \
--header 'authorization: Bearer <INSERT BEARER TOKEN>' \
--url https://recyclees.herokuapp.com/api/donors/1/items 
```

Result:

```json
{
    "new_item": {
        "brand": "Apple",
        "category":" Laptops",
        "condition": "Used",
        "delivery": "True",
        "description": "Will ship in original packaging.",
        "donee": null,
        "donor": 1,
        "id": 1,
        "item_name": "MacBook Pro"
        },
    "success": true
}
```



#### DELETE '/api/donors/<USER_ID>/items/<ITEM_ID>
Deletes an item from the database which has been added by donor. This endpoint needs authentication and the `delete:items` permission. Returns message and the deleted item upon success. Make sure to replace `<INSERT BEARER TOKEN>` with your token.

##### Sample curl

```shell
curl -X DELETE \
-H "Content-Type: application/json" \
--header 'authorization: Bearer <INSERT BEARER TOKEN>' \
--url https://recyclees.herokuapp.com/api/donors/1/items/3 
```

Result:

```json
{
    "deleted_item": {
        "brand": "Apple",
        "category": "Mobile Phones",
        "condition": "Used",
        "delivery": "True",
        "description": "Cracked screen, but still functional.",
        "donee": null,
        "donor": 1,
        "id": 3,
        "item_name": "iPhone 4"
    },
    "success": true
}
```



#### PATCH '/api/donors/<USER_ID>/items/<ITEM_ID>
Update an item in the database which has been added by donor. This endpoint needs authentication and the `update:items` permission. Returns message and the updated item upon success. Make sure to replace `<INSERT BEARER TOKEN>` with your token.

##### Sample curl

```shell
curl --request PATCH \
-H "Content-Type: application/json" \
--header 'authorization: Bearer <INSERT BEARER TOKEN>' \
--data '{"brand":"Apple","category":"Mobile Phones","condition":"Used","delivery":"True","description":"Cracked screen, but still functional. Will ship with new charger!","item_name":"iPhone 4s"}' \
--url https://recyclees.herokuapp.com/api/donors/1/items/2
```

Result:

```json
{
    "updated_item": {
        "brand": "Apple",
        "category": "Mobile Phones",
        "condition": "Used",
        "delivery": "True",
        "description": "Cracked screen, but still functional. Will ship with new charger!",
        "donee": null,
        "donor": 1,
        "id": 2,
        "item_name": "iPhone 4s"
    },
    "success": true
}
```



### Donee API routes

#### GET '/api/donees/<USER_ID>/items
Returns a list of items a donee with `USER_ID` has claimed from the database. This endpoint needs authentication and the `get:items` permission. Make sure to replace `<INSERT BEARER TOKEN>` with your token.

##### Sample curl

```shell
curl --request GET \
--header 'authorization: Bearer <INSERT BEARER TOKEN>' \
--url https://recyclees.herokuapp.com/api/donees/1/items
```

Result:

```json
{
  "items": [
    {
      "brand": "Apple",
      "category": "Laptops",
      "condition": "Used",
      "delivery": true,
      "description": "Will ship in original packaging.",
      "donee": null,
      "donor": 1,
      "id": 1,
      "item_name": "MacBook Pro"
    },
    {
      "brand": "Apple",
      "category": "Mobile Phones",
      "condition": "Used",
      "delivery": "True",
      "description": "Cracked screen, but still functional. Will ship with new charger!",
      "donee": null,
      "donor": 1,
      "id": 2,
      "item_name": "iPhone 4s"
    }
  ],
  "success": true
}
```



#### PATCH '/api/donees/<USER_ID>/items/<ITEM_ID>
Returns the item claimed from the database. This endpoint needs authentication and the `update:items` permission. Make sure to replace `<INSERT BEARER TOKEN>` with your token.

##### Sample curl

```shell
curl --request PATCH \
--header 'authorization: Bearer <INSERT BEARER TOKEN>' \
--url https://recyclees.herokuapp.com/api/donees/1/items/2
```

Result:

```json
{
  "item_claimed": {
      "brand": "Apple",
      "category": "Mobile Phones",
      "condition": "Used",
      "delivery": "True",
      "description": "Cracked screen, but still functional. Will ship with new charger!",
      "donee": null,
      "donor": 1,
      "id": 2,
      "item_name": "iPhone 4s"
    },
  "success": true
}
```



### Admin Routes (User Creation)

#### POST '/api/donors'
Returns the posted donor and a message. Make sure to replace `<INSERT BEARER TOKEN>` with your token.

##### Sample curl

```shell
curl -X POST \
-H "Content-Type: application/json" \
-d '{"user_name":"peter_smith", "first_name": "Peter", "last_name": "Smith", "state": "New Jersey", "city": "Jersey City"}' \
--header 'authorization: Bearer <INSERT BEARER TOKEN>' \
--url https://recyclees.herokuapp.com/api/donors
```

Result:

```json
{
    "new_donor": {
        "city": "Jersey City",
        "first_name": "Peter",
        "id": 2,
        "items": [],
        "last_name": "Smith",
        "state": "New Jersey",
        "user_name": "peter_smith"
    },
    "success": true
}

```



#### POST '/api/donees'
Returns the posted donee and a message. Make sure to replace `<INSERT BEARER TOKEN>` with your token.

##### Sample curl

```shell
curl --request POST \
-H "Content-Type: application/json" \
-d '{"user_name":"HSCT", "first_name": "Melissa", "last_name": "Grant", "state": "Connecticut", "city": "Hartford", "organization": "Homeless Shelter in Hartford, CT"}' \
--header 'authorization: Bearer <INSERT BEARER TOKEN>' \
https://recyclees.herokuapp.com/api/donees
```

Result:

```json
{
  "new_donee": {
    "city": "Hartford",
    "first_name": "Melissa",
    "id": 68,
    "items": [],
    "last_name": "Grant",
    "organization": "Homeless Shelter in Hartford, CT",
    "state": "Connecticut",
    "user_name": "HSCT"
  },
  "success": true
}
```


## TODOS

Things that I want to add soon:
1. The frontend!
2. Verifications for entering data into the database (State name, boolean types, etc...)