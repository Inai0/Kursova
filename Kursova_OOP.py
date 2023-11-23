import os
import re
from datetime import datetime,timedelta
class types_of_mineral_fertilizers:
    def __init__(self):
        self.type_name = "type of mineral fertilizers not found"
        self.type_index=0
        self.storage=[400,200]
        self.overall_amount = sum(self.storage)
        self.storage_date=[datetime.now(),datetime.now()]
        self.status=[]
        self.shelf_life=0
        name="empty"
    def Show_type(self):
        return self.type_name

    
class Nitrogen_Fertilizers (types_of_mineral_fertilizers):
    def __init__(self):
        super().__init__()
        self.type_name = "Nitrogen_Fertilizers"
        self.type_index=1
class Phosphorus_Fertilizers (types_of_mineral_fertilizers):
    def __init__(self):
        super().__init__()
        self.type_name = "Phosphorus_Fertilizers"
        self.type_index=2
class Potassium_Fertilizers (types_of_mineral_fertilizers):
    def __init__(self):
        super().__init__()
        self.type_name = "Potassium_Fertilizers"
        self.type_index=3
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    return False       
Type1=Nitrogen_Fertilizers()
Type2=Phosphorus_Fertilizers()
Type3=Potassium_Fertilizers()
types_array=[Type1,Type2,Type3]
j=1
#Filling objects with info
ammoniacal=Nitrogen_Fertilizers()
ammoniacal.name="ammoniacal"
ammoniacal.shelf_life=2
ammonium_sulfate=Nitrogen_Fertilizers()
ammonium_sulfate.name="ammonium_sulfate"
ammonium_sulfate.shelf_life=3
ammonium_nitrate=Nitrogen_Fertilizers()
ammonium_nitrate.name="ammonium_nitrate"
ammonium_nitrate.shelf_life=1
ammonium_phosphates=Phosphorus_Fertilizers()
ammonium_phosphates.name="ammonium_phosphates"
ammonium_phosphates.shelf_life=1
calcium_phosphates=Phosphorus_Fertilizers()
calcium_phosphates.name="calcium_phosphates"
calcium_phosphates.shelf_life=1
superphosphates=Phosphorus_Fertilizers()
superphosphates.name="superphosphates"
superphosphates.shelf_life=2
potassium_sulfate=Potassium_Fertilizers()
potassium_sulfate.name="potassium_sulfate"
potassium_sulfate.shelf_life=3
potassium_chloride=Potassium_Fertilizers()
potassium_chloride.name="potassium_chloride"
potassium_chloride.shelf_life=3
fertilizers_array=[ammoniacal,ammonium_sulfate,ammonium_nitrate,ammonium_phosphates,calcium_phosphates,superphosphates,potassium_sulfate,potassium_chloride]
global logs
logs=[]
def main_menu(fertilizers_array):
    print ("main menu\n\n1.Edit informatin about ferlitizers.\n2.Order logs\n3.Exit program")
    roam=input('\npress number to choose an option: ')
    if not re.match("^[0-9]*$", roam):
        print ("Error! Only numbers 0-9 allowed!")
        return True
    roam=int(roam)
    if roam==1:
        return (ferlitizers_edit(fertilizers_array))  
    if roam==2:
        if len(logs)==0:
            print ("No logs")
            return True
        for i in range(len(logs)):
            print ("Orders:")
            print (str(i+1)+'.'+logs[i])
    if roam==3:return clear_terminal() 
    else:return True  
def order_edit(choosen_obj_id,fertilizers_array):
    #deleting ordered amout from ferliteze's batches
    if len(fertilizers_array[choosen_obj_id].storage)>0:
        while True:
            amount=input("Write amout of fertilizers: ")
            if not re.match("^[0-9]*$", amount):
                print ("Error! Only numbers 0-9 allowed!")
            else: break
            
        amount=int(amount)
        dif=amount
    else:
        print("No fertilizers!")
        return fertilizers_array
    fertilizers_array[choosen_obj_id].overall_amount=0
    
    for i in fertilizers_array[choosen_obj_id].storage:
        fertilizers_array[choosen_obj_id].overall_amount+=i
    if amount>fertilizers_array[choosen_obj_id].overall_amount:
        print("\nNo enought fertilizers!")
        return fertilizers_array
    logs.append('Ferlitizer type: '+fertilizers_array[choosen_obj_id].Show_type()+' Ferlitizer name: '+fertilizers_array[choosen_obj_id].name+' Amount ordered: '+str(amount)+' Date: '+datetime.now().strftime("%Y-%m-%d %H:%M"))
    for i in range(len(fertilizers_array[choosen_obj_id].storage)):
        if dif<=fertilizers_array[choosen_obj_id].storage[i]:
            if dif==fertilizers_array[choosen_obj_id].storage[i]:
                fertilizers_array[choosen_obj_id].storage.pop(i)
                break
            fertilizers_array[choosen_obj_id].storage[i]-=dif
            break
        else: dif-=fertilizers_array[choosen_obj_id].storage[i]
    for j in range(i):
        fertilizers_array[choosen_obj_id].storage.pop(0)
        fertilizers_array[choosen_obj_id].storage_date.pop(0)
    return fertilizers_array
