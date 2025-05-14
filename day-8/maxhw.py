n=int(input("enter the no. of people "))
nums=list(map(int, input("enter the h and w of peoples: ").split()))
people=[]
max_height=0
max_width=0
max_height_i=-1
max_width_i=-1
for i in range(0,2*n,2):
    height=nums[i]
    width=nums[i+1]
    people.append((height, width))
    height = [h for h, w in people]    
    width = [w for h, w in people]
    max_height=max(height)
    max_width=max(width)
for h ,w in enumerate(people):
    if h > max_height:
        h=max_height_i
    if w > max_width:
        w=max_width_i

print(people)
print(max_height , max_width)