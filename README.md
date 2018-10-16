Todo APP の仕様
=====================

## APP 紹介 ##
シンプルなTodo APPである  
Viewはindex.htmlをそのまま利用  
下記のAPI仕様書を読み、Backendコードを完成してほしい  
言語はPython、FlameworkはFlaskとする

## API List ##


`1. GET /tasks`  
`2. POST /tasks`  
`3. GET /task/<id>`  
`4. DELETE /task/<id>`



### 1. List all Todo Items ###

**Definition**

`GET /tasks`

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

`POST /tasks`

**Arguments**

- `"id":integer` identifier of todo item
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

`GET /task/<id>`

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

`DELETE /task/<id>`

**Arguments**

- `"id":integer` identifier of todo item

**Response**

- `204 No Content` when success
- `404 Not Found` if id does not exist