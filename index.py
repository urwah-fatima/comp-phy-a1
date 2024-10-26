def bisection(fx, a, b, e):
    # Calculate function values at the interval endpoints
    fxa = fx(a)
    fxb = fx(b)
    
    # Check if the root is bracketed between a and b
    if fxa * fxb > 0:
        print("Root is not bracketed between initial guesses")
        return None
    
    # Define a variable for the interval size to avoid repeating (b - a) / 2
    interval = (b - a) / 2
    
    # Keep looping until the interval size is smaller than the tolerance
    while interval > e:
        c = (a + b) / 2  # Calculate the midpoint of the interval
        fxc = fx(c)      # Calculate function value at midpoint
        
        # Debugging prints to show what's happening at each step
        print(f"a = {a}, b = {b}, c = {c}, interval = {interval}, f(c) = {fxc}")
        
        # If the function value at midpoint is close to zero, we've found the root
        if abs(fxc) < e:
            print(f"Root found: {c}")
            return c
        
        # Determine which half of the interval contains the root
        if fxa * fxc < 0:
            b = c  # Root is in the left half
        else:
            a = c  # Root is in the right half
            fxa = fxc  # Update fxa to avoid recomputing fx(a) repeatedly
        
        # Update the interval size for the next iteration
        interval = (b - a) / 2
    
    # If we've reached this point, return the midpoint of the final small interval
    return (a + b) / 2

# Test the bisection function
fx = lambda x: x - 5  # Define the function for which we want to find the root
root = bisection(fx, 2, 8, 0.001)  # Call bisection method with initial interval [2, 8] and tolerance 0.001

# Check if the root is accurate by evaluating fx(root)
print(f"Root found: {root}")
print(f"f({root}) = {fx(root)}")  # This should be close to 0