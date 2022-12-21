print("welcome to KBC game ")
print("are you redy:--?")
questions=["1..which programe we will learn in navgurukul",
["2..who created python program"],
["3..who is the frist priminister of india"],
["4..who is the father of nation"],
["5..who is the frist ledy priminister"]]
options=[["1. sivil engineer" , "2. communication", "3.software engineer"," 4. ngo managment"],
["1. guido van rusum", "2. thomas josarsan","3. nil armstrong","4.bill gates"],
["1. Dr.b.r.Ambedkar","2. Dr.abdul kalam","3. mahatma gandhi","pandit nehru"],
["1. subhash chandr bhos","2.mahatma gandhi","3. narendr modhi","4. Dr.manmohan shing"],
["1. pratibha patil","2. indira gandhi","3. sunita vilam","4. priynka gandi"]]
c=[3,1,4,3,2]
d=[["1. software engineer","2. sivil engineer"],["1. bill gates","2. guido van rusum"],
["1. dr.rajendra prasad","2. pandit nehru"],["1. mahatma gandi","2. narendr modhi"],
["1. saniya mirja","2. indira gandi"]]
salu=[1,2,2,1,2]
i=0
while i<len(questions):
    print(questions[i])
    j=0
    while j<len(options[i]):
        print(options[i][j])
        j=j+1
    i=i+1
    hoose=int(input("choose your options "))
    print("1.with lifeline 2.without lifeline")
    choose=int(input("choose your options "))
    if choose==1:
        