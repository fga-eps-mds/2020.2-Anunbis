from . import authorization_header

tags = ["Student's paths"]


student_post = {
    "summary": "This path is responsable for" " registering a student",
    "description": "It doesn't required an authorization"
    " header, only the student's attributes",
    "tags": tags,
    "parameters": [
        {
            "in": "body",
            "name": "Register a studant",
            "description": "It needs to be given a name, email, "
            "student's registration, course's identification "
            "and a password",
            "schema": {
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "reg_student": {"type": "integer"},
                    "id_course": {"type": "integer"},
                    "password": {"type": "string"},
                },
            },
        }
    ],
    "responses": {
        "201": {"description": "Student successfully registered"},
        "400": {"description": "Validation Error"},
        "404": {"description": "Course not found"},
        "409": {"description": "Student already registered"},
    },
}

student_put = {
    "summary": "This path is responsable for" " modfying the student's password",
    "tags": tags,
    "description": "It needs to be given the "
    "authorization header to validate the user"
    ", and the new password to be able to"
    " modify the old one.",
    "parameters": [
        authorization_header,
        {
            "in": "body",
            "name": "Modify student's password",
            "description": "Requires a new password",
            "schema": {
                "properties": {
                    "password": {"type": "string"},
                },
            },
        },
    ],
    "responses": {
        "200": {"description": "Student successfully changed"},
        "400": {"description": "Validation Error"},
        "401": {"description": "Missing Authorization Header"},
    },
}

student_delete = {
    "summary": "This path is responsable for deleting the student's account",
    "tags": tags,
    "description": "It only needs to be given the authorization header"
    " to validate the user and delete the student's account.",
    "parameters": [authorization_header],
    "responses": {
        "204": {"description": "Nothing will be displayed"},
    },
}
