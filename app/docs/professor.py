from . import authorization_header

tags = ["Professor's paths"]

professor_get_by_name = {
    "summary": "This path is responsable for getting " "the professors by its name.",
    "tags": tags,
    "description": "It needs to be given an "
    "authorization header and part of the professor's name.",
    "parameters": [
        authorization_header,
        {
            "in": "path",
            "name": "name",
            "type": "string",
            "required": "true",
            "description": "It needs to be given the " "professor's part of the name.",
        },
    ],
    "responses": {
        "200": {
            "description": "It will return all the professors that have "
            "part of the given name, if there's any"
        },
        "400": {"description": "Validation Error"},
    },
}


professor_get_by_id = {
    "summary": "This path is responsable " "for getting a professor by its id",
    "tags": tags,
    "description": "It needs to be given an authorization"
    " header and the professor's id.",
    "parameters": [
        authorization_header,
        {
            "in": "path",
            "name": "id",
            "type": "integer",
            "required": "true",
            "description": "It needs to be given the " "professor's id.",
        },
    ],
    "responses": {
        "200": {
            "description": " It will return the professor's"
            " information by the id, if there's any"
        },
    },
}

professor_post = {
    "summary": "This path is responsable for" " registering a professor",
    "tags": tags,
    "description": "It doesn't require an authorization header.",
    "parameters": [
        {
            "in": "body",
            "name": "Register a professor",
            "description": "It needs to be given a name, email, professor's "
            "registration, and a password to make this method"
            " work and register a professor in the plataform.",
            "schema": {
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "reg_professor": {"type": "integer"},
                    "password": {"type": "string"},
                },
            },
        },
    ],
    "responses": {
        "201": {"description": "Professor successfully registered"},
        "400": {"description": "Validation Error"},
        "409": {"description": "This professor is already registered"},
    },
}

professor_put = {
    "summary": "This path is responsable" " for modfying the professor's password",
    "tags": tags,
    "description": "It needs to be given the"
    " authorization header to validate the user"
    ", and the new password to be able to modify the old one.",
    "parameters": [
        authorization_header,
        {
            "in": "body",
            "name": "Modify professor's password",
            "description": ("It requires the new password."),
            "schema": {
                "properties": {
                    "password": {"type": "string"},
                },
            },
        },
    ],
    "responses": {
        "200": {"description": "Professor password successfully changed"},
        "400": {"description": "Validation Error"},
        "401": {"description": "Missing Authorization Header"},
    },
}

professor_delete = {
    "summary": "This path is responsable for deleting" " the professor's account",
    "tags": tags,
    "description": "Only the header is needed to delete " "the professor's account",
    "parameters": [
        authorization_header,
    ],
    "responses": {
        "204": {"description": "Nothing will be displayed"},
    },
}
