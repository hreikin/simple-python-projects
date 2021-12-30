# Start with your work from "admin.py". Store the classes User, Privileges and 
# Admin in one module. Create a separate file, make an Admin instance, and call 
# show_privileges() to show that everything is working correctly.

import imported_admin_module

admin_user = imported_admin_module.Admin("Super", "User", 33, "Everywhere")
admin_user.describe_user()
admin_user.privileges.show_privileges()

print("Adding privileges.")
new_privileges = ["can add post", "can delete post" , "can ban user"]
admin_user.privileges.privileges = new_privileges
admin_user.privileges.show_privileges()