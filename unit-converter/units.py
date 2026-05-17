#unit converter
def print_menu():
    print("1. Kilometers to Meters(also works for kilograms,grams)")
    print("2.Meters to Kilometers")
    print("3.Meters to Centimeters")
    print("4.Inch to Centimeter")
    print("5. Centimeter to Inch")
    print("6.Close")

def km_m():
    km=float(input("Enter the value of kilometer:"))
    m=km/10**3
    print("kilometer to meter:",m)
def m_km():
    m=float(input("Enter the value of meter:"))
    km=10**3*m
    print("Meter to Kilometer:",km)

def m_cm():
    m=float(input("Enter the value of meter:"))
    cm=m/10**2
    print("Meter to centimeter:",cm)

def In_cm():
    Inch=float(input("Enter the value of Inch:"))
    cm=Inch*2.54
    print("Inch to centimeter:",cm)

def cm_In():
    cm=float(input("Enter the value of centimeter:"))
    Inch=cm/2.54
    print("Centimeter to Inch:",Inch)

choice=int(input("Enter any choices:"))

while(choice!=6):
    if choice==1:
        km_m()
    elif choice==2:
        m_km()
    elif choice==3:
        m_cm()
    elif choice==4:
        In_cm()
    elif choice==5:
        cm_In()
#If possible more will be added idk
