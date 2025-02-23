import pyrebase
import json
import re 

class AuthModel:
    def __init__(self):
        with open("firebase_config.json") as f:
            self.config = json.load(f)
        self.firebase = pyrebase.initialize_app(self.config)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()  # Use Realtime Database

    def login(self, email, password):
        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            return user
        except Exception as e:
            return str(e)

    def register(self, email, password, first_name, last_name, dob, gender):
        # Email validation using regex
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if not re.match(email_regex, email):
            return "Invalid email format"

        # Password validation (minimum 6 characters)
        if len(password) < 6:
            return "Password must be at least 6 characters long"

        try:
            # Create the user in Firebase Authentication
            user = self.auth.create_user_with_email_and_password(email, password)
            
            # Prepare the user data to store in Realtime Database
            user_data = {
                "first_name": first_name,
                "last_name": last_name,
                "dob": dob,
                "gender": gender,
                "email": email  # Optionally store the email in the Realtime Database as well
            }

            # Use the user's UID to store the data under their unique path in Realtime Database
            self.db.child("users").child(user['localId']).set(user_data)

            return "Registration Successful"
        except Exception as e:
            # Print the full error message to help debug
            print("Error occurred:", e)
            return f"Registration Failed: {str(e)}"
        
    def get_user_id_by_email(self, email):
        """Retrieve the user ID (UID) associated with the given email from Firebase Realtime Database."""
        try:
            users = self.db.child("users").get()
            if users.each():
                for user in users.each():
                    user_data = user.val()
                    if "email" in user_data and user_data["email"] == email:
                        return user.key()  # Return the user UID

            return "User not found"

        except Exception as e:
            return f"Error: {str(e)}"
