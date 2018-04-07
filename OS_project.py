
# coding: utf-8

# In[42]:


#GUI part of the code 
       #Entry(root,textvariable=name)

from  tkinter import *
case=0
root= Tk()
root.title("CPU Scheduler")
arrival=StringVar()
burst=StringVar()
priority=StringVar()
quantum=StringVar()
process=StringVar()

#print(myname)
#frame=Frame(root,width=300,height=250)

root.geometry("640x640+0+0")
def arrival_func(dic):
    keys=list(dic.keys())
    values=list(dic.values())
    arrival_list=[]
    while (len(values)!=0):
        j=0
        min_index=0
        for x2 in values:
            if(values[min_index][0]>x2[0]):
                min_index=j            
            j+=1
        minimum_process=keys[min_index]
        arrival_list.append(minimum_process)
        values.pop(min_index)
        keys.pop(min_index) 
    return arrival_list


def FCFS_func(dic):
    output=" "
    line2= " "
    arrival_list=arrival_func(dic)
    sum=0
    flag1=0
    line2 +="["+ str(dic[arrival_list[0]][0])+"]"
    for process in arrival_list:
        output+=str(process)
        burst_time=dic[process][1]
        while (burst_time>0):
            output+=" "
            line2 +=" "
            burst_time-=1
        sum+=dic[process][1]
        if(flag1==0):
            sum+=dic[process][0]
        flag1+=1
        line2 +="["+str(sum)+"]"
    output_label1=Label(root, text =line2)
    output_label1.grid(row=7,sticky=W)
    output_label2=Label(root, text =output)
    output_label2.grid(row=8,sticky=W) 
    
def SJF_NON_func(dic):
    output=" "
    line2 =" "
    arrival_list=arrival_func(dic)
    burst_list=[]
    flag2=0
    sum1=0 
    while (len(arrival_list)!=0):
        first=arrival_list[0]
        for process2 in arrival_list:
            if(first!=process2):
                if(dic[first][0]==dic[process2][0]or dic[process2][0]<=sum1):
                    if(dic[first][1]>dic[process2][1]):
                        first=process2
        sum1+=dic[first][1]
        if(flag2==0):
            sum1+=dic[first][0]
        flag2+=1
        burst_list.append(first)
        first_index=arrival_list.index(first)
        arrival_list.pop(first_index)
    sum=0
    line2+="["+str(dic[burst_list[0]][0])+"]"
    flag1=0
    for process in burst_list:
        output+=str(process)
        burst_time=dic[process][1]
        while (burst_time>0):
            output+=" "
            line2 +=" "
            burst_time-=1
        sum+=dic[process][1]
        if(flag1==0):
            sum+=dic[process][0]
        flag1+=1        
        line2+="["+str(sum)+"]"
    output_label1=Label(root, text =line2)
    output_label1.grid(row=14,sticky=W)
    output_label2=Label(root, text =output)
    output_label2.grid(row=15,sticky=W)

def Priority_Non_func(dic):
    output=" "
    line2 =" "    
    priority_queue=[]
    arrival_list=arrival_func(dic)
    flag2=0
    sum1=0    
    while(len(arrival_list)!=0):
        first=arrival_list[0]
        for process2 in arrival_list:  
            if(process2!=first):
                if(dic[first][0]==dic[process2][0] or dic[process2][0]<=sum1 ):
                    if(dic[first][2]>dic[process2][2]):
                        first=process2  
        sum1+=dic[first][1]
        if(flag2==0):
            sum1+=dic[first][0]
        flag2+=1
        priority_queue.append(first)
        first_index=arrival_list.index(first)
        arrival_list.pop(first_index)
    sum2=0
    flag1=0
    line2+="["+str(dic[priority_queue[0]][0])+"]"
    for process in priority_queue:
        output+=str(process)
        sum2+=dic[process][1]
        if(flag1==0):
            sum2+=dic[process][0]
        count=0
        while(count<dic[process][1]):
            output+=" "
            line2+=" "
            count+=1
        line2+="["+str(sum2)+"]"
        flag1+=1
    output_label1=Label(root, text =line2)
    output_label1.grid(row=22,sticky=W)
    output_label2=Label(root, text =output)
    output_label2.grid(row=23,sticky=W)

