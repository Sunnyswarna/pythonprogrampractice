def count(pharse):
    lower=0
    upper=0
    for l in pharse:
        if l.islower():
            lower = lower +1
        elif l.isupper():
            upper = upper +1
    print( 'number of lower is ', lower, upper)
print(count('ABFSJjdhfhJSGhdhjgg'))