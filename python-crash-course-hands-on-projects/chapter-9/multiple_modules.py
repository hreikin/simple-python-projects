# Store the User class in one module, and store the Privileges and Admin classes 
# in a separate module. In a separate file, create an Admin instance and call 
# show_privileges() to show that everything is still working correctly.

import multiple_modules_admin

admin_user = multiple_modules_admin.Admin("Super", "User", 33, "Everywhere")
admin_user.describe_user()
admin_user.privileges.show_privileges()

print("Adding privileges.")
new_privileges = ["can add post", "can delete post" , "can ban user"]
admin_user.privileges.privileges = new_privileges
admin_user.privileges.show_privileges()