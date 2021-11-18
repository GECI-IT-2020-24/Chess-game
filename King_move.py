#progam_which_defines_the_movement_of_king_piece_in_chess
a=int(input())
b=int(input())
c=int(input())
d=int(input())
if c-1==a or c+1==a:                #top_and_bottom_rows
    if d-1==b or d+1==b:
        print("YES")
    elif d==b:
        print("YES")
    else:
        print("NO")
elif d-1==b or d+1==b:              #side_rows
    if c-1==a or c+1==a:
        print("YES")
    elif c==a:
        print("YES")
    else:
        print("NO")
else:
    print("NO")