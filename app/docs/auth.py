tags = ["Auth's paths"]

login_list_post = {
    "summary": "This path is responsable for login",
    "tags": tags,
    "description": "It must have already successfuly registered a user "
    "for then be able to login. ",
    "parameters": [
        {
            "in": "body",
            "name": "User's login",
            "required": True,
            "description": (
                "It needs to be given an email and password "
                "to successfully login in the plataform."
            ),
            "schema": {
                "properties": {
                    "email": {"type": "string"},
                    "password": {"type": "string"},
                },
            },
        }
    ],
    "responses": {
        "200": {
            "description": "It returns the information"
            " of the user and the access token"
        },
        "400": {"description": "Validation Error"},
        "401": {"description": "Email or password invalid"},
    },
}

email_verify_get = {
    "summary": "This path is responsable for activate user's account",
    "tags": tags,
    "description": "Active user's account using the token sended in e-mail",
    "parameters": [
        {
            "in": "query",
            "name": "token",
            "required": True,
            "description": "Token sended in confirmation e-mail",
        }
    ],
    "responses": {
        "302": {"description": "Account actived successfully. Redirects to frontend"},
        "400": {"description": "Token expired or invalid"},
    },
}

email_verify_post = {
    "summary": "This path is responsable for resend the confirmation e-mail",
    "tags": tags,
    "description": "Resend confirmation e-mail",
    "parameters": [
        {
            "in": "body",
            "name": "User's e-mail",
            "required": True,
            "description": "User's e-mail",
            "schema": {
                "properties": {"email": {"type": "string"}},
            },
        }
    ],
    "responses": {
        "200": {"description": "Email resent successfully"},
        "203": {"description": "User already actived"},
        "400": {"description": "Validation Error"},
        "404": {"description": "User not found"},
    },
}
