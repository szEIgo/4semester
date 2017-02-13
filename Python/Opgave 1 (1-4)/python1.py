#
#1
print("#1")
import timeit


first_list = list(range(1,1000000))
print "first index "+ str(min(first_list))
print "last index " + str(max(first_list))

print "Sum of whole list: " + str(sum(first_list))
print str(timeit.timeit())[0:5] + " seconds"

print timeit.timeit()
#2
print
print("#2")
print("Gauss Method")
print((first_list[0] + first_list[-1]) * len(first_list) / 2)


#3

print "#3 odd numbers 1-20"
odds = list(range(1,20,2))

print odds
print
#4
print
print [i * 3 for i in range(3,30)]

#5

print [value ** 3 for value in range (1,10)]





	
