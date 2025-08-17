# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

# setting up variables
green_light_duration = [30, 45]
red_light_duration = 25
yellow_light_duration = 5

# Vehicles (For now only cars)
vehicle_arrival_rate_ns = 4 # Average cars arriving in North South direction per minute (Poisson)
vehicle_arrival_rate_ew = 6 # Average cars arriving in East West direction per minute (Poisson)

# Random circumstances
pedestrian_delay_prob = 0.1
malfunction_prob = 0.05 

# Traffic Flow iterations
total_iterations = 1000

def traffic_flow_simulation():  # Function to simulate a single run of a traffic light
    north_queue, south_queue, east_queue, west_queue = 0, 0, 0, 0 

    for _ in range(total_iterations):
        # Generate random arrival of cars (Poisson distribution)
        north_queue += np.random.poisson(vehicle_arrival_rate_ns)
        south_queue += np.random.poisson(vehicle_arrival_rate_ns)
        east_queue += np.random.poisson(vehicle_arrival_rate_ew)
        west_queue += np.random.poisson(vehicle_arrival_rate_ew)

        north_arrival = np.random.poisson(vehicle_arrival_rate_ns)
        south_arrival = np.random.poisson(vehicle_arrival_rate_ns)
        east_arrival = np.random.poisson(vehicle_arrival_rate_ew)
        west_arrival = np.random.poisson(vehicle_arrival_rate_ew)

        north_queue += north_arrival
        south_queue += south_arrival
        east_queue += east_arrival
        west_queue += west_arrival

        # Randomly set the green light duration for NS and EW directions
        green_time_ns = random.randint(green_light_duration[0], green_light_duration[1])
        green_time_ew = random.randint(green_light_duration[0], green_light_duration[1])

        if random.random() < pedestrian_delay_prob:
            green_time_ns -= 5  # Pedestrian delays reduce green light time by 5 seconds
            green_time_ew -= 5
        if random.random() < malfunction_prob:
            green_time_ns, green_time_ew = 0, 0  # Due to a malfunction both lights will stop working

        # Vehicles that pass during green light for NS
        vehicles_pass_ns = min(north_queue, green_time_ns // 2)
        north_queue -= vehicles_pass_ns
        vehicles_pass_ns = min(south_queue, green_time_ns // 2)
        south_queue -= vehicles_pass_ns

        # Vehicles that pass during green light for EW
        vehicles_pass_ew = min(east_queue, green_time_ew // 2)
        east_queue -= vehicles_pass_ew
        vehicles_pass_ew = min(west_queue, green_time_ew // 2)
        west_queue -= vehicles_pass_ew

    return north_queue, south_queue, east_queue, west_queue

#-------------------------------------------------------------------------------------------------------------------------------
#                                                      MONTE CARLO EXECUTION
def monte_carlo_simulation(runs):
    results = []
    for _ in range(runs):
        results.append(traffic_flow_simulation())
    return results

# Function to run Monte Carlo and collect average results
def run_simulations(runs=1000):
    final_results = monte_carlo_simulation(runs)

    # Collecting queue lengths at the end of each simulation run
    north_final = [result[0] for result in final_results]
    south_final = [result[1] for result in final_results]
    east_final = [result[2] for result in final_results]
    west_final = [result[3] for result in final_results]

    # Average queues using np mean function
    avg_north = np.mean(north_final)
    avg_south = np.mean(south_final)
    avg_east = np.mean(east_final)
    avg_west = np.mean(west_final)

    print(f"Average Vehicles Left in North Queue: {avg_north}")
    print(f"Average Vehicles Left in South Queue: {avg_south}")
    print(f"Average Vehicles Left in East Queue: {avg_east}")
    print(f"Average Vehicles Left in West Queue: {avg_west}")

    # ----------------------------------------------------------------------------------------------------------------------------
    #                                                   ANIMATED LINE CHART
    def animate_simulation():
        fig, ax = plt.subplots()
        ax.set_xlim(0, runs)
        ax.set_ylim(0, max(max(north_final), max(south_final), max(east_final), max(west_final)))
        line_north, = ax.plot([], [], label="North Queue", color="blue")
        line_south, = ax.plot([], [], label="South Queue", color="green")
        line_east, = ax.plot([], [], label="East Queue", color="red")
        line_west, = ax.plot([], [], label="West Queue", color="purple")

        def update(frame):
            line_north.set_data(range(frame), north_final[:frame])
            line_south.set_data(range(frame), south_final[:frame])
            line_east.set_data(range(frame), east_final[:frame])
            line_west.set_data(range(frame), west_final[:frame])
            return line_north, line_south, line_east, line_west

        anim = FuncAnimation(fig, update, frames=runs, interval=50)
        plt.legend(loc="upper left")
        plt.title("Animated Traffic Queue Simulation")
        plt.xlabel("Simulation Runs")
        plt.ylabel("Queue Length")
        plt.show()

    # Run the animation
    animate_simulation()

# Run and visualize the simulation
run_simulations(1000)
