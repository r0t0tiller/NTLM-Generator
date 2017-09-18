import hashlib,binascii
import sys

def generate():

	if len(sys.argv) < 2:

		print "usage: ntlm_gen.py file.txt"

		sys.exit(1)

	file = sys.argv[1]

	f = open(file, 'r')

	for word in iter(f):

		hash = hashlib.new('md4', word.encode('utf-16le')).digest()
		print binascii.hexlify(hash)

	f.close()

generate()
