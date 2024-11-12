import os
from menu.mainMenu import desing as desingPrincipal
from menu.calculateTipMenu import desing as basic_tip
from menu.divideAmountsMenu import desing as multiple_basic_tip
from menu.thanksMenu import desing as exit

def main():
    while True:
        os.system('clear')  
        option = desingPrincipal()  
        
        if option == 1:
            os.system('clear')  
            basic_tip()
            os.system('clear') 
        elif option == 2:
            os.system('clear')
            multiple_basic_tip()
            os.system('clear') 
        else:
            os.system('clear')
            if exit() == 0:  
                break

main()
