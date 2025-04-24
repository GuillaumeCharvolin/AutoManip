# Installation Guide

This section outlines the steps to set up the development environment for this autonomous object manipulation project.

## Prerequisites

* **Docker:** Ensure Docker is installed on your system.
* **Docker Compose:** Docker Compose should also be installed.
* **Git:** You will need Git to clone the project repository.
* **Ubuntu:** The project is developped on Ubuntu and may not work on other OS.

## Setup Instructions

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/GuillaumeCharvolin/AutoManip.git
    cd AutoManip
    ```

2.  **Start the ROS 2 Container:**
    Navigate to the directory containing your `start.sh` file and give it the permission, and run the start script:
    ```bash
    chmod u+x start.sh
    ./start.sh
    ```

3.  **Install Gazebo:**
    Inside the container, update the package lists:
    ```bash
    apt update
    apt upgrade
    ```
    Then, install the Gazebo packages for your ROS 2 Foxy distribution:
    ```bash
    sudo apt install ros-foxy-gazebo-ros-pkgs ros-foxy-gazebo-ros
    ```

## Verifying the Installation

To verify the Gazebo installation, run:
```bash
gazebo --verbose worlds/empty.world