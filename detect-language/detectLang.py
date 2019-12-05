import detectlanguage

detectlanguage.configuration.api_key = "7e8ac16dc6ab196f2449de5fd7d7f70b"

# Enable secure mode (SSL) if you are passing sensitive data
# detectlanguage.configuration.secure = True


print(detectlanguage.simple_detect("Buenos dias señor"))
print(detectlanguage.detect("سلام گلم"))
print(detectlanguage.detect("Oui"))

detectlanguage.user_status()
