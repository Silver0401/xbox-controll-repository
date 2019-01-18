from state import state
import wpilib


def read_all_controller_inputs():

	#Chasis Inputs


	controller = wpilib.Joystick(0)


	xr = controller.getThrottle()
	state["mov_xr"] = xr

	xl = controller.getZ()
	state["mov_xl"] = xl

	y = controller.getY()
	state["mov_y"] = y

	z = controller.getX()
	state["mov_z"] = z

	button_x = controller.getRawButton(1)
	state["button_x_active"] = button_x

	#Lift_inputs

	button_y = controller.getRawButton(2)
	state["activating_lift"] = button_y




