print("WELCOME TO KBC GAME !!!\n ARE YOU READY??? ")
question_list =[["who is the frist ledi priminister of india?"],["What is the capital of India?"],["which is the correct year about domastic valians?"],["the largest river in the world"]]
options_list = [["pratibha patil", "saniya mirja", "indira gandi", "mayavati"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["2005", "1999", "1947", "1860"],["godawari","ganga","nail","amezon"]]
life=[["pratibha patil","indira gandi"],["mumbai","Dehli"],["2005","1860"],["nail","amezone"]]
life_solution=[2,2,1,1]
list_solution=[3,4,1,3]
i=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j=j+1
    user=("1. without life line","2. with life line")
    print("choose your choise")
    print("1. without life line")
    print("2.with life line")
    choise=int(input("your choise"))
    if choise==1:
        user1=int(input("enter your answer"))
        if user1==list_solution[i]:
             print("wow!!congraculations your answer is correct")
    elif choise==2:
        if count==0:
            k=0
            while k<len(life[i]):
                print(k+1,life[i][k])
                k=k+1
            count=count+1
            user2=int(input("enter your answer"))
            if user2==life_solution[i]:
                print("wow!!congraculations,go ahead")
            else:
                print("try next time your ansewr is not correct")
        else:
            print("you have used your lifeline")
            user3=int(input("enter your answer"))
            if user3==list_solution[i]:
                print("wow!!congratulacation,you are the winner")
            else:
                print(" sorry go back your answer is wrong")
            user4=int(input("enter your answer"))
            if user4==life_solution[i]:
                print("wow!!congratulacation,your the best plyer")
            else:
                print("your answer is wrong sorry")
            break
    else:
        print(" dont warry try again thank you for particept on kbc game ")
        break
    i=i+1