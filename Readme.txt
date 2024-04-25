Following are the API Paths tot test

Below APIs are protected thus requires you generate a Token to authenticate your request

http://127.0.0.1:8000/api/menu/
http://127.0.0.1:8000/api/menu/1/
http://127.0.0.1:8000/api/booking/
http://127.0.0.1:8000/api/booking/1/

User authentication

http://127.0.0.1:8000/auth/users/   (using the POST method create user by entering details in JSON format)
http://127.0.0.1:8000/auth/token/login/ (using the POST method enter user details in JSON format to generate token)
