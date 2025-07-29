# sad-backend
Super Admin Dashboard(SAD) - backend application with Python-Django framework


Ensure your Django project is running at:
https://localhost:8000/api

If you're using Visual Studio:
â€¢	Set the API project as Startup Project
â€¢	Press F5 or click Start Debugging
________________________________________
ðŸ”¹ 8. Common Pages and Actions

________________________________________


API End points:
http://127.0.0.1:8000/api/user/
{
    "users": "http://127.0.0.1:8000/api/user/users/",
    "permissions": "http://127.0.0.1:8000/api/user/permissions/"
}

http://127.0.0.1:8000/api/comment/
{
    "comments": "http://127.0.0.1:8000/api/comment/comments/",
    "history": "http://127.0.0.1:8000/api/comment/history/"
}

Login.jsx:
http://127.0.0.1:8000/api/token/
{
  "username": "user1",
  "password": "Test1234"
}
{
  "username": "user1@example.com",
  "password": "Test1234"
}
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MzgyNjkyMCwiaWF0IjoxNzUzNzQwNTIwLCJqdGkiOiJiOWY4ZjYxZDA4OTM0NzFiOWQ5MWFmYTRhNjQxMTI5NSIsInVzZXJfaWQiOiIzIn0.x8sErAOSsSoWA8s68lx09MuWWSP8LU0H3hoK8Vj6xmQ",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzNzQ0MTIwLCJpYXQiOjE3NTM3NDA1MjAsImp0aSI6ImY1MDNhNDFiMTZiNTQ0NGJiZmEzODM2MDVhODk4MGZkIiwidXNlcl9pZCI6IjMifQ.vYkqOcrt59GmuibP_wkp9Mq6uYZIZgLAtfJXTyhea_o"
}

http://127.0.0.1:8000/api/user/users/
Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzNzM3Mzg0LCJpYXQiOjE3NTM3MzM3ODQsImp0aSI6ImIxMDk3NDQwNzcxOTQ3NWViMmJhNTcyOTViOWJmMDI2IiwidXNlcl9pZCI6IjMifQ.Cp1gd6y1t3PP-6TsudvlBPsYanpDKxV7EyYrkL9S4Ks

{
  "username": "user1@example.com",
  "password": "Test1234"
}
[
  {
    "id": 1,
    "last_login": null,
    "is_superuser": true,
    "username": "admin",
    "first_name": "",
    "last_name": "",
    "email": "admin@gmail.com",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2025-07-28T15:56:18.254931Z",
    "is_super_admin": false,
    "groups": [],
    "user_permissions": []
  },
  {
    "id": 2,
    "last_login": "2025-07-28T17:29:15.131245Z",
    "is_superuser": true,
    "username": "superadmin",
    "first_name": "",
    "last_name": "",
    "email": "superadmin@gmail.com",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2025-07-28T16:16:17.227633Z",
    "is_super_admin": false,
    "groups": [],
    "user_permissions": []
  },
  {
    "id": 3,
    "last_login": null,
    "is_superuser": false,
    "username": "user1@example.com",
    "first_name": "",
    "last_name": "",
    "email": "user1@example.com",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2025-07-28T16:31:39Z",
    "is_super_admin": false,
    "groups": [],
    "user_permissions": []
  },
  {
    "id": 4,
    "last_login": null,
    "is_superuser": false,
    "username": "user2",
    "first_name": "",
    "last_name": "",
    "email": "user2@example.com",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2025-07-28T16:31:44.515962Z",
    "is_super_admin": false,
    "groups": [],
    "user_permissions": []
  },
  ....
  {
    "id": 12,
    "last_login": null,
    "is_superuser": false,
    "username": "user10",
    "first_name": "",
    "last_name": "",
    "email": "user10@example.com",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2025-07-28T16:32:24.242499Z",
    "is_super_admin": false,
    "groups": [],
    "user_permissions": []
  }
]
Dashboard.jsx:
http://127.0.0.1:8000/api/user/permissions/
[
  {
    "id": 1,
    "page": "products",
    "access": "view",
    "user": 3
  },
  {
    "id": 2,
    "page": "marketing",
    "access": "edit",
    "user": 4
  }
]

redirect: http://localhost:3000/page/products

DynamicPage.jsx:
http://127.0.0.1:8000/api/comment/comments/
code filter by product name as page = products

http://127.0.0.1:8000/api/user/permissions/
[
  {
    "id": 1,
    "page": "products",
    "access": "view",
    "user": 3
  },
  {
    "id": 2,
    "page": "marketing",
    "access": "edit",
    "user": 4
  }
]
res.data.filter(p => p.user === userId && p.page === pageName)

http://127.0.0.1:8000/api/comment/history/
[]

http://127.0.0.1:8000/api/comment/comments/
[
  {
    "id": 1,
    "page": "products",
    "text": "Comment for user1@example.com",
    "created_at": "2025-07-28T19:23:35.605248Z",
    "modified_at": "2025-07-28T19:23:35.605248Z",
    "user": 3
  }
]

Admin.jsx:
fetchUsers: http://127.0.0.1:8000/api/user/users/
[
  {
    "id": 1,
    "last_login": null,
    "is_superuser": true,
    "username": "admin",
    "first_name": "",
    "last_name": "",
    "email": "admin@gmail.com",
    "is_staff": true,
    "is_active": true,
    "date_joined": "2025-07-28T15:56:18.254931Z",
    "is_super_admin": false,
    "groups": [],
    "user_permissions": []
  },
  ......]

fetchPermissions: http://127.0.0.1:8000/api/user/permissions/
[
  {
    "id": 1,
    "page": "products",
    "access": "view",
    "user": 3
  },
  {
    "id": 2,
    "page": "marketing",
    "access": "edit",
    "user": 4
  },
  {
    "id": 3,
    "page": "orders",
    "access": "view",
    "user": 5
  }
]
togglePermission:
 await api.delete(`/user/permissions/${match.id}/`);
 await api.post('/user/permissions/', { user: userId, page, access });
POST: http://127.0.0.1:8000/api/user/permissions 
 {
  "user": "3",
  "page": "products",
  "access":"edit"
}
â€¢	If .env changes are not reflected, restart the server after editing the .env file.