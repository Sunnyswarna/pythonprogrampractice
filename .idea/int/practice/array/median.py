l1=[25,60]
l2 = [10,90]
combine = l1 + l2
combine.sort()
print('sort list:',combine)
n=len(combine)
if n % 2 ==1:
    median = combine[n//2]
else:
    m1=combine[n//2-1]
    m2=combine[n//2]
    median = (m1+m2)/2
print('median:',median)