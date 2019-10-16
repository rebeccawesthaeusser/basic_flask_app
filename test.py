import unittest
from flask import Flask
import app
import database_logic_pymongo
#TODO: write tests for routes

invalid_username = 'Anna'
valid_username = 'Thomas'

def create_app():
    my_app = Flask(__name__)
    my_app.config['TESTING'] = True
    return app

class TemplateTests(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_about(self):
        rv = self.app.get('/about')
        self.assertEqual(rv.status, '200 OK')

    def test_database_action_search(self):
        rv = self.app.get('/database_action_search')
        self.assertEqual(rv.status, '200 OK')

    '''
    def test_database_action_add(self):
        rv = self.app.get('/database_action_add')
        self.assertEqual(rv.status, '200 OK')

    def test_database_action_delete(self):
        rv = self.app.get('/database_action_delete')
        self.assertEqual(rv.status, '200 OK')

    def test_database_action_update(self):
        rv = self.app.get('/database_action_update')
        self.assertEqual(rv.status, '200 OK')
    '''

class DatabaseLogicTests(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_add_valid_user(self):
        database_logic_pymongo.delete_user(valid_username)
        message = database_logic_pymongo.add_user(valid_username)
        expected_message = " has been added."
        self.assertEqual(expected_message, message, "A valid user could not be added.")

    def test_add_valid_user_twice(self):
        message = database_logic_pymongo.add_user(valid_username)
        expected_message = " has already been added."
        self.assertEqual(expected_message, message, "A user was added twice.")

    def test_delete_invalid_user(self):
        message = database_logic_pymongo.delete_user(invalid_username)
        expected_message = " couldn't be deleted."
        self.assertEqual(expected_message, message, "An invalid user was deleted.")

    def test_delete_valid_user(self):
        message = database_logic_pymongo.delete_user(valid_username)
        expected_message = " has been deleted."
        self.assertEqual(message, expected_message, "A valid user cloud not be deleted.")

    def test_find_invalid_user(self):
        message = database_logic_pymongo.find_user(invalid_username)
        expected_message = " can't be found."
        self.assertEqual(expected_message, message, "An invalid user can be found.")

    def test_find_valid_user(self):
        database_logic_pymongo.add_user(valid_username)
        message = database_logic_pymongo.find_user(valid_username)
        expected_message = ""
        self.assertEqual(expected_message, message, "A valid user can't be found.")

    def test_update_invalid_user(self):
        message = database_logic_pymongo.update_user(invalid_username, None)
        expected_message = " can't be found."
        self.assertEqual(expected_message, message, "An invalid user can be found.")

    def test_update_valid_user_no_age(self):
        message = database_logic_pymongo.update_user(valid_username, None)
        expected_message = " hasn't been updated. Please enter the age."
        self.assertEqual(expected_message, message, "A valid user is updated without the age.")

    def test_update_valid_user_with_age(self):
        message = database_logic_pymongo.update_user(valid_username, 33)
        expected_message = " has been updated."
        self.assertEqual(expected_message, message, "A valid user with age can't be updated.")

if __name__ == '__main__':
    unittest.main()
