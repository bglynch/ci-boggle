def sumlist(l):
    if l == []:
        return 0
    else:
        # first = l[0]
        # rest = l[1:]
        # return first + sumlist(rest)

        return l[0] + sumlist(l[1:])

    
print(sumlist([1, 4, 13, 34, 56]))

# Recursion
#   Need 3 things
#   1.  function to call itself
#   2.  values to head towards an end
#   3.  if statement as an escape


def maxlist(l2):
    if len(l2) == 1 :
        return l2[0] 
    else:
        first = l2[0]
        rest = l2[1:]
        max_of_rest = maxlist(rest)
        if first > max_of_rest:
            return first
        else:
            return max_of_rest

print(maxlist([-2, -13, -5, -34, -56]))


