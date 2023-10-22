import csv
import hashlib
import os

FILE_NAME_10K_MOST_COMMON_PASSWORDS = "10k-most-common_passwords.txt"
FILE_NAME_10K_MOST_COMMON_PASSWORDS_HASHED = "10k-most-common_passwords_hashed.csv"


def get_sha256_hash_password(password) -> str:
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256(password.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_password = sha256.hexdigest()

    return hashed_password


# Yes, I know you can you make it into one function and just have an optional parameter.
def get_sha256_hash_password_with_salt(password: str, salt: str) -> str:
    # Append salt to password, then encode as bytes
    password_w_salt = f"{password}{salt}".encode('utf-8')

    sha256 = hashlib.sha256(password_w_salt)

    # Get the hexadecimal representation of the hash and salt
    hashed_password = sha256.hexdigest()

    return hashed_password


def does_sha256_match_password(sha256: str, password: str) -> bool:
    hash = get_sha256_hash_password(password)
    if hash == sha256:
        return True
    return False


# Yes, I know you can you make it into one function and just have an optional parameter.
def does_sha256_match_password_and_salt(sha256: str, password: str, salt: str) -> bool:
    hash = get_sha256_hash_password_with_salt(password, salt)
    if hash == sha256:
        return True
    return False


def read_file_into_list(filename: str) -> list[str]:
    lines = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                lines.append(line.strip())  # Remove newline characters and add to the list
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines


def generate_csv_of_common_hashes(data: dict, filename: str) -> None:
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            for key in data.keys():
                writer.writerow([key, data[key]])
        print(f'Data has been written to {filename}')
    except Exception as e:
        print(f"An error occurred: {e}")


def get_dict_with_common_password_hashes() -> dict:
    passwords = read_file_into_list(FILE_NAME_10K_MOST_COMMON_PASSWORDS)
    dict_hash = {}

    for password in passwords:
        dict_hash[password] = get_sha256_hash_password(password)

    return dict_hash


if __name__  == "__main__":
    # Variables
    print('\n--------------')
    password = "enter_pass_word_here"
    custom_salt = "your_custom_salt_string"

    # Ultimately what you want to store it the database to be compared.
    hashed_password = get_sha256_hash_password(password)
    hashed_password_w_salt = get_sha256_hash_password_with_salt(password, custom_salt)

    ### Usages: Print out sha256 and sha256 with a salt
    # print(f'sha256: {get_sha256_hash_password(password)}')
    # print(f"sha256 with salt: '{custom_salt}':{get_sha256_hash_password_with_salt(password, custom_salt)}")

    ### Usages: Compare a hash password with and without a salt. Obvisouly these values would be true as I didn't change the parameters.
    # print(does_sha256_match_password(hashed_password, password))
    # print(does_sha256_match_password_and_salt(hashed_password_w_salt, password, custom_salt))
    
    ### Usages: This generate a csv file by reading in the 10k txt with the most common passwords and generate the hash and output to a csv.
    generate_csv_of_common_hashes(get_dict_with_common_password_hashes(), FILE_NAME_10K_MOST_COMMON_PASSWORDS_HASHED)
    

