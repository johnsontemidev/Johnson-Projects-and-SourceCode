# =============== INTRODUCTION TO PROGRAMMING - TASK 20 ====================
# =============== JOHNSON TEMILOLA - [26/03/2017] ==========================

# ========== PROGRAMMING DESCRIPTION =================================
'''
    read in the contents of the textfile 'input.txt', and for each line in input.txt.
# Write out a new line in a new text file output.txt that computes the answer to some operation on a list of numbers.

# If the input.txt file has the following:
#    min: 1,2,3,5,6
#    max: 1,2,3,5,6
#    avg: 1,2,3,5,6

# Your program should generate an output.txt file as following:
#    The min of [1, 2, 3, 5, 6] is 1
#    The max of [1, 2, 3, 5, 6] is 6
#    The avg of [1, 2, 3, 5, 6] is 3.4
'''
# ============================================================================

'''
   with open (filename) in read mode as 'file'
        for i in file
           operation is equal to i.strip().split(':') - strip the new line character from the end of the number and split the line variable
           number_list is equal to [int(j) for j in operation[1].split(',')]

           with open (filename) in write mode as outf
               write to output file the min of number list
               write to output file the max of number list
               write to output file the sum of number list divided by the length of number list

'''    


with open ("input.txt", "r") as file:
    for i in file:
        operation = i.strip().split(':')
        number_list = [int(j) for j in operation[1].split(',')]

        with open ("output.txt", "w") as outf:
            outf.write ("The min of [1, 2, 3, 4, 5, 6] is  " + str(min(number_list)) + '\n')
            outf.write ("The max of [1, 2, 3, 4, 5, 6] is  " + str(max(number_list)) + '\n')
            outf.write ("The avg of [1, 2, 3, 4, 5, 6] is  " + str(sum(number_list) / len(number_list)))





         
