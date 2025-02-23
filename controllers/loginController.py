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
    
    def get_user_id(self, user_id):
        return self.read_dp.get_user_id(user_id)
    
    def get_password(self, user_id):
        return self.read_dp.get_password(user_id)
    
    def get_user_id_by_email(self,email):       
        user = self.read_dp.get_user_by_email(email)
        return user.uid
       