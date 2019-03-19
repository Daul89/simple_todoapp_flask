## Frontend ##
Vue.jsを仕様したシンプルなSPA
`~/frontend`にて`npm install`

Todo APP の仕様
=====================

## APP 紹介 ##
シンプルなTodo APPである  
Viewはindex.htmlをそのまま利用  
下記のAPI仕様書を読み、Backendコードを完成してほしい  
言語はPython、FlameworkはFlaskとする


## API List ##


`1. GET /todos`  
`2. POST /todos`  
`3. GET /todos/<id>`  
`4. DELETE /todos/<id>`



### 1. List all Todo Items ###

**Definition**

`GET /todos`

**Response**

- `200 OK` when success

```json
[
	{
        "id":"1",
        "item":"Training Preps #1"
	},
	{
	    "id":"2",
	    "item":"Training Preps #2"
    }
]
```


### 2. Insert a Todo Item ###

**Definition**

`POST /todos`

**Arguments**

- `"id":integer` identifier of todo item. implicit.
- `"item":string` context of todo item

**Response**

- `201 Created` when success

```json
{
    "id":"1",
    "item":"Training Preps #1"
}
```

### 3. Get a Todo Item ###

**Definition**

`GET /todos/<id>`

**Arguments**

- `"id":integer` identifier of todo item

**Response**

- `200 OK` when success
- `404 Not Found` if id does not exist

```json
{
    "id":"1",
    "item":"Training Preps #1"
}
```


### 4. Delete a Todo Item ###

**Definition**

`DELETE /todos/<id>`

**Arguments**

- `"id":integer` identifier of todo item

**Response**

- `204 No Content` when success
- `404 Not Found` if id does not exist
