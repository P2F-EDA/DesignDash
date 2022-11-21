import json
import sys
# defining keys

def parse_timing(input, output):
    start=[]
    start_clk_by=[]
    end=[]
    end_clk_by=[]
    required_time=[]
    path_Group=[]
    path_Type=[]
    slack=[]
    points = []
    data={}
    point_index=[]
    slack_index=[]

    with open(input,'r') as d:
        lines=d.readlines()

        for i, line in enumerate(lines):
            if line.strip().startswith('Startpoint:'):
                c=line.split(':')[1]
                c=c.split('(')
                d=c[1].strip('),\n').split('by')
                start.append(c[0].strip())
                start_clk_by.append(d[1])

            elif line.strip().startswith('Endpoint:'):
                c=line.split(':')[1]
                c=c.split('(')
                d=c[1].strip('),\n').split('by')
                end.append(c[0].strip())
                end_clk_by.append(d[1])

            elif line.strip().startswith('Path Group:'):
                path_Group.append(line.strip('\n').split(':')[1])

            elif line.strip().startswith('Path Type:'):
                path_Type.append(line.strip('\n').split(':')[1]) 

            elif line.strip().startswith('Point'):
                point_columns = line.split()
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

        #defining main points list where all paths are added 
        points = [] 
        for j in range(len(point_index)):
            points_sub = []

            for count, line in enumerate(lines[point_index[j]:(slack_index[j]-14)]):
                # checking for 2 number of columns in points section
                if len(point_columns)>3:
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
                                "point":int(count/3),
                                "instance_name" : li_in[0],
                                "ref_name" : li_in[1].strip("()"),
                                "net" : li_net[0],
                                "in_trans" : float(li_in[2]),
                                "out_trans" : float(li_out[2]),
                                "delay_increment" : float(li_out[3])-float(li_in[3]),
                                "net_fanout" : float(li_net[2]),
                                "net_cap" : float(li_net[3]),
                                "delay_point" : float(li_out[4]),
                                }
                            points_sub.append(dict1)
                        except:
                            li_in = lines[point_index[j]+count+5].split()
                            dict1={
                                "point":int(count/3),
                                "instance_name" : li_in[0],
                                "ref_name" : li_in[1].strip("()"),
                                "net" : "-",
                                "in_trans" : float(li_in[2]),
                                "out_trans" : "-",
                                "delay_increment" : "-",
                                "net_fanout" : "-",
                                "net_cap" : "-",
                                "delay_point" : "-",
                                }
                            points_sub.append(dict1)
                            break
                else:
                    if count%2!=0:
                        pass
                    else:
                        try:
                            # accessing 2 lines at a time input, output.  
                            li_in = lines[point_index[j]+count+5].split()
                            li_out = lines[point_index[j]+count+6].split()
                            dict1={
                                "point":int(count/2),
                                "instance_name" : li_in[0],
                                "ref_name" : li_in[1].strip("()"),
                                "net" : '-',
                                "in_trans" : '-',
                                "out_trans" : '-',
                                "delay_increment" : float(li_out[2])-float(li_in[2]),
                                "net_fanout" : '-',
                                "net_cap" : '-',
                                "delay_point" : float(li_out[3]),
                                }
                            points_sub.append(dict1)
                        except:
                            li_in = lines[point_index[j]+count+5].split()
                            if 'data' in li_in:
                                break
                            else:
                                dict1={
                                    "point":int(count/2),
                                    "instance_name" : li_in[0],
                                    "ref_name" : li_in[1].strip("()"),
                                    "net" : "-",
                                    "in_trans" : '-',
                                    "out_trans" : "-",
                                    "delay_increment" : "-",
                                    "net_fanout" : "-",
                                    "net_cap" : "-",
                                    "delay_point" : "-",
                                    }
                                points_sub.append(dict1)
                                break
                        

                        
            points.append(points_sub)
                    
                
    with open(output,"w") as outfile:  
                
        d=[{
                    'path':i,
                    "start":start[i],
                    "start_clk_by":start_clk_by[i].strip(" )\t"),
                    "end":end[i],
                    "end_clk_by":end_clk_by[i].strip(" )\t"),
                    "data_required_time":required_time[i+1],
                    "path_group":path_Group[i].strip(" \t"),
                    "path_type":path_Type[i].strip(" )\t"),
                    "slack":float(slack[i].strip("\t")),
                    "points":points[i]
                    } for i in range(len(end))]

        json.dump(d,outfile,indent=4)
    return output
    

parse_timing('fulladder_timing_V0.1.rpt.txt', 'timing_out.json')