def Round_Robin_func (dic,Quantum):
    output=" "
    line2 =" "
    arrival_list=arrival_func(dic)
    queue_list=arrival_list  
    sum=0
    flag1=0
    line2+="["+str(dic[arrival_list[0]][0])+"]"
    for process in queue_list:
        output+=str(process)
        burst_time=dic[process][1]
        Quantum_counter=1
        while (Quantum_counter<=Quantum and Quantum_counter<=burst_time ):
            dic[process][1]-=1
            output+=" "
            line2 +=" "
            Quantum_counter+=1
        if(flag1==0):
            sum+=dic[process][0]
        flag1+=1            
        if(dic[process][1]==0):
            sum+=burst_time
            line2+="["+str(sum)+"]"
        else:
            sum+=Quantum
            line2+="["+str(sum)+"]"
            queue_list.append(process)    
    output_label1=Label(root, text =line2)
    output_label1.grid(row=30,sticky=W)
    output_label2=Label(root, text =output)
    output_label2.grid(row=31,sticky=W)

    
def run():
    if(case=="FCFS"):
        process_input=0
        process_input=str(process.get())
        arrival_input=0
        arrival_input=str(arrival.get())
        burst_input=0
        burst_input=str(burst.get())
        schedule_process={}
        #print(process_input)
        process_input=process_input.split(',')
        arrival_input=arrival_input.split(',')
        burst_input=burst_input.split(',')
        i=0
        for item in process_input:
            schedule_process[item]=[int(arrival_input[i]),int(burst_input[i])]
            i+=1
        FCFS_func(schedule_process)
    if(case=="SJF_NON"):
        process_input=0
        process_input=str(process.get())
        arrival_input=0
        arrival_input=str(arrival.get())
        burst_input=0
        burst_input=str(burst.get())
        schedule_process={}
        #print(process_input)
        process_input=process_input.split(',')
        arrival_input=arrival_input.split(',')
        burst_input=burst_input.split(',')
        i=0
        for item in process_input:
            schedule_process[item]=[int(arrival_input[i]),int(burst_input[i])]
            i+=1
        SJF_NON_func(schedule_process)
    if(case=="priority_NON"):
        process_input=0
        process_input=str(process.get())
        arrival_input=0
        arrival_input=str(arrival.get())
        burst_input=0
        burst_input=str(burst.get())
        priority_input=0
        priority_input=str(priority.get())
        schedule_process={}
        #print(process_input)
        process_input=process_input.split(',')
        arrival_input=arrival_input.split(',')
        burst_input=burst_input.split(',')
        priority_input=priority_input.split(',')
        i=0
        for item in process_input:
            schedule_process[item]=[int(arrival_input[i]),int(burst_input[i]),int(priority_input[i])]
            i+=1
        Priority_Non_func(schedule_process) 
    if(case=="round_robin"):
        process_input=0
        process_input=str(process.get())
        arrival_input=0
        arrival_input=str(arrival.get())
        burst_input=0
        burst_input=str(burst.get())
        quantum_input=0
        quantum_input=str(quantum.get())
        quantum_input=int(quantum_input)
        schedule_process={}
        #print(process_input)
        process_input=process_input.split(',')
        arrival_input=arrival_input.split(',')
        burst_input=burst_input.split(',')
        i=0
        for item in process_input:
            schedule_process[item]=[int(arrival_input[i]),int(burst_input[i])]
            i+=1
        Round_Robin_func(schedule_process,quantum_input)

    
#2,4,0,2,3
#1,5,2,3,6
def FCFS_button():
    global case
    case="FCFS"
    process_label=Label(root, text = "Enter processes list:")
    process_label.grid(row=3,sticky=W)
    
    arrival_label=Label(root, text = "Enter arrival_time list:")
    arrival_label.grid(row=4,sticky=W) 
    
    burst_label=Label(root, text = "Enter burst_time list:")
    burst_label.grid(row=5,sticky=W) 
    
    process_Entry=Entry(root,textvariable=process)
    process_Entry.grid(row=3,column=1,sticky=W)
    
    arrival_Entry=Entry(root,textvariable=arrival)
    arrival_Entry.grid(row=4,column=1,sticky=W)
    
    Burst_Entry=Entry(root,textvariable=burst)
    Burst_Entry.grid(row=5,column=1,sticky=W)   
    
    run_button=Button(root,text="run",command=run)
    run_button.grid(row=6,column=0,sticky=W)
    
def SJF_NON_button():
    global case
    case="SJF_NON"
    process_label=Label(root, text = "Enter processes list:")
    process_label.grid(row=10,sticky=W)
    
    arrival_label=Label(root, text = "Enter arrival_time list:")
    arrival_label.grid(row=11,sticky=W) 
    
    burst_label=Label(root, text = "Enter burst_time list:")
    burst_label.grid(row=12,sticky=W) 
    
    process_Entry=Entry(root,textvariable=process)
    process_Entry.grid(row=10,column=1,sticky=W)
    
    arrival_Entry=Entry(root,textvariable=arrival)
    arrival_Entry.grid(row=11,column=1,sticky=W)
    
    Burst_Entry=Entry(root,textvariable=burst)
    Burst_Entry.grid(row=12,column=1,sticky=W)   
    
    run_button=Button(root,text="run",command=run)
    run_button.grid(row=13,column=0,sticky=W)

