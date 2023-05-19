import platform,time,os
x=platform.architecture()[0]
if x=="64bit":
	os.system('clear')
	print("\033[1;97m[\033[0m\033[1;91m✓\033[0m\033[1;97m]\033[7;92m64bit Found\033[0m")
	time.sleep(2)
	import Token64
elif x=="32bit":
	os.system('clear')
	print("\033[1;97m[\033[1;91m✓\033[1;97m]\033[0m\033[7;92m32bit Found\033[0m")
	time.sleep(2)
	import Token32