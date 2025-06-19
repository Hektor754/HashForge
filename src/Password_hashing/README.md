# Password Hashing

This project demonstrates a basic password hashing mechanism in Python using the `hashlib` library. It stores a hashed password securely and verifies user input against the stored hash.

## Project Structure

```
password_hashing/
│
├── file_one.py          # Hashes and stores the password
├── store_password.txt   # Stores the hashed password (auto-generated)
├── file_three.py        # Verifies user password against stored hash
```

## How It Works

* `file_one.py`:

  * Prompts the user to enter a password.
  * Hashes the password using `PBKDF2 HMAC` with SHA-256 and 100,000 iterations.
  * Saves the hashed password (in hexadecimal format) to `store_password.txt`.

* `file_three.py`:

  * Reads the stored hashed password from `store_password.txt`.
  * Prompts the user to input a password.
  * Hashes the input password using the same hashing parameters.
  * Compares the newly hashed password with the stored hash to verify correctness.

## Usage

1. Run `file_one.py` to hash and store your password:

   ```bash
   python file_one.py
   ```

2. Run `file_three.py` to verify a password against the stored hash:

   ```bash
   python file_three.py
   ```

## Dependencies

* Python 3.x
* Standard library (`hashlib`, `os`)

## Notes

* The salt used is an empty byte string (`b''`), which is insecure in real-world applications.
* For improved security, use a proper, random salt and store it alongside the hash.
