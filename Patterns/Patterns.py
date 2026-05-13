# lines = 10 
# for j in range(lines):
#     for i in range(lines):
#         print("*",end="")
#     print()
    
# lines
# for j in range(lines):
#     print("*"*lines)
    
# *
# **
# *** 
# ****
# *****


lines = 5
for j in range(lines):
    print("*"*(j+1))
    
# *****
# ****
# ***
# **
# *

lines = 5
for j in range(lines):
    print("*"*(lines-j-1))
    

#      *
#     **
#    ***
#   ****
#  *****

# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j+1):
#         print("*",end="")
#     print()
    
    
# *****
#  ****
#   ***
#    **
#     * 

# lines = 5
# for j in range(lines):
#     for k in range(j):
#         print(" ",end=" ")
#     for i in range(lines-j):
#         print("*",end=" ")
#     print()
    
#     *
#    * *
#   * * *
#  * * * * 
# * * * * *

# lines = 5
# for j in range(lines):
#     for k in range(lines-j-1):
#         print(" ",end="")
#     for i in range(j+1):
#         print("* ",end="")
#     print()
    
#     *
#    * *
#   * * *
#  * * * * 
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

lines = 5
for j in range(lines):
    for k in range(lines-j-1):
        print(" ",end="")
    for i in range(j+1):
        print("* ",end="")
    print()

for j in range(lines-1):
    for k in range(j+1):
        print(" ",end="")
    for i in range(lines-j-1):
        print("* ",end="")
    print()
    

