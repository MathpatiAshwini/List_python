question_list =[["who is the frist ledi priminister of india?"],["What is the capital of India?"],["which is the correcte year about domastic valians?"]]
options_list = [["pratibha patil", "saniya mirja", "indira gandi", "mayavati"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["2005", "1999", "1947", "1860"]]
life=[["pratibha patil","indira gandi"],["mumbai","Dehli"],["2005","1961"]]
life_solution=[2,2,1]
solution_list=[3,4,1]
i=0
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(options_list[i]):
        print(j+1,options_list[i][j])
        j=j+1
    user=("without live line","with live line")
    print("choise your choise")
    print("1. without life")
    print("2.with life line")
    choise=int(input("your choise"))
    if choise==1:
        user1=int(input("enter your ans"))
        if user1==solution_list[i]:
            print("wow!!congratulacation")
    elif choise==2:
        if count==0:
            k=0
            while k<len(life[i]):
                print(k+1,life[i][k])
                k=k+1
            count=count+1
            user2=int(input("enter your ans"))
            if user2==life_solution[i]:
                print("wow!!congratulacation")
            else:
                print("you are wrong anshwer")
        else:
            print("you have used your lifline")
            user3=int(input("enter your ans"))
            if user3==solution_list[i]:
                print("wow!!congratulacation")
            else:
                print("you are wrong answer")
                break
    else:
        print("you are wrong answer")
        break
    i=i+1