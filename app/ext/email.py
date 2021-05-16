from flask_mail import Mail, Message
from flask import render_template_string, current_app, url_for


def init_app(app):
    app.mail = Mail(app)


def send_email(title, email_html, recipients):
    msg = Message(title, recipients=recipients)
    msg.html = email_html
    current_app.mail.send(msg)


def send_verify_email(user_db, token):
    title = "Cadastro no Anunbis"
    header_text = "Cadastro Anunbis"
    first_name = user_db.name.split(" ")[0]
    message = (
        f"Bem vindo, {first_name}.<br>"
        "Para confirmar seu cadastro, voce precisa clicar no botão abaixo. "
        "Esse procedimento é importante para sua segurança "
        "e o melhor funcionamento da comunidade."
    )
    footer_text = (
        "Clique no botão abaixo para confirmar seu e-mail."
        "<br>Esse link expirará em 1 dia."
    )
    button_text = "Confirmar email!"
    href_button = current_app.config["ANUNBIS_BACKEND_URI"] + url_for(
        "restapi.emailverifylist", token=token
    )
    email_template = EmailTemplate(
        header_text, message, footer_text, button_text, href_button
    )
    email_html = email_template.get_html()
    send_email(
        title,
        email_html,
        [user_db.email],
    )


class EmailTemplate:
    def __init__(self, header_text, message, footer_text, button_text, href_button):
        with current_app.open_resource("static/email/index.html") as fp:
            self.email_html = fp.read().decode("utf-8").replace("\n", "")
        self.header_text = header_text
        self.message = message
        self.footer_text = footer_text
        self.button_text = button_text
        self.href_button = href_button

    def get_html(self):
        return render_template_string(
            self.email_html,
            header_text=self.header_text,
            main_text=self.message,
            footer_text=self.footer_text,
            button_text=self.button_text,
            href_button=self.href_button,
        )
