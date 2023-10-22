# Hashing and Salting Hobby Project

This Python code repository is a hobby project created to explore the concepts of hashing and salting in Python. It demonstrates how to hash sensitive information, such as passwords, using the SHA-256 algorithm and the application of salts for added security.

## Motivation

The primary motivation behind this project is to gain a deeper understanding of cryptographic techniques used in password security. Hashing and salting are fundamental concepts in cybersecurity and are essential for protecting user credentials and sensitive data in applications.

## Functionality

- Hashing passwords using SHA-256: This code demonstrates how to generate a SHA-256 hash from a given password.
- Adding custom salts: You can provide a custom salt to enhance the security of the hashed password.
- Writing to a CSV file: The code also includes an example of how to write data (hashed passwords) to a CSV file.

## Best Practices
1. Do not store anything in plaintext.
2. Encrypting is good as long as the decryption key is not on the same server or network that is being attacked.
3. Hashing is good as it prevents any third party or even the developer from guessing the password, assuming everything else is encrypted, hashed, and obfuscated.
4. Hashing and salting makes it much harder to brute force.
5. You can use sha512 which makes it even harder. `hashlib.sha512()`
6. Use bcrypt instead of whatever I'm using. Bcrypt handles the salting and the work factor can be adjusted so any password will take exponential time to crack. Higher work factor means hashing process will be slower to generate, make it high enough and you will witness the heat death of the universe before you get the hash. Something fun to read for you nerds: https://stackoverflow.com/questions/4443476/optimal-bcrypt-work-factor