def check_status(fertilizers_array,i,choosen_obj_id):
    if fertilizers_array[choosen_obj_id].status[i]==True:
        return ' Expired'
    else: return ' Not Expired'
def obj_data(fertilizers_array,choosen_obj_id):
    #Prints information about ferlitize
    print('\nname: ' + fertilizers_array[choosen_obj_id].name + '\nType: '+fertilizers_array[choosen_obj_id].Show_type()+'\nShelf life: ' +str(fertilizers_array[choosen_obj_id].shelf_life) +' years\nBatchs: ')
    j=1
    for i in range(len(fertilizers_array[choosen_obj_id].storage)):
        print(str(j)+"."+str(fertilizers_array[choosen_obj_id].storage[i])+'kg Manufacturing date: '+str(fertilizers_array[choosen_obj_id].storage_date[i].strftime("%Y-%m-%d %H:%M"))+check_status(fertilizers_array,i,choosen_obj_id))
        j+=1
    
def batch_edit(choosen_obj_id,fertilizers_array):
    #adds a batch
    while True:
        local=input("\nWrite amout of fertilizers: ")
        if not re.match("^[0-9]*$", local):
            print ("Error! Only numbers 0-9 allowed!")
        else: break
            
    fertilizers_array[choosen_obj_id].storage.append(int(local))
    fertilizers_array[choosen_obj_id].storage_date.append(datetime.now())
    return fertilizers_array
def ferlitizers_edit(fertilizers_array):
    while True:
        
        while True:
            j=1
            print ("\nChoose type of the fertilizers:\n")
            for i in types_array:
                print(str(j)+"."+i.type_name)
                j+=1
            print (str(j)+'.Back to main menu')
            roam=input('\npress number to choose an option: ')
            if not re.match("^[0-9]*$", roam):
                print ("Error! Only numbers 0-9 allowed!")
            else: break
        roam=int(roam)
        if int(roam)==j:
            return True
        if int(roam)<=len(types_array):
            break
        else: print("No such type.")
    print ('\nType: '+types_array[int(roam)-1].Show_type()+"\n\nChoose the fertilizer:")
    ferlitizer_roam=int(roam)
    while True:
        
        while True:
            j=1
            index=0
            counter=0
            for i in fertilizers_array:
                if ferlitizer_roam==i.type_index:
                    print(str(j)+"."+i.name)
                    j+=1
                    index=counter-2
                counter+=1
            print (str(j)+'.Back to main menu')
            roam=input('\npress number to choose an option: ')
            if not re.match("^[0-9]*$", roam):
                print ("Error! Only numbers 0-9 allowed!")
            else: break
        roam=int(roam)
        if roam==j:
            return True
        if roam<j:
            break
        else:
            print("No such fertilizer.")
    choosen_obj_id=(index+roam)-1
    while True:
    #checking if batchs are expired 
        for i in range(len(fertilizers_array[choosen_obj_id].storage)):
            if fertilizers_array[choosen_obj_id].storage_date[i]+timedelta(days=365*(fertilizers_array[choosen_obj_id].shelf_life))<datetime.now():
                fertilizers_array[choosen_obj_id].status.append(True)
            else: fertilizers_array[choosen_obj_id].status.append(False)
        
        while True:
            obj_data(fertilizers_array,choosen_obj_id)
            print('\n1.Add batch\n2.Add order\n3.Back to main menu')
            roam_in_edit=input('\npress number to choose an option: ')
            if not re.match("^[0-9]*$", roam_in_edit):
                print ("Error! Only numbers 0-9 allowed!")
            else: break
        roam_in_edit=int(roam_in_edit)
        if roam_in_edit==1:
            fertilizers_array=batch_edit(choosen_obj_id,fertilizers_array)
        if roam_in_edit==2:
            fertilizers_array=order_edit(choosen_obj_id,fertilizers_array)
        if roam_in_edit==3:
            return True
        elif roam_in_edit>3: print ('No such option')
    return True    
start=True
while start:
    start=main_menu(fertilizers_array)
    print ('\n')
    