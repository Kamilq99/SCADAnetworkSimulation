# Traffic light simulation system

### Project Description

The aim of this project was to design and implement a simplified simulation of traffic lights using a master-slave architecture. The project aimed not only to reproduce the basic logic of traffic lights, but also to demonstrate how such systems can be implemented in real conditions using modern IT technologies and the principles applicable to industrial automation systems.

### Technological Context

In real industrial and infrastructure environments, such as smart cities or traffic management systems, solutions based on Operation Technology (OT) are widely used. One of the key components of such environments are SCADA (Supervisory Control and Data Acquisition) systems, which play the role of central supervision and control. SCADA systems communicate with distributed executive units, such as PLCs (Programmable Logic Controllers), which perform specific operations at the physical level, e.g. switching traffic lights on and off.

The master-slave architecture was chosen as a model reflecting this approach. In our case, the "master" is responsible for coordinating the entire system, while the "slave" responds to its commands and executes them in a manner consistent with the programmed logic.

### Implementation description

The created application is based on REST API technology, which ensures simple communication between components and easy scalability and integration with other systems. The application was divided into two independent microservices, each of which performs a specific function:

Master microservice - acts as a superior unit. It is responsible for managing the logic of the traffic light cycle (e.g. green → yellow → red), sending control commands to the slave unit, and time synchronization.

Slave microservice - receives commands from the master unit and executes them, emulating the physical operation of traffic lights. It can also send feedback on the status of task execution.

Communication between microservices takes place via HTTP requests in JSON format. This cooperation model reflects well the way in which modern distributed systems exchange data in real time.

### Frontend layer

For the purpose of better visualization of the system operation, a simple graphical interface (frontend) was also prepared, which presents the current status of traffic lights in real time. Data needed for visualization is retrieved from the slave microservice, which provides it in the form of a standardized API.

The frontend can operate both as a local web application and as a component integrated with a larger traffic management system. Thanks to this, it is possible to use this simulation as a prototype for more complex implementations.

##3 Summary

The project is an example of the use of modern programming solutions to represent the logic of classic automation systems. Thanks to the use of microservices, REST API and the master-slave approach, it was possible to create a flexible and readable architecture that can be easily developed and adapted to various scenarios. The project can be treated as an introduction to more advanced simulations of traffic control systems or as didactic material for learning the basics of OT and IoT systems in the context of software engineering.

# Visualization Appearance

![Red Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/24c03f55-cbe7-43b3-a3b6-3c69d35284c3)
![Yellow Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/33285bb9-293e-4807-96f8-fcdf97bcc485)
![Green Light](https://github.com/Kamilq99/SCADAnetworkDANGERsimulation/assets/83961352/99875af1-c3f3-46ed-b4b4-f2bb584352d3)

## Components

1. **Lights**:
    - `Lights.html`: HTML file creating a traffic light visualization.
    - `LightsStyle.css`: CSS file styling the traffic light.
    - `Dockerfile`: Configuring Docker to serve HTML and CSS files using Nginx.

2. **SCADA**:
    - `scada_controller.py`: Python script simulating a SCADA system that sends commands to a PLC every 30 seconds.
    - `Dockerfile`: Docker configuration for SCADA system.

3. **PLC**:
    - `PLC.py`: A Python script simulating a PLC that controls traffic lights based on commands received from a SCADA system.
    - `Dockerfile`: Docker configuration for PLC.

## How to run my app
From the very beginning, the application was designed to be run in a containerized environment using Docker. This method of distribution and run ensures simplicity, repeatability, and ease of implementation in both local and cloud environments.

For this reason, the recommended way to run the project is to use Docker configuration files (e.g. Dockerfile, docker-compose.yml) available in the repository. They allow you to quickly build and run the application without having to manually install dependencies or configure the environment.

More advanced users who prefer other containerization tools — such as Podman — can easily adapt existing Docker files to their own needs. Thanks to Podman's compatibility with Docker CLI, this migration should not be difficult for people with experience with containerization.

## Steps to Get Started

So let's start how to run my application. Obviously, you need to clone my github repository or create a fork and then clone it.

To run the application and develop it, you will need a Python interpreter, and then you need to install the flask framework with the command:

```Bash
pip install flask
```

Another important thing is the Docker I mentioned earlier, in order to run the application, you need to have Docker containerization installed on a computer with a Linux, Windows or MacOS operating system. The application does not require starting each container separately and by the way, I have not used it for a long time, but I widely use an additional device built into docker, which is docker-compose. To run the application, you need to run the command:

```Bash
docker-compose up --build -d
```

It will make all 3 containers built and run in the background. The master-slave architecture (SCADA - PLC) works on port 5000 and should be generally available on localhost:5000, while the frontend visualization of the application is available on localhost:8080


## Docker Compose Configuration

The `docker-compose.yml` file is used to define and run a multi-container Docker application. The configuration includes:

- **Lights**: Starts an Nginx server to serve HTML and CSS files.
- **SCADA**: Starts a SCADA controller script.
- **PLC**: Starts a PLC script.

