import json

def parse_def(input, output):
    main_dict = {}
    index_end = 0 
    components = []                          # it was throwing error in py file so initialized it here
    #opened file in read mode
    with open(input) as f:
        lines = f.readlines()
        # iterating over each line
        i=0 
        for line in lines:
            if line.startswith('UNITS DISTANCE'):
                line1 = line.split(" ")
                
                main_dict['unit_in_micron']=float(line1[3])

                # converting co-oradinate values to mm
                mul_unit = main_dict['unit_in_micron']*(10**-6)
                
            


            # getting line containing die area
            elif line.startswith('DIEAREA'):
                line1 = line.split(" ")
                main_dict['diearea']={'x1':float(line1[2])*mul_unit,
                                        'y1':float(line1[3])*mul_unit,
                                        'x2':float(line1[6])*mul_unit,
                                        'y2':float(line1[7])*mul_unit}
            # getting line containg COMPONENTS and getting start and end index
            elif line.startswith('COMPONENTS'):
                line1 = line.split(" ")
                index_start = lines.index(line)
                index_end = lines.index('END COMPONENTS\n')
                main_dict['number_of_components']=int(line1[1])
            
            # lines containing component part with start and end index
            
            elif lines.index(line)<index_end and lines.index(line)>index_start:
                line3 = line.split("\t")
                line3 = list(filter(None, line3))   #filtering null values
              
                # before we splitted on \t now spliting on space for getting X, Y and Direction values 
                try:
                    line3_1 = line3[2].split(" ")
                except:
                    try:
                        line3_1 = line3[1].split(" ")
                    except:
                        line3_1 = line3[0].split(" ")

                try:
                    line3_2 = line3[1].strip("-").split(" ") #splitting some unsplitted lines and extracting instance name
                    line3_2 = list(filter(None, line3_2))
                except:
                    line3_2 = line3[0].strip("-").split(" ")
                    line3_2 = list(filter(None, line3_2))
                

                def parse_components(word):
                    if word in line3_1:
                        components.append({
                                    'Comp_id':i,
                                    'cell_name':line3[0].strip('- ').split(" ")[0],
                                    'instance_name':line3_2[0],
                                    'x':float(line3_1[line3_1.index(word)+2])*mul_unit,
                                    'y':float(line3_1[line3_1.index(word)+3])*mul_unit,
                                    'direction':line3_1[line3_1.index(word)+5]                           
                                    })
            
                
                
                parse_components('COVER')
                parse_components('FIXED')
                parse_components('PLACED')
                i+=1
    main_dict['components']=components
    main_json = json.dumps(main_dict, indent=4)

    print(len(main_dict['components']))
    print(main_dict['number_of_components'])
    if len(main_dict)!=main_dict['number_of_components']:
        print('There are {} missing components'.format(main_dict['number_of_components']-len(main_dict['components'])))
        
    with open(output, 'w') as output1:
        json.dump(main_dict, output1, indent=4)
    return output

parse_def('dd1.def', 'def_out.json')
