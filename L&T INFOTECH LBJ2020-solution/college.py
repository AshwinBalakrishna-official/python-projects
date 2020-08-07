import csv
class College():
    #to view details
    def view(self):
        with open('college.txt','r') as colFile:
            reader=csv.reader(colFile)
            colList= []
            for row in reader:
                if len(row) != 0:
                    colList= colList + [row]
        colFile.close()
        print(colList)
    
    #to add a student detail
    def addrow(self):
        with open('college.txt','a') as colFile:
            writer=csv.writer(colFile)
            College_Id=int(input('Enter the college id : '))
            College_Name=input('ENter the college name : ')
            Course_Type=input('Enter the Course name : ')
            City=input('Enter the City of  College : ')
            Fees=int(input('Enter the Fees of College : '))
            PinCode=int(input('Enter the pincode of college area : '))
            colDetails=[College_Id, College_Name, Course_Type, City,Fees,PinCode]
            writer=csv.writer(colFile)
            writer.writerow(colDetails)
        colFile.close()
    
    
    #to search based on city
    def city_search(self):
        with open('college.txt','r') as colFile:
            city=input('Enter the  city you want to search : ')
            reader=csv.reader(colFile)
            for row in reader:
                for search in row:
                    if(search == city):
                        print(row)
        colFile.close()
    
    #to delete based on id
    def id_delete(self):
        with open('college.txt','r') as colFile:
            new_row=[]
            id=input('Enter the id to delete : ')
            reader=csv.reader(colFile)
            x=1
            for row in reader:
                for search in row:
                    if(search == id):
                        x=0
                if(x == 1):
                    new_row.append(row)
                else:
                    x=1
        colFile.close()
        with open('college.txt','w') as colFile:
            writer=csv.writer(colFile)
            writer.writerow(new_row)
        colFile.close()
            
                        
        
        
obj=College()
print('Welcome to college,What would u like to do:\n1. View \n2. Insert \n3. Search \n4. Delete')
in1=int(input('Your Choice:'))
if(in1==1):
    obj.view()
elif(in1==2):
    obj.addrow()
elif(in1==3):
    obj.city_search()
elif(in1==4):
    obj.id_delete()
else:
    print('invalid option')
         
