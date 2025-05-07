l1= [1,2,3,4,5,7,8,9,10]
n=len(l1)+1
expected_sum=n * (n+1) / 2
actual_sum= sum(l1)
missing_num=expected_sum-actual_sum
print('missing_num:',missing_num)    