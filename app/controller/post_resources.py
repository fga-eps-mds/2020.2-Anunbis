from flask_restful import Resource
from flask import request, make_response, jsonify
from ..schemas import post_schema
from ..services import post_services
from flask_jwt_extended import current_user, jwt_required
from ..ext.auth import student_required
from marshmallow import ValidationError


class PostList(Resource):
    @student_required()
    def post(self):
        """
        This path is responsable for registering a post about a professor
        ---
        tags:
        - Post's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        - in: body
          name: Register a post from student
          description:  It needs to be given a students' registration, professor's identification,
             discipline code, content, didactic, metod, avaliations, disponibility and
             if it is anonymous, to be able to make this method work and register a post in the plataform.
          schema:
                type: object
                required:
                    - reg_student
                    - id_professor
                    - discipline_code
                    - content
                    - didactic
                    - metod
                    - avaliations
                    - disponibility
                    - is_anonymous
                properties:
                    reg_student:
                        type: integer
                    id_professor:
                        type: integer
                    discipline_code:
                        type: string
                    content:
                        type: string
                    didactic:
                        type: integer
                    metod:
                        type: integer
                    avaliations:
                        type: integer
                    disponibility:
                        type: integer
                    is_anonymous:
                        type: boolean
        responses:
            201:
                description: Post successfully added

            400:
                description: Validation Error

            404:
                description: Professor or discipline not found


        """
        ps = post_schema.PostSchema(exclude=["id_post"])
        post = ps.load(request.json)
        if post.get("reg_student") != current_user.reg_student:
            raise ValidationError(
                {"reg_student": "Your reg_student is different to" " post.reg_student"}
            )
        message, status_code = post_services.register_post(post)
        return make_response(jsonify(message), status_code)

    @jwt_required()
    def get(self):
        """
        This path is responsable for obtaining the list of posts related to the user
        ---
        tags:
        - Post's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true

        responses:
            200:
                description: It will return all the posts related to the user, if there's any

        """
        user = current_user
        if not user.is_professor():
            ps = post_schema.PostSchema(
                many=True, context={"reg_student": user.reg})
        else:
            ps = post_schema.PostSchema(many=True)
        return make_response(ps.jsonify(user.posts), 200)


class PostAgreesList(Resource):
    @student_required()
    def post(self):


<< << << < HEAD
        student = current_user
        ps = post_schema.PostSchema(only=["id_post"])
        id = ps.load(request.json).get("id_post")
        post, status_code = post_services.agree_student_post(student, id)
        if status_code == 200:
            ps = post_schema.PostSchema(
                context={"reg_student": student.reg_student})
            return make_response(ps.jsonify(post), status_code)
        else:
            return make_response(jsonify(post), status_code)
== == == =
        """
        This path is responsable for registering an agree in an existed post
        ---
        tags:
        - Post's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        - in: body
          name: Register an agree in a post that already exists
          description:  It only needs the post's id to be able to make this method work and
           agree in the post of another student in the plataform.
          schema:
                type: object
                required:
                    - id_post
                properties:
                    id_post:
                        type: integer
        responses:
            200:
                description: The post agreed will be returned

            400:
                description: Validation Error

            404:
                description: Post not found

        """
        try:
            student = current_user
            ps = post_schema.PostSchema(only=["id_post"])
            id = ps.load(request.json).get("id_post")
            post, status_code = post_services.agree_student_post(student, id)
            if status_code == 200:
                ps = post_schema.PostSchema(
                    context={"reg_student": student.reg_student}
                )
                return make_response(ps.jsonify(post), status_code)
            else:
                return make_response(jsonify(post), status_code)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)
>>>>>> > 81d667a((  # 204)Adicionando docstring dos metodos de post)


class PostDisagreesList(Resource):
    @ student_required()
    def post(self):
<< << << < HEAD
        student=current_user
        ps=post_schema.PostSchema(only=["id_post"])
        id=ps.load(request.json).get("id_post")
        post, status_code=post_services.disagree_student_post(student, id)
        if status_code == 404:
            return make_response(jsonify(post), status_code)
        else:
            ps=post_schema.PostSchema(
                context={"reg_student": student.reg_student})
            return make_response(ps.jsonify(post), status_code)
== == == =
        """
        This path is responsable for registering a disagree in an existed post
        ---
        tags:
        - Post's paths
        parameters:
        - in: header
          name: authorization
          type: string
          required: true
        - in: body
          name: Register a disagree in a post that already exists
          description:  It only needs the post's id to be able to make this method work and
           disagree in the post of another student in the plataform.
          schema:
                type: object
                required:
                    - id_post
                properties:
                    id_post:
                        type: integer
        responses:
            200:
                description: The post disagreed will be returned

            400:
                description: Validation Error

            404:
                description: Post not found

        """
        try:
            student=current_user
            ps=post_schema.PostSchema(only=["id_post"])
            id=ps.load(request.json).get("id_post")
            post, status_code=post_services.disagree_student_post(student, id)
            if status_code == 404:
                return make_response(jsonify(post), status_code)
            else:
                ps=post_schema.PostSchema(
                    context={"reg_student": student.reg_student}
                )
                return make_response(ps.jsonify(post), status_code)
        except ValidationError as err:
            return make_response(jsonify(err.messages), 400)


def configure(api):
    api.add_resource(PostList, "post")
    api.add_resource(PostAgreesList, "post/agree")
    api.add_resource(PostDisagreesList, "post/disagree")
