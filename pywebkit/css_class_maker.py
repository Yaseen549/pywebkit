# CSS Class Generator

def css_class_generator():
    filename = input("File name: ")
    total_num_of_classes = int(input("How many CSS classes do you need?: "))
    myfile = open( filename + ".css", "w+")

    for i in range(int(total_num_of_classes)):
        print("Class ", int(i+1))
        total_num_of_pv = int(input("How many properties?: "))
        css_selector = input("Selector: ")
        line1 = "." + css_selector +"{\n"
        myfile.writelines(line1)
        
        for j in range(int(total_num_of_pv)):
            css_property = input("Property: ")
            css_value = input("Value: ")            
            line2 = " "*4 + css_property + ": " + css_value + ";\n"
            myfile.writelines(line2)
        
        line3 = "}\n\n"
        myfile.writelines(line3)
    myfile.close()

# New Lines
for f in range(12):
    exec(f"def newline{f+1}(): print('\\n'*{f+1})")
