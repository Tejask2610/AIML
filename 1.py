
#motion detected means, the system senses whether someone is present in the room.#

class SmartHomeAgent:
    def __init__(self, target_temp=21.0):
        self.target_temp = target_temp
        self.history = []  # Internal model: stores recent temperature history

    def perceive(self, current_temp, motion_detected):
        # Sensors provide these inputs
        self.history.append(current_temp)

        # Keep only last 3 readings
        if len(self.history) > 3:
            self.history.pop(0)

        return self.decide_action(current_temp, motion_detected)

    def decide_action(self, current_temp, motion_detected):

        # Actuator decisions based on percepts
        if not motion_detected:
            action = "Set AC/Heater to OFF (Energy Saving Mode)"

        elif current_temp > self.target_temp + 1.0:
            action = "Turn ON AC (Cooling)"

        elif current_temp < self.target_temp - 1.0:
            action = "Turn ON Heater (Heating)"

        else:
            action = "Temperature is Optimal. Fan Only."

        return action


print("========= SMART HOME AGENT =========\n")

# User enters desired room temperature
target = float(input("Enter Target Temperature (°C): "))

# Creat Agent
agent = SmartHomeAgent(target_temp=target)

# Number of sensor readings
n = int(input("How many sensor readings do you want to enter? "))

print()

for i in range(n):

    print(f"------ Sensor Reading {i+1} ------")

    current_temp = float(input("Enter Current Temperature (°C): "))

    motion = input("Is Motion Detected? (yes/no): ").strip().lower()

    if motion == "yes":
        motion_detected = True
    else:
        motion_detected = False

    # Agent decides action
    action = agent.perceive(current_temp, motion_detected)

    print("\n------ OUTPUT ------")
    print(f"Sensors -> Temperature : {current_temp}°C")
    print(f"Sensors -> Motion      : {motion_detected}")
    print(f"Actuator -> {action}")

    # Show internal model (history)
    print(f"Internal Model (Last 3 Temps): {agent.history}")
    print()
