# Assignment 3

The Ki, Kd, and K p values where initialise randomly and the simple PID controller was implemented in the python code. However, the environment applies only a fixed magnitude of force at each step and allows us only to choose the direction. So, only the direction of force was determined by the correction value obtained by the PID controller.

## Running the code

1. Make sure that python3 is installed and install the required packages by running `pip3 install -r ./controls/requirements.txt` where this markdown file is there.
2. Run `python3 ./controls/CartPoleBalance.py`.

The simulation runs for 2000 steps and shows a graph of angle of pole from vertical and the force magnitude calculated by PID controller at each step.
