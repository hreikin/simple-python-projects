# Start with a copy of the below code. Build a profile of 
# yourself by calling build_profile(), using your first and last names and 
# three other key-value pairs that describe you.
#
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     profile = {}
#
#     profile['first_name'] = first
#     profile['last_name'] = last
#
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile = build_profile('albert', 'einstein',
#                             location='princeton',
#                             field='physics')
# print(user_profile)

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
print(user_profile)

my_profile = build_profile("michael", "haslam",
                            location = "scotland",
                            learning = "python",
                            status = "in-progress")
print(my_profile)
for k, v in my_profile.items():
    print(k.title() + ":", v.title())