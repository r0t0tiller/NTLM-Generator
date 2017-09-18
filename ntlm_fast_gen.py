import hashlib,binascii
import sys
import threading
from threading import Lock

reload(sys)
sys.setdefaultencoding('utf-8')

def generate():

	for word in iter(f):

		hash = hashlib.new('md4', word.encode('utf-16le')).digest()
		lock.acquire()
		print binascii.hexlify(hash)
		out.write(binascii.hexlify(hash)+'\n') # File output
		lock.release()

if __name__ == "__main__":

	if len(sys.argv) < 4:

		print "usage: ntml_fast_gen.py input.txt <number of threads> output.txt"

		sys.exit(1)

	file = sys.argv[1]

	f = open(file, 'r')

	threads = int(sys.argv[2])
	jobs = []

	outfile = sys.argv[3]

	out = open(outfile, 'w')

	lock = Lock()

	for x in range(0, threads):

		thread = threading.Thread(target=generate)
		jobs.append(thread)

	for j in jobs:

		j.start()

	for j in jobs:

		j.join()

	f.close()
