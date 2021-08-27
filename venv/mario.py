# This program prints out a number of Mario pyramids


# Right sided pyramid

#
##
###
####


for i in range(10):
    for j in range(i):
        print(end=" " "#")
    print("\n")

# Left sided pyramid
    #
   ##
  ###
 ####
#####

for i2 in range(10):
    for j2 in range(10-i2):
        print(end=" " " ")
    for j22 in range(i2):
        print(end=" " "#")
    print("\n")

print("\n\n")
# Half pyramid

######
#####
####
###
##
#
#
##
###
####
#####
######


for i3 in range(10):
    for j3 in range(i3):
        print(end=" " " ")
    for j32 in range(10-i3):
        print(end=" " "#")
    print("\n")
for i4 in range(10):
    for j4 in range(10-i4):
        print(end=" " " ")
    for j42 in range(i4):
        print(end=" " "#")
    print("\n")

print("\n\n")


# Full hour glass

############
##########
########
######
####
##
##
####
######
########
##########
############


for i5 in range(10):
    for j5 in range(i5):
        print(end=" " " ")
    for j52 in range(10-i5):
        print(end=" " "#")
    for j5 in range(10-i5):
        print(end=" " "#")
    for j52 in range(i5):
        print(end=" " " ")
    print("\n")
for i6 in range(10):
    for j6 in range(10-i6):
        print(end=" " " ")
    for j62 in range(i6):
        print(end=" " "#")
    for j6 in range(i6):
        print(end=" " "#")
    for j62 in range(10-i6):
        print(end=" " " ")
    print("\n")
