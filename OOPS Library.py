class batch2():
    
    def init(self):
        pass 
    
    def form(self):
        wave=int(input("Enter the Age:"))
        if(wave<=18):
            segment='Teen'
            print('Teen')
        elif(wave<39):
            segment='adult'
            print('adult')
        elif(wave<60):
            segment='citizen'
            print('citizen')
        else:
            segment='senior citizen'
            print('senior citizen') 
        return segment
    
    def passwordcheck(self):
        wave=input("Enter the password:")
        if(wave=='Hope@123'):
            passwordcheck='correct'
            print('welcome')
        else:
            passwordcheck='incorrect'
            print('sorry the passwork is incorrect,trg again') 
        return passwordcheck
    
    def twoseg(self):
        wave=int(input("Enter the Age:"))
        if(wave<18):
            answer='adult'
            print('adult')
        else:
            answer='citizen'
            print('citizen') 
        return answer
    
    
class Calculator():
    
    def init(self):
        pass 
    
    def addition(self,a,b):
        addition=a+b
        return addition
    def sub(self,a,b):
        sub=a-b
        return sub
    def mul(self,a,b):
        mul=a*b
        return mul
    def div(self,a,b):
        div=a/b
        return div
    
    
class Mall():
    
    def init(self):
        pass 
    
    def addition(self):
        num1=int(input("enter the number1:"))
        num2=int(input("enter the number2:"))
        addition=num1+num2
        print('addition')




