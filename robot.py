
import wpilib
from wpilib.drive import MecanumDrive
from state import state
import oi
import time


class MyRobot(wpilib.TimedRobot):

	def robotInit(self):

		self.frontLeftMotor = wpilib.Talon(0)
		self.rearLeftMotor = wpilib.Talon(1)
		self.frontRightMotor = wpilib.Talon(2)
		self.rearRightMotor = wpilib.Talon(3)

		self.sensor_1 = wpilib.DigitalInput(1)

		self.frontLeftMotor.setInverted(True)

		self.rearLeftMotor.setInverted(True)


		self.drive = MecanumDrive(self.frontLeftMotor,
										 self.rearLeftMotor,
										 self.frontRightMotor,
										 self.rearRightMotor)


	def teleopPeriodic(self):   

		oi.read_input()

		x = state["mov_x"]
		y = state["mov_y"]
		z = state["mov_z"]

	

		if state["button_x_active"]:
			if self.sensor_1.get():
				self.drive.driveCartesian(0, 0, 0, 0)
			else:
				self.drive.driveCartesian(0, -1, 0, 0)

		else:
			self.drive.driveCartesian(x, y, z, 0)
				


if __name__ == '__main__':
	wpilib.run(MyRobot)
