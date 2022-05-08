
# calla function named numbers
def numbers():
  for number in range(1,21):
    if number is not 11 and number is not 13:
    # if number is not [11, 13,19]:
      print("#",number)

#find the smallest/min number
def lowest():
  nums = [12,234,123,56,678,45,7,3,567,2423,56,-2,345,6752,-34,345,0,0,2]

  smallest = nums[0]
  for n in nums:
    if(n < smallest):
      smallest = n

  print(f'lowest {smallest}')


numbers()
lowest()