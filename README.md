# 🔐 Password Strength Checker

A simple Python command-line tool that instantly evaluates password strength against established security criteria, with practical feedback for improvement.

## ✨ Features

- **Precise point-based scoring** (0 to 6) instead of a simple binary rating
- **Comprehensive checks** covering:
  - Password length (8 characters minimum, 12+ recommended)
  - Presence of both uppercase and lowercase letters
  - Presence of digits
  - Presence of special characters
  - Detection of common, well-known passwords (`123456`, `password`, ...)
  - Detection of excessive character repetition (`aaaa1111`)
- **Secure input**: uses `getpass` instead of `input` so the password is never displayed on screen while typing
- **Zero external dependencies** — runs on the Python standard library only

## 📦 Requirements

- Python 3.9 or later

No additional libraries need to be installed.

## 🚀 Usage

```bash
python password_strength_checker.py
```

You'll be prompted to enter a password, and immediately receive a report like:

```
Rating: Good (5/6)
Suggestions to improve your password:
  - Use 12 or more characters for stronger security.
```

## 🧩 Using it as a library

You can also import the core function into another project:

```python
from password_strength_checker import check_password_strength

result = check_password_strength("MyP@ssw0rd123")
print(result.score)   # 6
print(result.label)   # "Very strong"
print(result.issues)  # []
```

## ⚠️ Disclaimer

This tool is intended for personal and educational use in checking your own passwords, and is not a substitute for a properly enforced password policy in production environments.

## 📄 License

MIT
