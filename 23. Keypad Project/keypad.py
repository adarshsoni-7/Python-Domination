num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))



for board in num_pad:
    for key in board:
        print(key, end=" ")        
    print()