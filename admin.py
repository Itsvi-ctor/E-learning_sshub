# Predefined admin credentials
admin_email = "admin@gmail.com"
admin_password = "admin123"

# Existing courses
courses = {
    "CIT401": {"name": "Course Name 401", "materials": []},
    "CIT402": {"name": "Course Name 402", "materials": []},
    # Add other courses similarly
}

# Admin login
def admin_login():
    email = input("Enter admin username/email: ")
    password = input("Enter password: ")

    if email == admin_email and password == admin_password:
        return True
    else:
        print("Access Denied")
        return False

# Show courses for admin
def admin_display_courses():
    print("Courses Available for Upload:")
    for course_code, course_info in courses.items():
        print(f"{course_code}: {course_info['name']}")

# Upload material for a course
def upload_material(course_code):
    if course_code in courses:
        print(f"Uploading material for {course_code}:")
        material_type = input("Enter material type (Video, Course Material, Reading Material, Extra Resources): ")
        material = input("Enter material name: ")
        courses[course_code]["materials"].append({material_type: material})
        print("Material uploaded successfully.")
    else:
        print("Invalid course code.")

# Admin main workflow
def admin_main():
    # Admin login
    while not admin_login():
        pass  # Repeat login until successful
    
    # Once logged in as admin
    admin_display_courses()
    
    # Select course to upload material
    selected_course = input("Enter the course code you want to upload material for: ")
    upload_material(selected_course)
    
    # Admin logout
    print("Logged out as admin.")

# Run admin workflow
if __name__ == "__main__":
    admin_main()
