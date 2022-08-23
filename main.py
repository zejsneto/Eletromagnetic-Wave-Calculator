import math

#1
#Insert frequency, calculates the rest
def calc_f():
  f = float(input('Enter frequency value (Hz): '))

  lamb=(3*(10**8))/f
  
  k=2*math.pi/lamb
  
  w=(3*(10**8))*k
  
  print('\nThe lambda value is: {:.2e} (m).'.format(lamb))
  print('The slope value is: {:.2e} (rad/m).' .format(k))
  print('The angular velocity value is: {:.2e} (rad/s).\n' .format(w))

#2
#Insert lambda, calculates the rest
def calc_lambda():
  lamb = float(input('Enter lambda value (m): '))
  
  k=2*math.pi/lamb
  
  w=(3*(10**8))*k
  
  f=(3*(10**8))/lamb
  
  print('\nThe frequency value is: {:.2e} (Hz).'.format(f))
  print('The slope value is: {:.2e} (rad/m).' .format(k))
  print('The angular velocity value is: {:.2e} (rad/s).\n' .format(w))

#3
#Insert slope, calculates the rest
def calc_k():
  k = float(input('Enter slope value (rad/m): '))
  
  lamb=2*math.pi/k
  
  w=(3*(10**8))*k
  
  f=(3*(10**8))/lamb
  
  print('\nThe frequency value is: {:.2e} (Hz).'.format(f))
  print('The lambda value is: {:.2e} (m).' .format(lamb))
  print('The angular velocity value is: {:.2e} (rad/s).\n' .format(w))

#4
#Insert angular velocity, calculates the rest
def calc_w():
  w = float(input('Enter angular velocity value (rad/s): '))

  k=w/(3*(10**8))
  
  lamb=2*math.pi/k
  
  f=(3*(10**8))/lamb
  
  print('\nThe frequency value is: {:.2e} (Hz).'.format(f))
  print('The lambda value is: {:.2e} (m).' .format(lamb))
  print('The slope value is: {:.2e} (rad/m).\n' .format(k))
  
#5
#Insert magnetic field, calculates the electric field
def calc_em():
  bm = float(input('Enter magnetic field value (T): '))

  em=bm*(3*(10**8))
  
  print('\nThe electric field value is: {:.2e} (V/m).\n'.format(em))

#6
#Insert electric field, calculates the magnetic field
def calc_bm():
  em = float(input('Enter electric field value (V/m): '))

  bm=em/(3*(10**8))
  
  print('\nThe magnetic field value is: {:.2e} (T).\n'.format(bm))

#7
#Insert amplitude of the magnetic field, calculates the amplitude of the electric field
def calc_ElectricAm():
  bo = float(input('Enter the amplitude of the magnetic field (T): '))

  eo=bo*(3*(10**8))
  
  print('\nThe amplitude of the electric field is: {:.2e} (V/m).\n'.format(eo))

#8
#Insert amplitude of the electric field, calculates the amplitude of the magnetic field
def calc_MagneticAm():
  eo = float(input('Enter the amplitude of the electric field (V/m): '))

  bo=eo/(3*(10**8))
  
  print('\nThe amplitude of the magnetic field is: {:.2e} (T).\n'.format(bo))

#Create Menu
def main():
  while True:
    print("---***---\n")
    print("Choose an option (0 to 8):\n")
    print("0 - Close \n")
    print("1 - Enter frequency value (Hz)")
    print("2 - Enter lambda value (m)")
    print("3 - Enter slope value (rad/m)")
    print("4 - Enter angular velocity value (rad/s)")
    print("5 - Enter magnetic field value (T)")
    print("6 - Enter electric field value (V/m)")
    print("7 - Calculate the amplitude of the electric field (V/m)")
    print("8 - Calculate the amplitude of the magnetic field (T)\n")
    print("---***---\n")
    
    selector = int(input("Option: "))
    if (selector == 1):
      calc_f()
    elif (selector == 2):
      calc_lambda()
    elif (selector == 3):
      calc_k()
    elif (selector == 4):
      calc_w()
    elif (selector == 5):
      calc_em()
    elif (selector == 6):
      calc_bm()
    elif (selector == 7):
      calc_ElectricAm()
    elif (selector == 8):
      calc_MagneticAm()
    elif(selector==0):
      break
    else:
      print("Please choose an available option.\n")
      
main()