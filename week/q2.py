"""2. Given three angles of a triangle, determine whether it is an acute,
obtuse, or right-angled triangle."""

a:float=float(input("enter the no"))
b:float=float(input("enter the no"))
c:float=float(input("enter the no"))
sum=a+b+c
if sum==180:   
    if a==90 or b==90 or c==90:
       type="right"
    elif a<90 and b<90 and c<90:
       type="acute"

    else:
       type="obtuse" 
    print(f"{type=}")   
else:
      print("invalid")    

   











