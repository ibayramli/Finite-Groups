import math 

# Run extended euclidean algorith to find the two coefficients in Bezout's identity
def extend_euclidean(a, b):
    """
    Inputs: integers a, b

    Outputs: integers m, n such that am + bn = gcd(a, b) in this order
    """
    # This makes sure the variables are in the right order
    a = max(a, b)
    b = min(a, b)

    hist = find_gcd_with_hist(a, b, [])[1]
    
    # Control for the case where:
    if hist == []:
        # b divides a
        if a >  b:
            return (0, 1)
        # a divides b
        return(1, 0)

    for equation in reversed(hist):
        # Control for the case where q_1 and q_2 are undefined
        if equation == hist[-1]:
            q_1 = 1
            q_2 = equation[-1]
            continue
        
        q_1_previous = q_1
        q_1 = q_2
        q_2 = q_1_previous + q_2 * equation[-1]
    
    return q_1, q_2

# Find the inverse of a mod p
def invert_a_mod_b(a, b):
    """
    Inputs: an integer a 

    Output: the inverse of a mod p
    """
    a = max(a, b)
    b = min(a, b)

    a_inverse = extend_euclidean(a, b)[1]

    if a_inverse < 0:
        return -(-b - a_inverse)
    
    return a_inverse

def gcd(a, b):
    """
    Inputs: integers a, b and a list to store the equations

    Outputs: gcd of a, b and a history of equations
    """
    # Calculate q_1 and r_1
    divisor = math.floor(a/b)
    remainder = a - b*divisor
    
    # Terminal case
    if remainder == 0:
        return b

    return gcd(b, remainder)

# Find gcd together with the history of computation to be used in Extended Euclidean Algorithm
def find_gcd_with_hist(a, b, hist):
    """
    Inputs: integers a, b and a list to store the equations

    Outputs: gcd of a, b and a history of equations
    """
    # Calculate q_1 and r_1
    divisor = math.floor(a/b)
    remainder = a - b*divisor
    
    # Terminal case
    if remainder == 0:
        return b, hist

    hist.append([remainder, a, b, -divisor])

    return find_gcd_with_hist(b, remainder, hist)
