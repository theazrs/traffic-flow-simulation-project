# Monte Carlo Simulation of Traffic Flow at an Intersection

READ THE Monte_Carlo_Simulation_Project_Report.odt FILE FOR A BETTER/INDEPTH EXPLANATION 

This project simulates traffic flow through an intersection managed by traffic lights using the Monte Carlo method. By running thousands of simulations, this project captures the effect of various factors on traffic queues, helping model the unpredictable behavior of traffic and providing insights that can be used to improve traffic management systems.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Simulation Variables](#simulation-variables)
- [Results Interpretation](#results-interpretation)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The simulation models four traffic directions at an intersection, with vehicles arriving at different rates and traffic lights changing based on random conditions. The project tracks average vehicle queue lengths over multiple runs, visualizing the results in an animated line chart. This can be particularly useful for traffic management or city planning to optimize traffic flows and understand the effects of random delays.

## Features

- **Traffic Flow Simulation**: Simulates vehicle queues in each direction (North, South, East, and West).
- **Monte Carlo Method**: Uses random events to model real-life uncertainties, like varying vehicle arrival rates, pedestrian delays, and traffic light malfunctions.
- **Animated Visualization**: Shows the evolution of vehicle queues over multiple simulation runs.
- **Real-World Insights**: Provides valuable insights for traffic flow management and potential real-world applications.

## Technologies Used

- Python (3.7 or higher)
- NumPy
- Matplotlib

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/civaabtw/traffic-flow-simulation-project.git
   cd traffic-flow-simulation-project
2. **Install Required Libraries**: Ensure that numpy and matplotlib are installed. 
    Run:
    ```bash
    pip install numpy matplotlib

## Usage

1. **Run the Simulation**: Execute the following command to start the simulation and display the animated chart.
    ```bash
    python traffic_simulation.py
2. **Interpreting the Animated Chart**
    Each line represents a different traffic queue direction:
    Blue: North Queue
    Green: South Queue
    Red: East Queue
    Purple: West Queue
    The animation displays how queues evolve, showing fluctuations due to random factors and potential congestion patterns.
3. **Customization**: You can adjust the simulation parameters in traffic_simulation.py, such as:
    green_light_duration, 
    vehicle_arrival_rate, 
    and total_iterations.

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. Please credit the me (CivaaBTW) when making modifications.

## License

This project is open for use and modification, but credit must always be given to the original author, Wilson Machoco / CivaaBTW. See the LICENSE file for details.

