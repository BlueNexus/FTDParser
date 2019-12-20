def main():
    while True:
        fileToLoc = (raw_input("Enter the path of the file to localise"))
        f = open(fileToLoc, "r+")
        flines = f.readlines()
        output = []
        for line in flines:
            start = line.find('"')
            end = line.rfind('"')
            if(start > -1 and end > -1 and start != end):
                replacing = line[start:end+1]
                initialreplacing = replacing
                key = ""
                print(line)
                option = int(input("Press 1 to Get, 2 to Format or 3 to skip"))
                if(option in [1,2,3]):
                    if(option == 1):
                        key = raw_input("Enter the key for this value")
                        if(key):
                            line = line.replace(replacing, '_locFile.Get("' + key + '",' + replacing + ')')
                            print(line)
                    elif(option == 2):
                        line = line.strip("$")
                        key = raw_input("Enter the key for this value")
                        if(key):
                            skipping = 0
                            toreplace = []
                            while(skipping > -1):
                                initial = replacing.find('{',skipping)
                                final = replacing.find('}',initial)
                                skipping = final
                                if(skipping > -1):
                                    toreplace.append(replacing[initial+1:final])
                                    print(toreplace)
                            if(len(toreplace)):
                                for thing in range(0, len(toreplace)):
                                    replacing = replacing.replace(toreplace[thing],str(thing))
                            suffix = ", ".join(toreplace)
                            line = line.replace(initialreplacing, '_locFile.Format("' + key + '",' + replacing + ',' + suffix + ')')
                            print(line)
                    elif(option == 3):
                        pass
                    else:
                        pass
            output.append(line)
            print(line)
        f.seek(0)
        f.writelines((output))
        f.truncate()
        f.close()
                        
           
main()
