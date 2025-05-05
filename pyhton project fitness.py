# Define a dictionary to store user data
users = {}

# Define a set to store available exercises
exercises = set()

# Define a function to load data from a file
def load_data():
    try:
        with open("fitness_data.txt", "r") as file:
            data = eval(file.read())
            users.update(data.get("users", {}))
            exercises.update(data.get("exercises", []))
    except FileNotFoundError:
        print("No existing data file found. Creating a new one.")

# Define a function to save data to a file
def save_data():
    try:
        data = {
            "users": users,
            "exercises": list(exercises)
        }
        with open("fitness_data.txt", "w") as file:
            file.write(str(data))
    except Exception as e:
        print(f"Error saving data: {e}")

# Define a function to register a new user
def register_user():
    name = input("Enter your name: ")
    if name in users:
        print("User already exists.")
    else:
        age = input("Enter your age: ")
        weight = input("Enter your weight (in kg): ")
        height = input("Enter your height (in cm): ")
        users[name] = {
            "age": int(age),
            "weight": float(weight),
            "height": float(height),
            "activities": []
        }
        print("User registered successfully.")

# Define a function to log an activity
def log_activity():
    name = input("Enter your name: ")
    if name not in users:
        print("User not found. Please register first.")
        return

    activity = input("Enter the activity (e.g., running, cycling, swimming): ")
    duration = input("Enter the duration (in minutes): ")
    distance = input("Enter the distance (in km): ")
    users[name]["activities"].append({
        "activity": activity,
        "duration": int(duration),
        "distance": float(distance)
    })
    print("Activity logged successfully.")

    if activity not in exercises:
        exercises.add(activity)

# Define a function to view user activities
def view_activities():
    name = input("Enter your name: ")
    if name not in users:
        print("User not found.")
        return

    user_activities = users[name]["activities"]
    if not user_activities:
        print("No activities logged yet.")
    else:
        print(f"Activities for {name}:")
        for activity in user_activities:
            print(f"Activity: {activity['activity']}, Duration: {activity['duration']} minutes, Distance: {activity['distance']} km")

# Load existing data from the file
load_data()

# Main program loop
while True:
    print("\nFitness Tracker")
    print("1. Register User")
    print("2. Log Activity")
    print("3. View Activities")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            register_user()
        elif choice == 2:
            log_activity()
        elif choice == 3:
            view_activities()
        elif choice == 4:
            save_data()
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")