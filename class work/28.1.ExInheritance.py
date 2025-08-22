#
class Person:
    def details(self,name,phonenumber,gender):
        self.name=name
        self.phonenumber=phonenumber
        self.gender=gender

class Driver(Person):
    def driverdetails(self,vehno,photo,vehtype):
        self.vehno=vehno
        self.photo=photo
        self.vechtype=vehtype
        print(f"\n Hello {self.name}\n Your driver account is successfully created")

class Wheels_2:
    def Price2W(self):
        self.fare = 30
        return self.fare
        
class Wheels_3:
    def Price3W(self):
        self.fare = 60 
        return self.fare
        
class Wheels_4:
    def Price4W(self):
        self.fare = 120 
        return self.fare
        
''' class FareCal(2_Wheels,3_Wheels,4_Wheels,Driver):
    def farecal(self,distance):
        if self.vehtype == 2: '''
    
class DriverRides(Driver):
    def driver_rides(self,exp,totalride):
        self.exp=exp
        self.totalride=totalride
        print(f"Hello {self.name}.\n Your ride details are updated")

class User(Person):
    def ridedetails(self,droppoint,pickup):
        self.droppoint=droppoint
        self.pickup=pickup
        print(f"\n Hello {self.name}\nYou booked the ride successfully.\nHave a safe ride!!!")


priyanka=User()
priyanka.login('priyanka',9059719144 ,'F')
priyanka.ridedetails('Ameerpet','Tarnaka')


ramu=Driver()
