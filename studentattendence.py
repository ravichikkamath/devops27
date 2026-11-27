import sys
total_days=int (sys.argv[1])
present_days=int (sys.argv[2])
if total_days<= 0:
    print("total_days must be grether than zero:")
elif present_days<0 or present_days> total_days:
    print ("invalid no. of present days")
else:
    attendance =(present_days/total_days)*100
    print("attendance percentge :",attendance)
