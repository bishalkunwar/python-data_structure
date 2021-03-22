#Python code to implement sets;

Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)

#Accessing values in sets:
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
 
for d in Days:
	print(d)

#adding values on sets:
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
Days.add("Sun")
print(Days)


#removing items from sets;

Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])
 
Days.discard("Sun")
print(Days)

#union of sets:
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)

#intersection of sets:
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)