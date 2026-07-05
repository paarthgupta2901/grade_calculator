m1 = int(input("marks in maths : ")) 
m2 = int(input("marks in physics : "))
m3 = int(input("marks in chemistry : "))
m4 = int(input("marks in english : "))
m5 = int(input("marks in physical education : "))

per = ((m1+m2+m3+m4+m5)/500)*100

if (m1 > 100 or m2 > 100 or m3 > 100 or m4 > 100 or m5 > 100) :
    print("invalid marks") 
else: 
    print(per)
    
    if per >= 90  :
        if per > 100 :
            print("invalid score")
        else :
            print(" grade : A")
    elif per >= 80 and per <90 :
        print(" grade : B")
    elif per >= 70 and per < 80 :
        print(" grade : C")
    elif per >= 60 and per <70 :
        print(" grade : D")
    elif per >= 50 and per < 60 :
        print(" grade : E")
    elif per >= 40 and per < 50 :
        print(" your grade : G")
    if per >= 40 : 
        print("PASS")
    else :
        print("FAIL")
