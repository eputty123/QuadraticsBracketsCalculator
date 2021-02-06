import math as Math

def choose():
  print('\n1: Quit')
  print('2: Find values of x / factor expanded brackets.')
  print('3: Expand brackets.')
  choice = int(input('CHOICE = '))

  if choice == 1:
    return
  elif choice == 2:
    quadform_calc()
  elif choice == 3:
    expand()
  else: print('Unknown choice')

def quadform_calc():
  # Quadratic Formula Calculator using Python
  # ax^2 + bx + c = 0
  # quadratic formula for finding x: (-b +- sqrt(b^2 - 4ac) / 2a

  print('\nax^2 + bx + c = 0\n')

  a = float(input('A = '))
  b = float(input('B = '))
  c = float(input('C = '))

  if a == 1:
    
    # Adding method of Quadratic Formula
    quadpos = (-b + Math.sqrt(b**2 - 4*c)) / 2
    
    # Subtracting method of Quadratic Formula
    quadneg = (-b - Math.sqrt(b**2 - 4*c)) / 2

    # Printing factored brackets
    if a == 1:
      print(f'\nFactored brackets: (x + {-quadpos})(x + {-quadneg})')
    else:
      print(f'\nFactored brackets: {a}(x + {-quadpos})(x + {-quadneg})')

    # Printing values of x
    print(f'\nX = {(-b + Math.sqrt(b**2 - 4*a*c)) / 2*a}')
    print(f'X = {(-b - Math.sqrt(b**2 - 4*a*c)) / 2*a}\n')
  elif a <= 0:
    # If a is 0 or less
    print('ERROR')
  else:
    # Dividing values of b and c by a to exclude the (for example) 2 in 2x^2
    b = float(b/a)
    c = float(c/a)

    if b**2 - 4*c < 0:
      print('ERROR')
      return

    # Adding method of Quadratic Formula
    quadpos = (-b + Math.sqrt(b**2 - 4*c)) / 2
    
    # Subtracting method of Quadratic Formula
    quadneg = (-b - Math.sqrt(b**2 - 4*c)) / 2

    # Printing factored brackets
    if a == 1:
      print(f'\nFactored brackets: (x + {-quadpos})(x + {-quadneg})')
    else:
      print(f'\nFactored brackets: {a}(x + {-quadpos})(x + {-quadneg})')

    # Printing values of x
    print(f'\nX = {quadpos}')
    print(f'X = {quadneg}\n')

def expand():
  
  # Getting input
  print('\n(Outside of bracket)(x + a)(x + b)')
  xamount = float(input('Outside of bracket = '))
  a = float(input('A = '))
  b = float(input('B = '))

  print(f'\nExpanded: {xamount}x^2 + {(a+b) * xamount}x + {(a*b) * xamount}\n')

choose()
