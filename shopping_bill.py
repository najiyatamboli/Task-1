
a = b = c = d = e = 100


def ElectronicsGST(a, b):
    Add = a + b
    calculateGST = Add * 18 / 100
    return Add + calculateGST


def FashionGST(c, d):
    Add = c + d
    calculateGST = Add * 13 / 100
    return Add + calculateGST


def foodGST(e):
    calculateGST = e * 7 / 100
    return e + calculateGST


def totalBill(a, b, c, d, e):
    electronics = ElectronicsGST(a, b)
    fashion = FashionGST(c, d)
    food = foodGST(e)

    return electronics + fashion + food


def calculateDiscountBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    payable = total - discount

    print("Total after GST =", total)
    print("Discount =", discount)
    print("Total payable bill =", payable)

    return payable


calculateDiscountBill(a, b, c, d, e)
