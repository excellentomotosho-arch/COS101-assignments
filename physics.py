
# PHYSICS CALCULATOR

# Function 1: Calculate Speed
def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    if time == 0:
        print("Time cannot be zero.")
    else:
        print("Speed =", distance / time, "m/s")


# Function 2: Calculate Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))
    print("Force =", mass * acceleration, "N")


# Function 3: Calculate Weight
def weight():
    mass = float(input("Enter mass (kg): "))
    gravity = 9.8
    print("Weight =", mass * gravity, "N")


# Function 4: Calculate Density
def density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))
    if volume == 0:
        print("Volume cannot be zero.")
    else:
        print("Density =", mass / volume, "kg/m³")


# Function 5: Calculate Work Done
def work_done():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    print("Work Done =", force_value * distance, "J")


# Main Program
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed")
    print("2. Force")
    print("3. Weight")
    print("4. Density")
    print("5. Work Done")

    choice = input("Choose a physics operation (1-5): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
    elif choice == "3":
        weight()
    elif choice == "4":
        density()
    elif choice == "5":
        work_done()
    else:
        print("Invalid choice!")

    answer = input("\nDo you want to continue? (yes/no): ").lower()

    if answer != "yes":
        print("Thank you for using the Physics Calculator!")
        break
