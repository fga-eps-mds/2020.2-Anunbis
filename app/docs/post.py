from . import authorization_header

tags = ["Post's paths"]

post_list_post = {
    "summary": "This path is responsable for " "registering a post about a professor",
    "description": "It requires the authorization header "
    "and the post's informations",
    "tags": tags,
    "parameters": [
        authorization_header,
        {
            "in": "body",
            "name": "Post informations",
            "required": True,
            "description": (
                "It needs to be given a students' registration, "
                "professor's identification, discipline code, content, "
                "didactic, metod, avaliations, disponibility and "
                "if it is anonymous, to be able to make this method "
                "work and register a post in the plataform."
            ),
            "schema": {
                "properties": {
                    "reg_student": {
                        "type": "integer",
                    },
                    "id_professor": {
                        "type": "integer",
                    },
                    "discipline_code": {"type": "string"},
                    "content": {
                        "type": "string",
                    },
                    "metod": {
                        "type": "integer",
                    },
                    "avaliations": {
                        "type": "integer",
                    },
                    "disponibility": {
                        "type": "integer",
                    },
                    "didactic": {
                        "type": "integer",
                    },
                    "is_anonymous": {
                        "type": "boolean",
                    },
                },
            },
        },
    ],
    "responses": {
        "201": {"description": "Post successfully added"},
        "400": {"description": "Validation Error"},
        "404": {"description": "Professor, Student or discipline not found"},
    },
}

post_list_get = {
    "summary": "This path is responsable for obtaining"
    " the list of posts related to the user",
    "description": "This method only requires the authorization header ",
    "tags": tags,
    "parameters": [authorization_header],
    "responses": {
        "200": {
            "description": "It will return all the posts related"
            " to the user, if there's any"
        },
    },
}

post_list_postAgree = {
    "summary": "This path is responsable for registering "
    "an agree in an existed post",
    "tags": tags,
    "description": "It only needs the post's id to be able "
    "to make this method work and agree in a post from"
    " the plataform.",
    "parameters": [
        authorization_header,
        {
            "in": "body",
            "name": "Register an agree in a post that already exists",
            "description": "It only needs the post's id",
            "schema": {
                "properties": {
                    "id_post": {"type": "integer"},
                }
            },
        },
    ],
    "responses": {
        "200": {"description": "The post agreed will be returned"},
        "400": {"description": "Validation Error"},
        "404": {"description": "Post not found"},
    },
}

post_list_postDisagree = {
    "summary": "This path is responsable for registering "
    "an disagree in an existed post",
    "tags": tags,
    "description": "It only needs the post's id to be able "
    "to make this method work and disagree in a post from"
    " the plataform.",
    "parameters": [
        authorization_header,
        {
            "in": "body",
            "name": "Register an disagree in a post that already exists",
            "description": "It only needs the post's id. ",
            "schema": {
                "properties": {
                    "id_post": {"type": "integer"},
                }
            },
        },
    ],
    "responses": {
        "200": {"description": "The post disagreed will be returned"},
        "400": {"description": "Validation Error"},
        "404": {"description": "Post not found"},
    },
}
