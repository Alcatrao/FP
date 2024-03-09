def euclides(a,b):
    if a<=0 or b<=0:
        print("Unnatural numbers detected.")
        exit()

    if a%b==0:
        return b
    return euclides(b, a%b)


x=13
y=29
print(euclides(x,y))