### List
from mock_data import mock_catalog

def test_1():
  print("basic python lists")

  nums = [1, 2, 3, 234, 5342, 5433, 633]

  # read
  print(nums[0])
  print(nums[1])

  # add
  nums.append(42)
  nums.append(-1)

  # remove by element
  nums.remove(234)

  # remove by index
  del nums[0]

  print(nums)

  # loop
  for n in nums:
    print(n)

# ------------------------------------
def test_2():
  print("Sum numbers")
  prices = [12.23,345,123.2,542,65,123.2,0.223,-23, 123.2,6,171,5678]

  #for and print every number
  #print the sum of all the number
  # fint the cheapest product
  # find the most expensive product
  total = 0
  cheapest = prices[0]
  most_expensive = prices[0]

  for price in prices:
    print(price)
    total += price

    #compare
    if(price < cheapest):
      cheapest = price

    if(price > most_expensive ):
      most_expensive = price

  print("total: " + str(total))
  print(f"cheapest price:  {cheapest} ")
  print(f"Expensive price: {most_expensive}")

# ------------------------------------
def test_3():
  cheapest = mock_catalog[0]

  for product in mock_catalog:
    #for print evey dict/prod form moc_catalog
    print(f"product: {product}")

    #print only the title of every product
    print(f"Title: {product['title']}")
    print("***", product["price"])

    #the cheapest product is: Title - $price
    if(product["price"] < cheapest["price"]):
      cheapest = product

  print(f"The cheapest product is: {cheapest['title']} - Price: ${cheapest['price']}")




# call
# test_1()
# test_2()
test_3()