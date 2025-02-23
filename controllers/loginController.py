from models.authModel import AuthModel

class LoginController:
    def __init__(self):
        self.model = AuthModel()

    def login(self, email, password):
        response = self.model.login(email, password)
        if isinstance(response, dict):
            return "Login Successful"
        return "Login Failed: " + response

    def register(self, email, password, first_name, last_name, dob, gender):
        response = self.model.register(email, password, first_name, last_name, dob, gender)
        if isinstance(response, dict):
            return "Registration Successful"
        return "Registration Message: " + response
