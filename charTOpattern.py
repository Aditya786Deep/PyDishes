
import string as st
n=7
def disign_A():
    for i in range(n):
       if i==0:
         print(' '*n+'*')
       elif i==3:
        print(' '*(n-i-1)+'* '*4+'* ')
       else:
        print(' '*(n-i-1)+'*'+' '*(2*i+1)+'*')
def disign_D():
  for i in range(n):
    if i==0 or i==(n-1):
      print('* '*4)
    else:
      print('*  '*1+' '*2+'   *'*1)
def disign_O():
  for i in range(n):
    if i==0 or i==(n-1):
      print(' '*2+'*  '*3)
    else:
      print('*   '*1+' '*2+'   *'*1)
def disign_C():
  for i in range(n):
    if i==0 or i==(n-1):
      print('  *'*4)
    else:
      print('*'+' '*3)
def disign_E():
  for i in range(n):
    if i==0 or i==(n-1) or i==3:
      print('* '*4)
    else:
      print('*'+' '*3)
def disign_F():
  for i in range(n):
    if i==0  or i==3 :
      print('* '*4)
    else:
      print('*'+' '*3)
def disign_L():
  for i in range(n):
    if  i==(n-1):
      print('* '*4)
    else:
      print('*'+' '*3)
def disign_U():
  for i in range(n):
    if  i==(n-1):
      print(' '*2+'*  '*3)
    else:
      print('*   '*1+' '*2+'   *'*1)
def disign_V():
  for i in range(n):
    if i==(n-1):
      print(' '*n+'*')
    else:
      print(' '*(i+1)+'*'+'  '*(n-i-1)+'*')
def disign_T():
  for i in range(n):
    if i==0:
      print('* '*5)
    else:
      print('  '*2+'*'+' '*2)
def disign_I():
  for i in range(n):
    if i==0 or i==(n-1):
      print('* '*5)
    else:
      print('  '*2+'*'+' '*2)
def disign_K():
  j=1
  for i in range(n):
    if i<=3:
      print('*'+' '*(n-2*i)+'*')
    else:
      print('*'+' '*(j+1)+' *')
      j += 2
def disign_R():
  for i in range(n):
    if i==0 or i==3:
      print('*  '*3)
    else:
      print('*   '*1+' '*2+'   *'*1)
def disign_P():
  for i in range(n):
    if i==0 or i==3:
      print('*  '*3)
    elif i>=4:
      print('*')
    else:
      print('*  '+' '*4+'*')
def disign_X():
  j=0
  for i in range(n+1):
       if i<4:
         print(' '*(i+3)+'*'+' '*(n-2*i)+'*')
       else:
           print(' '*(n-j-1)+'*'+' '*(2*j+1)+'* ')
           j += 1
def disign_Y():
  for i in range(n+1):
      if i<4:
        print(' '*(i+1)+'*'+' '*(n-2*i)+' *')
      else:
        print(' '*(n-2)+'*')
def disign_B():
  for i in range(n):
    if i==0 or i==(n-1) or i==3:
      print('* '*4)
    else:
      print('*'+' '*3+'   *')
def disign_J():
  for i in range(n):
    if i==0:
      print('* '*4)
    elif i==n-1:
      print(' * '*2)
    elif i==n-2:
      print('*'+' '*4+' *')
    else:
      print(' '*6+'*')
def disign_N():
  for i in range(n):
    print('*'+' '*(i+1)+'*'+' '*(n-i-1)+'*')
def disign_M():
  for i in range(n):
    if i<4:
      print('*'+' '*(i+1)+'*'+' '*(n-2*i)+'*'+' '*(i+1)+'*')
    else:
      print('*'+' '*11+'*')
def disign_H():
  for i in range(n):
    if i==3:
      print('* '*4)
    else:
      print('*'+' '*5+'*')
def disign_Z():
  for i in range(n):
   if i==0 or i==(n-1):
     print('*  '*5)
   else:
     print('  '*(n-i-1)+'*')
def disign_S():
  for i in range(n):
    if i==0 or i==(n-1) or i==3:
      print(' * '*3)
    elif i==1 or i==2:
      print('*'+' '*3)
    elif i==4 or i==5:
      print(' '*6+'  *')
def disign_W():
  for i in range(n):
    print('*'+' '*(n-i-1)+'*'+'  '*(i+1)+'*'+' '*(n-1-i)+'*')
def disign_G():
  for i in range(n):
    if i==0 or i==(n-1):
      print(' *'*4)
    elif i==5 :
      print('*'+' '*6+'*')
    elif i==4:
      print('* '+' '*2+' *'*2)
    else:
      print('*')
def disign_Q():
  for i in range(n):
    if i==0 or i==(n-1):
      print(' * '*3)
    elif i==4:
      print('* '*5)
    elif i==5:
      print('*'+' '*9+'*')
    else:
      print('*'+' '*7+'*')
while 1:
    char = input('Enter your character in capital:')
    if char not in st.ascii_uppercase:
      print('Please! enter uppercase alphabates or valid characters...')
    for alpha in char:
        if alpha == 'A':
          disign_A()
          print('='*36)
        elif alpha == 'B':
          disign_B()
          print('='*36)
        elif alpha == 'C':
          disign_C()
          print('='*36)
        elif alpha == 'D':
          disign_D()
          print('='*36)
        elif alpha == 'E':
          disign_E()
          print('='*36)
        elif alpha == 'F':
          disign_F()
          print('='*36)
        elif alpha == 'G':
          disign_G()
          print('='*36)
        elif alpha == 'H':
          disign_H()
          print('='*36)
        elif alpha == 'I':
          disign_I()
          print('='*36)
        elif alpha == 'J':
          disign_J()
          print('='*36)
        elif alpha == 'K':
          disign_K()
          print('='*36)
        elif alpha == 'L':
          disign_L()
          print('='*36)
        elif alpha == 'M':
          disign_M()
          print('='*36)
        elif alpha == 'N':
          disign_N()
          print('='*36)
        elif alpha == 'O':
          disign_O()
          print('='*36)
        elif alpha == 'P':
          disign_P()
          print('='*36)
        elif alpha == 'Q':
          disign_Q()
          print('='*36)
        elif alpha == 'R':
          disign_R()
          print('='*36)
        elif alpha == 'S':
          disign_S()
          print('='*36)
        elif alpha == 'T':
          disign_T()
          print('='*36)
        elif alpha == 'U':
          disign_U()
          print('='*36)
        elif alpha == 'V':
          disign_V()
          print('='*36)
        elif alpha == 'W':
          disign_W()
          print('='*36)
        elif alpha == 'X':
          disign_X()
          print('='*36)
        elif alpha == 'Y':
          disign_Y()
          print('='*36)
        elif alpha == 'Z':
          disign_Z()
          print('='*36)
    choice = input('Want to draw any other alphabate disign[y/n]>>')
    if choice == 'n' or choice == 'N':
          break
    elif choice == 'y' or choice == 'Y':
      continue
        