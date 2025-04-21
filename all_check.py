import os
import sys

def check_rei():
	'''
	Retorna True si el compu tiene pendiente un reinicio
	'''
	return os.path.exists('/run/reboot-required')

def main():
	if check_rei():
		print('Reinicio pendiente')
		sys.exit(1)
	if disk_full():
		print('disco lleno')
		sys.exit(1)
	print('Todo ok.')
	sys.exit(0)

main()