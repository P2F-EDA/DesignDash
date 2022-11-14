import json
import sys
# defining keys
Start=[]
Start_clk_by=[]
End=[]
End_clk_by=[]
required_time=[]
Path_Group=[]
Path_Type=[]
slack=[]
points = []
data={}
point_index=[]
slack_index=[]

with open(sys.argv[1],'r') as d:
    lines=d.readlines()

    # i=0
    for i, line in enumerate(lines):
        if line.strip().startswith('Startpoint:'):
            c=line.split(':')[1]
            c=c.split('(')
            d=c[1].strip('),\n').split('by')
            Start.append(c[0])
            Start_clk_by.append(d[1])

        elif line.strip().startswith('Endpoint:'):
            c=line.split(':')[1]
            c=c.split('(')
            d=c[1].strip('),\n').split('by')
            End.append(c[0])
            End_clk_by.append(d[1])

        elif line.strip().startswith('Path Group:'):
            Path_Group.append(line.strip('\n').split(':')[1])

        elif line.strip().startswith('Path Type:'):
            Path_Type.append(line.strip('\n').split(':')[1]) 

        elif line.strip().startswith('Point'):
            point_index.append(i)

        elif line.strip().startswith('data required time'):
            c=line.strip('\n,').split('  ')
            c=list(filter(None,c))
            required_time.append(float(c[1])) 

        elif line.strip().startswith('slack'):
            c=line.strip('\n').split(' ')
            c=list(filter(None,c))
            slack.append(c[2])
            slack_index.append(i)
        # i+=1

    #defining main points list where all paths are added 
    points = []  
    for j in range(len(point_index)):
        points_sub = []
        for count, line in enumerate(lines[point_index[j]:(slack_index[j]-14)]):
            # we are accessing 3 lines at a time so skipping 2 indices    
            if count%3!=0:
                pass
            else:
                try:
                    # accessing 3 lines at a time input, output and net lines 
                    li_in = lines[point_index[j]+count+5].split()
                    li_out = lines[point_index[j]+count+6].split()
                    li_net = lines[point_index[j]+count+7].split()
                    
                    dict1={
                        "Point":int(count/3),
                        "Instance_name" : li_in[0],
                        "Cell_name" : li_in[1].strip("()"),
                        "Net" : li_net[0],
                        "In_trance" : float(li_in[2]),
                        "out_trance" : float(li_out[2]),
                        "Delay_increment" : float(li_out[3])-float(li_in[3]),
                        "Net_fanout" : float(li_net[2]),
                        "Net_cap" : float(li_net[3]),
                        "Delay_point" : float(li_out[4]),
                        }
                    points_sub.append(dict1)
                except:
                    li_in = lines[point_index[j]+count+5].split()
                    dict1={
                        "Point":int(count/3),
                        "Instance_name" : li_in[0],
                        "Cell_name" : li_in[1].strip("()"),
                        "Net" : "-",
                        "In_trance" : float(li_in[2]),
                        "out_trance" : "-",
                        "Delay_increment" : "-",
                        "Net_fanout" : "-",
                        "Net_cap" : "-",
                        "Delay_point" : "-",
                        }
                    points_sub.append(dict1)
                    break
                       
        points.append(points_sub)
                
            
with open(sys.argv[2],"w") as outfile:  
             
    d=[{
                'Path':i,
                "Start":Start[i],
                "Start_clk_by":Start_clk_by[i].strip(" )\t"),
                "End":End[i],
                "End_clk_by":End_clk_by[i].strip(" )\t"),
                "Data required time":required_time[i+1],
                "Path Group":Path_Group[i].strip(" \t"),
                "Path Type":Path_Type[i].strip(" )\t"),
                "Slack":float(slack[i].strip("\t")),
                "point":points[i]
                } for i in range(len(End))]

    json.dump(d,outfile,indent=4)