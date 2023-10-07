def linerasearchproduct(productlist,targetproduct):
  indices=[]

for index ,product in enumerate(productList):
  if product == targetProduct:
    indices.append(index)
return indices


# Example usage:
product=["shoes","boot","loafer","sandal","shoes"]
targert="shoes"
result=linearsearchproduc(products,target)
print(result)
    


  