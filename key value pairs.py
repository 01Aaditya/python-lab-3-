def student_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling with at least three named arguments
student_profile(name="John", age=17, grade="11th")
