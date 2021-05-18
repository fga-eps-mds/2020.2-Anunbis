from . import authorization_header

tags = ["Report's paths"]


report_post = {
    "summary": "This path is responsable for registering a report",
    "tags": tags,
    "description": "It needs to be given the"
    " authorization header to validate the user and the report's values",
    "parameters": [
        authorization_header,
        {
            "in": "body",
            "name": "Register a report",
            "description": "It requires the"
            " written content, an id_post, and give a true or"
            " false for the variables offensive, prejudice, "
            "unrelated and others",
            "schema": {
                "properties": {
                    "id_post": {"type": "integer"},
                    "offensive": {"type": "boolean"},
                    "prejudice": {"type": "boolean"},
                    "unrelated": {"type": "boolean"},
                    "others": {"type": "boolean"},
                    "content": {"type": "string"},
                },
            },
        },
    ],
    "responses": {
        "201": {"description": "Report successfully added"},
        "400": {"description": "Validation Error"},
        "404": {"description": "Course not found"},
    },
}
