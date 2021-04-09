from unittest import TestCase
from app.app import create_app


class TestFlaskBase(TestCase):
    def setUp(self):
        """ Start before all tests """
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"    # This create a in-memory sqlite db
        self.app.db.create_all()

    def tearDown(self):
        """ Start after all tests """
        self.app.db.drop_all()



