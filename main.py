contacts={}

while True:
    print('1 :Create Contact ')
    print('2 :View Contact ')
    print('3 :Update Contact ')
    print('4 :Delete Contact ')
    print('5 :Search Contact ')
    print('6 :Count Contact ')
    print('7 :Exit Contact ')

    Choice=input("Enter your Choice:")

    if Choice == '1':
        name=input("Enter A name: ")
        if name in contacts:
            print("Contact name {name} is already there")
        else:
            age=input("Enter your Age =")
            email=input("Enter your email =")
            mobile=input("Enter your mobile number=")
            contacts[name]={'age':int(age),'email':email,'mobile':mobile}
            print("Contact name {name} Add Successufilly")

    elif Choice == '2':
        name=input("Enter A Name to View: ")
        if name in contacts:
            contacts=contacts[name]
            print(f'Name:{name},Age:{age},email:{email},mobile:{mobile}')
        else:
            print("Contact not found")

    elif Choice == '3':
        name=input("Enter A name to Update: ")
        if name in contacts:
           age=input("Enter your Age =")
           email=input("Enter your email =")
           mobile=input("Enter your mobile number=")
           contacts[name]={'age':int(age),'email':email,'mobile':mobile} 
        else:
            print('Contact not found') 

    elif Choice == '4':
        name=input("Enter A name to Delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact name {name} Deleted Successufilly")
        else:
            print('Contact not found') 
    
    elif Choice == '5':
        search_name=input("Enter A name to Search: ")
        found = False
        for name,contact in contacts.items():
            print(f'Found-Name{name}Age{age},Email:{email},Mobile{mobile}')
        if not found:
            print("No contact found")

    elif Choice == '6':
        print(f"Total contact in contact book :{len(contacts)}")

    elif Choice == '7':
        print("Good bye.....Closing the program")
    
    else:
      print("Invalid input")

 
    



        
        


