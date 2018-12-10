#225 - Exercise 1: From given list

#gadgets = [“Mobile”, “Laptop”, 100, “Camera”, 310.28,

#“Speakers”, 27.00, “Television”, 1000, “Laptop Case”, “Camera Lens”]

#a) Calculate the total price of the all the gadgets.

#b) Calculate the average of all the gadgets.


def priceGadgets(GadItems):
    priceList = []
    for prod in GadItems:
        if isinstance(prod, int) or isinstance(prod, float):
            priceList.append(prod)
    total = sum(priceList)
    average = total/len(priceList)
    return 'Total ${:.2f} / Average: ${:.2f}'.format(total, average)

gadgets = ['Mobile', 'Laptop', 100, 'Camera', 310.28, 'Speakers', 27.00, 'Television', 1000, 'Laptop Case', 'Camera Lens']
GadItems = priceGadgets(gadgets)
print(GadItems)
        