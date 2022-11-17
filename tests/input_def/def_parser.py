import json
import sys

def parse_def(input, output):
    main_dict = {}
    index_end = 0                           # it was throwing error in py file so initialized it here
    #opened file in read mode
    with open(input) as f:
        lines = f.readlines()
        # iterating over each line
        i=0 
        for line in lines:
            # getting line containing die area
            if line.startswith('DIEAREA'):
                line1 = line.split(" ")
                main_dict['DIEAREA']={'X1':float(line1[2]),
                                        'Y1':float(line1[3]),
                                        'X2':float(line1[6]),
                                        'Y2':float(line1[7])}
            # getting line containg COMPONENTS and getting start and end index
            elif line.startswith('COMPONENTS'):
                line1 = line.split(" ")
                index_start = lines.index(line)
                index_end = lines.index('END COMPONENTS\n')
                main_dict['Number of components']=int(line1[1])
            
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
                        main_dict[f'Comp_{i}']={
                                    'Cell_name':line3[0].strip('- ').split(" ")[0],
                                    'Instance_name':line3_2[0],
                                    'X':float(line3_1[line3_1.index(word)+2]),
                                    'Y':float(line3_1[line3_1.index(word)+3]),
                                    'Direction':line3_1[line3_1.index(word)+5]                           
                                    }
                
                
                parse_components('COVER')
                parse_components('FIXED')
                parse_components('PLACED')
                i+=1

    main_json = json.dumps(main_dict, indent=4)

    print(len(main_dict))
    print(main_dict['Number of components'])
    if len(main_dict)!=main_dict['Number of components']:
        print('There are {} missing components'.format(main_dict['Number of components']-len(main_dict)))
        
    with open(output, 'w') as output1:
        json.dump(main_dict, output1, indent=4)
    return output

parse_def('dd1.def', 'def_out.json')