import bcrypt


# Function to hash a password
def hash_password(password):
    print("password: ", "[",password,"]")
    # Generate a salt
    salt = bcrypt.gensalt()
    print("salt : " "[",salt,"]")
    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


# Function to check if the password matches the stored hash
def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)


# Example usage
if __name__ == "__main__":
    # Original password
    original_password = "sha123##"

    # Hash the password
    hashed = hash_password(original_password)
    print(f"Hashed Password: {hashed}")

    # Check if the password is correct
    password_is_correct = check_password("mysecretpassword", hashed)
    print(f"Password Match: {password_is_correct}")

    # Check if a wrong password is correct
    wrong_password_check = check_password("wrongpassword", hashed)
    print(f"Wrong Password Match: {wrong_password_check}")
