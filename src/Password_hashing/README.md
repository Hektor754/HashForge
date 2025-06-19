# Password Hashing

This project demonstrates a basic password hashing mechanism in Python using the `hashlib` library. It stores a hashed password securely and verifies user input against the stored hash.

## Project Structure

```
password_hashing/
│
├── main.py          # Hashes and stores the password
├── store_password.txt   # Stores the hashed password (auto-generated)
├── verify_hash.py        # Verifies user password against stored hash
```

## How It Works

* `main.py`:

  * Prompts the user to enter a password.
  * Hashes the password using `PBKDF2 HMAC` with SHA-256 and 100,000 iterations.
  * Saves the hashed password (in hexadecimal format) to `store_password.txt`.

* `verify_hash.py`:

  * Reads the stored hashed password from `store_password.txt`.
  * Prompts the user to input a password.
  * Hashes the input password using the same hashing parameters.
  * Compares the newly hashed password with the stored hash to verify correctness.

## Usage

1. Run `main.py` to hash and store your password:

   ```bash
   python main.py
   ```

2. Run `verify_hash.py` to verify a password against the stored hash:

   ```bash
   python verify_hash.py
   ```

## Dependencies

* Python 3.x
* Standard library (`hashlib`, `os`)

## Notes

* The salt used is an empty byte string (`b''`), which is insecure in real-world applications.
* For improved security, use a proper, random salt and store it alongside the hash.
