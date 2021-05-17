tags = ["Login's paths"]

login_list_post = {
    "summary": "This path is responsable for login",
    "tags": tags,
    "parameters": [
        {
            "in": "body",
            "name": "User's login",
            "required": True,
            "description": (
                "It must have already successfuly registered a user "
                "for then be able to make login. "
                "Although, it needs to be given an email and password "
                "to successfully login in the plataform."
            ),
            "schema": {
                "properties": {
                    "email": {
                        "type": "string",
                    },
                    "password": {"type": "string"},
                },
            },
        }
    ],
    "responses": {
        "200": {
            "description": "It returns the information of the user and the access token"
        },
        "400": {"description": "Validation Error"},
        "401": {"description": "Email or password invalid"},
    },
}
