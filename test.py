import unittest
from FlaskLogin import app

class TestLogin(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client before each test."""
        app.config["TESTING"] = True  
        self.client = app.test_client()

    def test_login_dendyprtha(self):
        response = self.client.post("/login", data={"username": "dendyprtha", "password": "qwe123"})
        self.assertIn("Welcome back dendyprtha!", response.data.decode())

    def test_login_maria_don_banvard(self):
        response = self.client.post("/login", data={"username": "maria_don_banvard", "password": "mariaD0nB4nV4Rd"})
        self.assertIn("Welcome back maria_don_banvard!", response.data.decode())

    def test_login_john_guilemot(self):
        response = self.client.post("/login", data={"username": "john_guilemot", "password": "JohnGu!l3M0T"})
        self.assertIn("Welcome back john_guilemot!", response.data.decode())

    def test_login_adid_kotelawala(self):
        response = self.client.post("/login", data={"username": "4DidN3Cis", "password": "Ad!N3C1sD4nK3R3n"})
        self.assertIn("Welcome back 4DidN3Cis!", response.data.decode())

    def test_login_invalid_password(self):
        response = self.client.post("/login", data={"username": "dendyprtha", "password": "wrongpassword"})
        self.assertIn("Login Failed! Please check your username & password!", response.data.decode())

    def test_login_invalid_username(self):
        response = self.client.post("/login", data={"username": "unknown_user", "password": "qwe123"})
        self.assertIn("Login Failed! Please check your username & password!", response.data.decode())

    @staticmethod
    def run_tests_with_score():
        """Run all tests, calculate marks, and print the score."""
        suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
        results = unittest.TextTestRunner(verbosity=2).run(suite)

        # Calculate the score
        total_tests = results.testsRun
        failed_tests = len(results.failures) + len(results.errors)
        passed_tests = total_tests - failed_tests

        # Assign equal weight to each test
        marks_per_test = 100 / total_tests
        score = passed_tests * marks_per_test

        # Print the score
        print("\nScore Calculation:")
        print(f"Total Tests: {total_tests}")
        print(f"Passed Tests: {passed_tests}")
        print(f"Failed Tests: {failed_tests}")
        print(f"Final Score: {score:.2f} / 100")

if __name__ == "__main__":
    TestLogin.run_tests_with_score()
