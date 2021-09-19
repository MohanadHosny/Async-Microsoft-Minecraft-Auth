# MsMcAuthAIO
**A python wrapper for xbox minecraft authentication.**

# How to install
```pip3 install msmcauthaio```

# Usage
```python
from msmcauthaio import MsMcAuth, UserProfile

client = MsMcAuth()
login: UserProfile = await client.login("your-email-here", "your-password-here")

# Login is UserProfile object
print(login)
```