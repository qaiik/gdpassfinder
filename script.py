import gd

db = gd.api.save.load()

print("Username: " + db.get_user_name())
print("Password: " + db.get_password())
