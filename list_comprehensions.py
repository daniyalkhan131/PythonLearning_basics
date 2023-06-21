# better than doing with looping as have to write long code
nums=list(range(1,4))
print(nums)

nums1=[x*10 for x in nums]
print(nums1)

name="daniyalkhan"
name_list=[char.upper() for char in name]
print(name_list)

friends=["ashley","matt","michael"]
frnd_list=[x[0].upper()+x[1:] for x in friends] # we can also-
# -do this with .capitalize()
print(frnd_list)

print([bool(val) for val in [0,'',[]]])

str_list=[str(i) for i in nums]
print(str_list)

# LC with conditnal logic
numbers=list(range(1,7))
evens= [num for num in numbers if num%2==0]
print(evens)
odds=[num for num in numbers if num%2!=0]
print(odds)
#if have to include else then way of writing change
tt=[num*2 if num%2==0 else num/2 for num in numbers]
print(tt)

with_vowels="this is so much fun"
tt=''.join(char for char in with_vowels if char not in "aeiou")
print(tt)  # .join() is use for concatenating string-
# -with '' in between every char

print([i for i in [1,2,3,4] if i in [3,4,5,6]])
print([i[::-1].lower() for i in ["Elie", "Tim", "Matt"]])
# same 
print([i.lower()[::-1] for i in ["Elie", "Tim", "Matt"]])
print([i for i in "amazing" if i not in "aeiou"])