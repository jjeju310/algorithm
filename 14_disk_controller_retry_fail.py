def what_is_min(waiting, time):
    wait_sec = time-waiting[0][0]
    work_sec = waiting[0][1]
    min_sec = wait_sec + work_sec
    min_j = [wait_sec, waiting[0][0], waiting[0][1]]
    min_idx = 0
    if(len(waiting)==1):
        return min_j, min_idx
    for i in range(1, len(waiting)):
        wait_sec = time-waiting[i][0]
        work_sec = waiting[i][1]
        temp_sec = wait_sec + work_sec
        if(min_sec > temp_sec):
            min_sec = temp_sec
            min_j =  [wait_sec, waiting[i][0], waiting[i][1]]
            min_idx = i
    print("indef",min_j)
    return min_j, min_idx

jobs.sort()
print(jobs)
working = [[0,jobs[0][0],jobs[0][1]]]
waiting = []
done = []
time_sum = 0
time = 0

while(True):
    time += 1
    
    print("time",time)
    if(len(working)!=0 and (working[0][0]+working[0][1]+working[0][2])==time):
        print("before", working)
        done.append(working[0])
        print("done",done)
        time_sum += (time-working[0][1])
        print("sum",time_sum)
        if(len(done)==len(jobs)):
            break

        print("def", waiting)
        if(len(waiting)!=0):
            wait_min_j, del_idx = what_is_min(waiting, time)
            print("wait_min_j", wait_min_j, "del_idx",del_idx)
            del working[0]
            del waiting[del_idx]
            working.append(wait_min_j)
        print("after", working)

    for idx in range(1, len(jobs)):
        if(len(working)!=0  and jobs[idx][0]==time):   
            waiting.append(jobs[idx])
        elif(len(working)==0  and jobs[idx][0]==time):
            working.append([time-jobs[idx][0],jobs[idx][0],jobs[idx][1]])
    """if(len(jobs)>idx):
        if(len(working)!=0  and jobs[idx][0]==time):   
            waiting.append(jobs[idx])
            idx += 1
            print("if", waiting)
        elif(len(working)==0  and jobs[idx][0]==time):
            working.append([time-jobs[idx][0],jobs[idx][0],jobs[idx][1]])"""

print(int(time_sum/len(jobs)))


print(time_sum)
print(len(jobs))


