import wpilib
from wpilib.drive import MecanumDrive
from state import state
import oi
import time


class MyRobot(wpilib.TimedRobot):

	def robotInit(self):

		#motores

		self.frontLeftMotor = wpilib.Talon(0)
		self.rearLeftMotor = wpilib.Talon(1)
		self.frontRightMotor = wpilib.Talon(2)
		self.rearRightMotor = wpilib.Talon(3)

		self.lift_motor = wpilib.Talon(4)
		self.cargo_motor = wpilib.Talon(5)

		#sensores

		self.sensor_izquierdo = wpilib.DigitalInput(1)
		self.sensor_principal = wpilib.DigitalInput(2)
		self.sensor_derecho = wpilib.DigitalInput(3)
		#invertidores de motores

		self.frontLeftMotor.setInverted(True)
		self.rearLeftMotor.setInverted(True)

		#Unión de los motores para su funcionamiento
		# en conjunto de mecaunm

		self.drive = MecanumDrive(
			self.frontLeftMotor,
			self.rearLeftMotor,
			self.frontRightMotor,
			self.rearRightMotor)
										
	def teleopPeriodic(self):  

		def getThrottle(self):
			return self._getRawAxis(0) 


		#se leen constantemente los botones y joysticks

		oi.read_all_controller_inputs()

		#código para el funcionamiento del movimiento
		# de las mecanum a través del control de xbox

		x = state["mov_x"] 
		y = state["mov_y"] * 0.7
		z = state["mov_z"] * 0.7

		if state["mov_xr"] != 0 and state["mov_xl"] == 0:
			x = state["mov_xr"] * 0.7

		if state["mov_xl"] != 0 and state["mov_xr"] == 0:
			x = state["mov_xl"] * 0.7


		powerX = 0 if x < 0.05 and x > -0.05 else x
		powerY = 0 if y < 0.05 and y > -0.05 else y
		powerZ = 0 if z < 0.05 and z > -0.05 else z


		self.drive.driveCartesian(powerX, powerY, powerZ, 0)
			
		#código para el funcionamiento del elevador y la garra
        
		if state["activating_lift"]:
			state["timer_lift"] += 1
			if state["timer_lift"] <= 100:
				self.lift_motor.set(1)
			elif state["timer_lift"] <= 200:
				self.lift_motor.set(0)
				self.cargo_motor.set(-1)
			elif state["timer_lift"] <= 300:
				self.lift_motor.set(-1)
				self.cargo_motor.set(0)
			else:
				self.lift_motor.set(0)
				self.cargo_motor.set(0)
		else:
			state["timer_lift"] = 0
			self.lift_motor.set(0)
			self.cargo_motor.set(0)

#funcion para correr el código del robot utlizando
# este archivo como el principal

if __name__ == '__main__':
	wpilib.run(MyRobot)