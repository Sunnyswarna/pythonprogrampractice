n1 = [5,10]
gcd = 1
for i in range(1, min(n1)+1):
    if n1[0] % i == 0 and n1[1] % i == 0:
        gcd = i 
print("GCD of", n1[0], "and", n1[1], "is", gcd)
lcm = (n1[0] * n1[1]) // gcd    
print("LCM of", n1[0], "and", n1[1], "is", lcm)
                        