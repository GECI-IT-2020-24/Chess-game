#program_that_checks_if_the_given_two_cells_are_same_colour
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if (a%2==0 and c%2==0):              #even_rows
    if (b%2==d%2 and (not b%2)==(not d%2)):  #(not b%2)==(not d%2)
        print("YES")
    else:
        print("NO")
elif (not a%2==0 and not c%2==0):     #odd_rows
    if (b%2==d%2 and (not b%2)==(not d%2)):   #(not b%2)==(not d%2)
        print("YES")
    else:
        print("NO")
else:                               #mixed
    if not b==d:
        print("YES")
    else:
        print("NO")
