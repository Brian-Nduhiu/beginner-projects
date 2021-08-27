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
