# Regular Expression (RegEx) Introduction
import re
message = "The current Python version is 3.13. Other previous versions are 3.12, 3.11, 3.10"

# If python is present in message
print("Python" in message)
print("13" in message)
print("14" in message)

print(message.find("3.13"))
print(message.find("Python"))

"""
re.search(regex_pattern)
"""

