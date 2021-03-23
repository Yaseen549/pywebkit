def css_class_generator():
    filename = input("File Name: ")
    total_num_of_classes = int(input("How many CSS class you need?"))
    myfile = open( filename+".css", "w+")

    for i in range(int(total_num_of_classes)):
        print("Class ", int(i+1))
        total_num_of_pv = int(input("How many properties?"))
        myselector = input(str("Selector: "))
        for j in range(int(total_num_of_pv)):
            myproperty = input(str("Property: "))
            myvalue = input(str("Value: "))
            line1 = "." + myselector +"{\n"
            line2 = "    " + myproperty + ": " + myvalue + ";\n"
            line3 = "}"
            l = [line1, line2, line3]
            myfile.writelines(l)
    myfile.close()