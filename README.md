# **Self-Driving Car Simulation**

A Python-based simulation demonstrating the core concepts of self-driving car navigation. The simulation includes pathfinding using the A* algorithm, obstacle avoidance, and dynamic goal-setting in a 2D grid environment.

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup and Installation](#setup-and-installation)
5. [How It Works](#how-it-works)
6. [Usage](#usage)
7. [Scenarios to Test](#scenarios-to-test)
8. [Contributing](#contributing)
9. [Future Improvements](#future-improvements)

---

## **Introduction**
This project simulates a self-driving car navigating a grid-based map. The car can:
- Detect and avoid both static and dynamic obstacles.
- Dynamically recalculate its path to reach a goal.
- Visualize its planned path and decision-making process in real-time.

This simulation serves as an educational tool for understanding core principles in robotics and AI, such as pathfinding and collision detection.

---

## **Features**
1. **Pathfinding**:
   - A* algorithm dynamically calculates the shortest path to the goal.
2. **Obstacle Avoidance**:
   - Static and dynamic obstacles are detected and avoided.
3. **Dynamic Environment**:
   - Moving obstacles create real-time challenges for the car.
4. **Visualization**:
   - Displays the car’s path, sensor feedback, and decision-making.
5. **Configurable Map**:
   - Easily adjust grid size, obstacles, and goal position.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - `pygame`: For 2D simulation and rendering.
  - `heapq`: For efficient priority queue operations in A* algorithm.
  - `math`: For smooth car movement calculations.

---

## **Setup and Installation**

### **Prerequisites**
- Python 3.8 or higher
- `pip` package manager

### **Installation Steps**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/self-driving-car-simulation.git
   cd self-driving-car-simulation
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install pygame
   ```

4. Run the simulation:
   ```bash
   python simulation.py
   ```

---

## **How It Works**

### **Grid-Based Map**
The environment is divided into a 2D grid. Each grid cell can:
- Be part of the road (walkable space).
- Contain a static or dynamic obstacle.

### **A* Pathfinding Algorithm**
1. Calculates the shortest path from the car’s current position to the goal.
2. Considers both static and dynamic obstacles, recalculating the path if necessary.

### **Obstacle Avoidance**
- **Static Obstacles**: Fixed in place and marked on the grid.
- **Dynamic Obstacles**: Move across the grid, requiring the car to adapt in real-time.

### **Sensors and Visualization**
- The car has simulated sensors for detecting obstacles.
- Visual aids include the planned path, grid layout, and car position.

---

## **Usage**

### **Controls**
- The simulation runs automatically.
- Adjust the grid size, car position, obstacles, and goal in the code.

### **Customizing the Map**
1. **Add Static Obstacles**:
   Define new obstacles as rectangles:
   ```python
   obstacles.append(pygame.Rect(x, y, width, height))
   ```
2. **Add Dynamic Obstacles**:
   Add to the `dynamic_obstacles` list:
   ```python
   dynamic_obstacles.append({"rect": pygame.Rect(x, y, width, height), "speed": velocity})
   ```
3. **Change Goal Position**:
   Set a new goal in grid coordinates:
   ```python
   goal = (row, col)
   ```

---

## **Scenarios to Test**

### **1. Dense Static Obstacles**
- Create a highly cluttered environment.
- Verify if the car successfully avoids obstacles and finds a valid path.

### **2. Moving Obstacles**
- Add several moving obstacles.
- Check if the car adapts to the dynamic changes.

### **3. Dynamic Goal**
- Change the goal position during the simulation.
- Observe if the car recalculates its path in real-time.

### **4. No Path Available**
- Block all routes to the goal.
- Confirm if the car stops and logs an appropriate message.

---

## **Contributing**
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## **Future Improvements**
1. **Advanced Pathfinding**:
   - Use D* or RRT for more efficient real-time pathfinding.
2. **3D Simulation**:
   - Extend to a 3D environment using tools like Unity or Blender.
3. **Machine Learning**:
   - Train a neural network for obstacle detection and decision-making.
4. **Traffic Rules**:
   - Add traffic lights and signals for more realistic scenarios.

---

## **License**
This project is licensed under the MIT License. See `LICENSE` for more details.

---
