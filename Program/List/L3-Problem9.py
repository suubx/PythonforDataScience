A = [1, 2, 3]
B = [4, 5, 6]
A.append(B)
print("Using append():", A)

A = [1, 2, 3] 
B = [4, 5, 6]
A.extend(B)
print("Using extend():", A)

A = [1, 2, 3] # Resetting list A
B = [4, 5, 6]

C = A + B
print("Using + operator:", C)