def build_profile(first,last,**user_profile):
    user_profile['first_name']=first
    user_profile['last_name']=last
    return user_profile

print(build_profile('hamit','sehjal',type='paper',mango='clips'))
