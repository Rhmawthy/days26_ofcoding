#program list data labtop /computer

list_computer = []
while True:
    merk     = input ("masukkan merk:")
    prosesor = input ("masukkan prosesor yang di gunakan:")
     
    insert_computer = [merk,prosesor]
    list_computer.append (insert_computer)

    for index,computer in enumerate (list_computer):
        
         print (index+1, "|" , computer [0], "|", computer[1])
    
    
    
