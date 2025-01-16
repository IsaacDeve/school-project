import random as r

lessons = ["PE", "Computer science", "Math", "Biology", "Media", "Guitar"]

current_lessons = []
banned_indexes = []
tempnum = 0
how_many_lessons = 10

#for l in lessons:
   # print(l)

for l in lessons:
    if tempnum<=how_many_lessons:
        tempnum+=1
        num = r.randint(0, len(lessons)-1)
        current_lessons.append(lessons[num])
        lessons.remove(lessons[num])
        
for l in current_lessons:
    print(l)
    
