# Predefined user credentials
valid_email = "folajimi@gmail.com"
valid_password = "fola123"

# Predefined courses
courses = {
    "CIT401": "Course Overview for CIT401",
    "CIT402": "Course Overview for CIT402",
    "CIT403": "Course Overview for CIT403",
    "CIT404": "Course Overview for CIT404",
    "CIT405": "Course Overview for CIT405",
    "CIT406": "Course Overview for CIT406",
    "CIT407": "Course Overview for CIT407",
    "CIT408": "Course Overview for CIT408",
    "CIT409": "Course Overview for CIT409",
    "CIT410": "Course Overview for CIT410"
}

# Simulating login
def login():
    email = input("Enter username/email: ")
    password = input("Enter password: ")

    if email == valid_email and password == valid_password:
        return True
    else:
        print("Access Denied")
        return False

# Display user's courses
def display_courses():
    print("Your Courses:")
    for course_code in courses:
        print(course_code)

# Course overview
def show_course_overview(course_code):
    if course_code in courses:
        print(f"Course Overview for {course_code}: {courses[course_code]}")
    else:
        print("Invalid course code.")

# Access course content
def access_course_content():
    print("Select the type of course material you want to access:")
    print("1. Course Materials")
    print("2. Videos")
    print("3. Reading Materials")
    print("4. Additional Resources")
    choice = input("Enter your choice (1-4): ")
    
    # Simulating access to different materials
    if choice == "1":
        print("Accessing Course Materials...")
    elif choice == "2":
        print("Accessing Videos...")
    elif choice == "3":
        print("Accessing Reading Materials...")
    elif choice == "4":
        print("Accessing Additional Resources...")
    else:
        print("Invalid choice.")

# Main workflow
def main():
    # Login
    while not login():
        pass  # Repeat login until successful
    
    # Once logged in
    display_courses()
    
    # Select course
    selected_course = input("Enter the course code you want to access: ")
    show_course_overview(selected_course)
    
    # Access course content
    access_course_content()
    
    # Logout
    print("Logged out.")

# Run the main workflow
if __name__ == "__main__":
    main()