def priority_NON_button():
    global case
    case="priority_NON"
    process_label=Label(root, text = "Enter processes list:")
    process_label.grid(row=17,sticky=W)
    
    arrival_label=Label(root, text = "Enter arrival_time list:")
    arrival_label.grid(row=18,sticky=W) 
    
    burst_label=Label(root, text = "Enter burst_time list:")
    burst_label.grid(row=19,sticky=W) 
    
    priority_label=Label(root, text = "Enter priority_time list:")
    priority_label.grid(row=20,sticky=W) 
    
    process_Entry=Entry(root,textvariable=process)
    process_Entry.grid(row=17,column=1,sticky=W)
    
    arrival_Entry=Entry(root,textvariable=arrival)
    arrival_Entry.grid(row=18,column=1,sticky=W)
    
    Burst_Entry=Entry(root,textvariable=burst)
    Burst_Entry.grid(row=19,column=1,sticky=W)   
    
    priority_Entry=Entry(root,textvariable=priority)
    priority_Entry.grid(row=20,column=1,sticky=W)  
    
    run_button=Button(root,text="run",command=run)
    run_button.grid(row=21,column=0,sticky=W)

def round_robin_button():
    global case
    case="round_robin"
    process_label=Label(root, text = "Enter processes list:")
    process_label.grid(row=25,sticky=W)
    
    arrival_label=Label(root, text = "Enter arrival_time list:")
    arrival_label.grid(row=26,sticky=W) 
    
    burst_label=Label(root, text = "Enter burst_time list:")
    burst_label.grid(row=27,sticky=W) 
    
    quantum_label=Label(root, text = "Enter Quantum_time:")
    quantum_label.grid(row=28,sticky=W) 
    
    process_Entry=Entry(root,textvariable=process)
    process_Entry.grid(row=25,column=1,sticky=W)
    
    arrival_Entry=Entry(root,textvariable=arrival)
    arrival_Entry.grid(row=26,column=1,sticky=W)
    
    Burst_Entry=Entry(root,textvariable=burst)
    Burst_Entry.grid(row=27,column=1,sticky=W)   
    
    quantum_Entry=Entry(root,textvariable=quantum)
    quantum_Entry.grid(row=28,column=1,sticky=W)  
    
    run_button=Button(root,text="run",command=run)
    run_button.grid(row=29,column=0,sticky=W)
    
def scheduler_button():
    FCFS = Button(root,text="FCFS",command=FCFS_button)
    FCFS.grid(row=2,column=0,sticky=W)
    SJF_NON_PREEM = Button(root,text="SJF_NON_PREEM",command=SJF_NON_button)
    SJF_NON_PREEM.grid(row=9,column=0,sticky=W)
    PRIORITY_NON_PREEM = Button(root,text="PRIORITY_NON_PREEM",command=priority_NON_button)
    PRIORITY_NON_PREEM.grid(row=16,column=0,sticky=W)
    ROUND_ROBIN = Button(root,text="ROUND_ROBIN",command=round_robin_button)
    ROUND_ROBIN.grid(row=24,column=0,sticky=W)
    '''
    SJF_PREEM = Button(root,text=" SJF_PREEM")#,command=scheduler_button)
    SJF_PREEM.grid(row=7,column=0,sticky=W)
    

    PRIORITY_PREEM = Button(root,text="PRIORITY_PREEM")#,command=scheduler_button)
    PRIORITY_PREEM.grid(row=4,column=0,sticky=W)
    PRIORITY_NON_PREEM = Button(root,text="PRIORITY_NON_PREEM")#,command=scheduler_button)
    PRIORITY_NON_PREEM.grid(row=5,column=0,sticky=W)
    ROUND_ROBIN = Button(root,text="ROUND_ROBIN")#,command=scheduler_button)
    ROUND_ROBIN.grid(row=6,column=0,sticky=W)
    '''
    Note= Label(root,text="Note:Insert comma ',' between every input for example: p1,p2,p3",font=("arial",10,"bold"),bg="steelblue",fg="Black")
    Note.grid(row=1,sticky=W)
button1 = Button(root,text="Choose The type of scheduler",command=scheduler_button)#type of scheduler
button1.grid(row=0,column=0,sticky=W)


root.mainloop()


# In[32]:




