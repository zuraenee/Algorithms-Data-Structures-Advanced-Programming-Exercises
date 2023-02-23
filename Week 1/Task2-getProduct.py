def getProduct(text):
    product=1;
    word = text.split("*")
    for i in word:
        product = product * int(i)
    print("product is", product)

getProduct("2*4*5")
