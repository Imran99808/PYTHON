# Statistics module with its two functions
import statistics
# first function
data=[10, 15, 25, 25, 275, 325, 475]
stat=statistics.pstdev(data)        # The pstdev returns the population standard deviation in short the sqare root of the population varience
print(stat)                         # if we need to retrive the avarage growth of population in some areas than this fuction can be very useful.

# Second function
geomet=statistics.geometric_mean(data)
print(geomet)                       # It basically finds the avarage of the given data unlike arithemetic mean it also
                                    # finds the acurate avarage while in percentage. It is generally used to determine
                                    # the performance result of and investment of portfolio.


