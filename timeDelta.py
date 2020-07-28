import datetime

#n = int(input())
#for _ in range(n):
#    t1 = input()
#    t2 = input()
#    delta = time_delta(t1, t2)
    
#d = datetime.datetime(2020,6,21,13,54,36)
s1 = 'Sun 10 May 2015 13:54:36 -0700'.split()
s2 = 'Sun 10 May 2015 13:54:36 -0000'.split()

d1 = ' '.join(s1[1:5])
d2 = ' '.join(s2[1:5])

print(datetime.datetime(s1[3],s1[2],s1[1],s1[4]))
#print(d2)

#print(d2-d1)
#delta = datetime.datetime.strptime('Sun 10 May 2015 13: 54: 36 - 0700', %Y-%B-%d)

#print(delta)

#def time_delta(t1, t2):

#print(d)
