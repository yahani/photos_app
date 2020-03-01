# API

## Create a user

POST : https://heroku-photos-app.herokuapp.com/users/


Headers:

	Content-Type: application/x-www-form-urlencoded
	
Body:

	username: user
	
	password: user@123 (at lease 8 charactors)
	
	email: user@123.com (optional)
	
Response:

    {
    
        "email": "user@123.com",
	
        "username": "user"
	
    }
    
    
## Obtain JWT token

POST: https://heroku-photos-app.herokuapp.com/api/token/

Headers:

	Content-Type: application/x-www-form-urlencoded
	
Body:

	username: user
	
	password: user@123
	
Response:

{

    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MzEyODIyMSwianRpIjoiNGU4ZmJiYzU0NmM1NDgzMDlkMDkzNTA3NzhkYWQ1NDciLCJ1c2VyX2lkIjoyfQ.-V7-xy_vmirqLb2eM6_8BHqcw0BMzCeliAZLY91TLvw",
    
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMDQyMTIxLCJqdGkiOiIyMmM1ZjJmZWY3MWE0OTk5ODQ0MTA3NDgzNWFjNDcwMiIsInVzZXJfaWQiOjJ9.L9UnDgPnCj0ezHRyG0z1d3k-p3sq9yseP1QMLAoB2l0"
    
}

	
## Photos API 


### Post a photo

PUT: https://heroku-photos-app.herokuapp.com/photos/

Headers:

	Content-Type: application/x-www-form-urlencoded
	
	Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMDQyMTIxLCJqdGkiOiIyMmM1ZjJmZWY3MWE0OTk5ODQ0MTA3NDgzNWFjNDcwMiIsInVzZXJfaWQiOjJ9.L9UnDgPnCj0ezHRyG0z1d3k-p3sq9yseP1QMLAoB2l0
	
Body:

	image: file
	
	is_draft: true/false
	
	caption: sample caption
	
Response:

{

    "id": 9,
    
    "image": "images/87459846_2228754534097009_1867908885080178688_n.jpg",
    
    "caption": "sample caption",
    
    "created": "2020-03-01T05:32:28.367226Z",
    
    "saved": null,
    
    "user": 2
    
}

* saved: null if is_draft:true else datetime.now

* image_size < 3mb, image_dimensions < 4000*4000 px

### Edit Photo

POST: https://heroku-photos-app.herokuapp.com/photos/<id>
	
Headers:

	Content-Type: application/x-www-form-urlencoded
	
	Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMDQyMTIxLCJqdGkiOiIyMmM1ZjJmZWY3MWE0OTk5ODQ0MTA3NDgzNWFjNDcwMiIsInVzZXJfaWQiOjJ9.L9UnDgPnCj0ezHRyG0z1d3k-p3sq9yseP1QMLAoB2l0
	
Body:

	is_draft: true/false
	
	caption: sample caption to update
	
Response:

{

    "id": 9,
    
    "image": "images/87459846_2228754534097009_1867908885080178688_n.jpg",
    
    "caption": "sample caption to update",
    
    "created": "2020-03-01T05:32:28.367226Z",
    
    "saved": null,
    
    "user": 2
    
}

### Delete Photo

DELETE: https://heroku-photos-app.herokuapp.com/photos/<id>
	
Headers:

	Content-Type: application/x-www-form-urlencoded
	
	Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMDQyMTIxLCJqdGkiOiIyMmM1ZjJmZWY3MWE0OTk5ODQ0MTA3NDgzNWFjNDcwMiIsInVzZXJfaWQiOjJ9.L9UnDgPnCj0ezHRyG0z1d3k-p3sq9yseP1QMLAoB2l0
	
Response:

{

	"Photo ID <id> is deleted.
	
}

### List Photos

GET: https://heroku-photos-app.herokuapp.com/photos/list/

Headers:

	Content-Type: application/x-www-form-urlencoded
	
	Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgzMDQyMTIxLCJqdGkiOiIyMmM1ZjJmZWY3MWE0OTk5ODQ0MTA3NDgzNWFjNDcwMiIsInVzZXJfaWQiOjJ9.L9UnDgPnCj0ezHRyG0z1d3k-p3sq9yseP1QMLAoB2l0
	
Body:

	filter_type: all/myphotos/mydrafts
	
	sort: asc/desc
	
Response:

[

    {
    
        "id": 4,
	
        "image": "images/87499384_2228754627430333_5481254125196804096_n.jpg",
	
        "caption": "fdgfdgfdgg",
	
        "created": "2020-03-01T12:09:09.169332Z",
	
        "saved": "2020-03-01T11:53:16.747673Z",
	
        "user": 2
	
    },
    
    {
    
        "id": 9,
	
        "image": "images/87459846_2228754534097009_1867908885080178688_n.jpg",
	
        "caption": "6766767",
	
        "created": "2020-03-01T05:32:47.004475Z",
	
        "saved": null,
	
        "user": 2
	
    }
    
]



