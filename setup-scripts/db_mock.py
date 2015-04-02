

u = Student()
u.username="Teddy"
u.pod_number = int(u.next_pod())
db.session.add(u)
db.session.commit()

v = Student()
v.username="Wei"
v.pod_number = v.next_pod()
db.session.add(v)
db.session.commit()

w = Student()
w.username="Damien"
db.session.add(w)
db.session.commit()

x = Student()
x.username="Yang"
db.session.add(x)
db.session.commit()





pods = Student.query.order_by('pod_number').all()




result = False
pods = Student.query.order_by('pod_number')


 for i in range(1, 255):
    for pod in pods:
        if i < int(pod.pod_number):
            print "i=%r : pod=%r : u=%r" % (i, pod.pod_number, pod.username)
            result = i
            break
    if result:
        break

print result


for i in range(1, 255):
			print "item: {0}".format(i)
			if i == pod.pod_number:
				break
			else:
				return i

from pprint import pprint as pp
def next_pod():
	MAX_PODS = 255
	new_pod_id = 1
	pods = Student.query.order_by('pod_number').all()
	for pod in pods:
		print "Pod: {0} / {1}".format(pod.username, pod.pod_number)
		if new_pod_id == pod.pod_number:
			print "Found ID: {0}".format(pod.pod_number)
			next
		else:
			print "Unused: {0}".format(new_pod_id)
			return new_pod_id
		new_pod_id = new_pod_id + 1
		
	return False

next_pod()