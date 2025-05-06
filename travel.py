# TripPlanner V1.2 (Interactive)

def trip_planner_welcome(name):
    print(f"\nWelcome to TripPlanner v1.2, {name}!\n")

def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    print(f"\nEstimated time entered: {estimated_time} hours")
    print(f"Rounded to nearest hour: {rounded_time} hours\n")
    return rounded_time

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print("Trip Summary:")
    print(f"- Origin: {origin}")
    print(f"- Destination: {destination}")
    print(f"- Mode of Transport: {mode_of_transport}")
    print(f"- Estimated Time: {estimated_time} hours")

def main():
    # Collect user input
    name = input("Enter your name: ")
    trip_planner_welcome(name)

    origin = input("Enter your starting location: ")
    destination = input("Enter your destination: ")
    mode = input("Enter mode of transport (or press Enter for default 'Car'): ") or "Car"

    # Get and validate estimated time input
    while True:
        try:
            time_input = float(input("Enter estimated time in hours (e.g., 3.5): "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Calculate and display results
    rounded_estimate = estimated_time_rounded(time_input)
    destination_setup(origin, destination, rounded_estimate, mode)

if __name__ == "__main__":
    main()
  
