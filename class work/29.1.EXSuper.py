#
class Phone:
    def __init__(self,user):
        self.user=user
        print(f"\nHello {self.user}.Welcome, Enjoy the below features!!!!")
        print("Call")
        print("SMS")
        print("Snake and ladder")
        print("Alarm")
        print("FM Radio")

class PhoneV1(Phone):
    def __init__(self,user):
        super().__init__(user)
        print("Camera")
        print("Bluetooth")
        print("Music")
        print("Maps")

class PhoneV2(PhoneV1):
    def __init__(self,user):
        super().__init__(user)
        print("Internet")
        print("Front Camera")
        print("Finger Print")
        print("Google")

class PhoneV3(PhoneV1):
    def __init__(self,user):
        print(f"\nHello {user}, This is the Trail version")
        print("Payments")
        print("Updated OS")
        print("FaceId")

class PhoneV4(PhoneV2,PhoneV3):
    def __init__(self,user):
        PhoneV2.__init__(self,user)
        PhoneV3.__init__(self,user)
        print("Scanner")
        print("5G")
        print("ESIM")
        print("Fast Charging")
        


keethana=Phone('keerthana')
akash= PhoneV1('akash')
abhinay=PhoneV2('abhinay')
ramya=PhoneV3('ramya')
nihithya=PhoneV4('nihitha')