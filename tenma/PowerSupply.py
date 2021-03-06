import serial,time
from decimal import Decimal

class PowerSupply():
	def __init__(self, Comport):
	    self.ser = serial.Serial(Comport,9600)

	def readResponse (self,formatted = True):
		time.sleep(0.02)
		out = b''
		while self.ser.inWaiting() > 0:
			out += self.ser.read()	
			#print("Got this far..")		
		if out != '':
			# print (out)
			if formatted:
				# print (self.customFormat(out))
				return (self.customFormat(out))
			else:
				print (out)
				return (out)

	def setVoltage (self,a):
		time.sleep(0.02)
		# print (str(a))
		self.ser.write(bytearray("VSET1:"+str(a),'ascii'))	

	def getVoltage (self):
		time.sleep(0.02)
		self.ser.write(bytearray("VOUT1?",'ascii'))	
		return (float(self.readResponse()))
		
	def checkSetVoltage (self):
		time.sleep(0.02)
		self.ser.write(bytearray("VSET1?",'ascii'))
		return ReadResponse()

	def setCurrent (self,a):
		time.sleep(0.02)
		print (str(a))
		self.ser.write(bytearray("ISET1:"+str(a),'ascii'))

	def getCurrent (self):
		time.sleep(0.02)
		self.ser.write(bytearray("IOUT1?",'ascii'))	
		return (float(self.readResponse()))		

	def customFormat(self,ba):
		s = ba.decode("utf-8")
		return s

	def close(self):
		self.ser.close()
	def on(self):
		time.sleep(0.02)
		return self.ser.write(bytearray("OUT1",'ascii'))
	def off(self):
		time.sleep(0.02)
		return self.ser.write(bytearray("OUT0",'ascii'))
	def Status(self):
		time.sleep(0.02)
		self.ser.write(bytearray("STATUS?",'ascii'))
		return self.ReadResponse(formatted=False)

	



