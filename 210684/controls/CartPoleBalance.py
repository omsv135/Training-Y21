import gym
import numpy as np
import matplotlib.pyplot as plt

# PID coefficients
Kp = 3
Ki = 1
Kd = 1

# The error is the angle of the pole itself;
# The reference is angle 0.
# Clockwise displacement of pole is positive.

# Number of trials
no_of_tries = 1
max_steps = 2000

# Creating the environment
env = gym.make('CartPole-v1', new_step_api=True, render_mode="human")
env.action_space.seed(42)
# print(env.action_space)

# The array containing pole angles for every trial
pole_angles = []

# Array containing the output force values of controller
force_values = []

# Runs the trials
for i in range(no_of_tries):
	cur_pole_angles = []
	cur_force_values = []
	obsv = env.reset(seed=42)

	truncated = False
	terminated = False
	step_count = 0

	integral = 0
	# while ((not truncated) and (not terminated) and (step_count < max_steps)):
	while ((not terminated) and (step_count < max_steps)):
		position, velocity, angle, ang_velocity = obsv

		integral += angle
		# The PID control equation
		force = (Kp * angle) + (Kd * ang_velocity) + (Ki * integral)

		# Deciding the action (the direction of force)
		# - 1 := towards right
		# - 0 := towards left
		action = 1 if (force > 0) else 0

		obsv, reward, terminated, truncated, info = env.step(action)
		step_count += 1

		cur_pole_angles.append(angle)
		cur_force_values.append(force)

	pole_angles.append(cur_pole_angles)
	force_values.append(cur_force_values)
env.close()

# Plot the angules of pole and forces applied by controller
fig, axes = plt.subplots(2, no_of_tries, squeeze=False)

for i, ax in enumerate(axes[0]):
	ax.plot(range(len(pole_angles[i])), pole_angles[i])
	ax.set(
		xlabel="Step",
		ylabel="Angle (in rads)"
	)
	ax.axhline(y=0, color="red", alpha=0.5)

for i, ax in enumerate(axes[1]):
	ax.plot(range(len(force_values[i])), force_values[i])
	ax.set(
		xlabel="Step",
		ylabel="Force"
	)

plt.show()
