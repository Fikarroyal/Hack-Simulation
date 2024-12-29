# Hack Simulation 

This system simulates various hacking techniques such as password cracking, network exploitation, and vulnerability scanning. It is designed as an educational tool to understand basic concepts in cybersecurity and ethical hacking.

## System Overview

The system consists of the following components:

1. **Core Components**:
   - `network.py`: Simulates network scanning and exploitation of vulnerabilities.
   - `cracker.py`: Simulates cracking of passwords using different techniques.
   - `exploit.py`: Simulates exploiting security flaws in the target system.

2. **Modules**:
   - `scanner.py`: Simulates scanning for open ports and vulnerabilities.
   - `brute_force.py`: Implements a brute force attack for password cracking.
   - `keylogger.py`: Simulates a keylogger for educational purposes.

3. **Targets**:
   - `server.py`: Represents a vulnerable server that can be exploited.
   - `device.py`: Represents a device that can be targeted for attacks.

4. **Utilities**:
   - `logger.py`: Logs the progress and events during the simulation.
   - `encryption.py`: Simulates encryption and decryption operations.
   - `config.py`: Holds configuration variables for the simulation.

5. **Testing**:
   - Unit tests are provided to verify the functionality of key components.

## Installation

To run this project, you'll need Python 3.x installed on your machine. Follow the steps below:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/hack_simulation.git
   cd hack_simulation

2. **Install required dependencies**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   pip install -r requirements.txt

3. **Running the simulations**

   ```bash
   python main.py
   python -m unittest discover tests/


