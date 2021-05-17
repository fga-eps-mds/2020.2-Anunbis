from . import authorization_header

tags = ["Post's paths"]

post_list_post = {
    "summary": "This path is responsable for registering a post about a professor",
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
