import subprocess
import os
import sys
import os.path

def list(input):
	packagesToList = []
	for line in open('ResultsDatabase.txt','r'):
		parts = line.split(' ')
		if parts[0].strip() == input.strip():
			print(parts[1].strip())
			for line1 in open(parts[1].strip()+'/permissionsList.txt'):
				print(line1.strip())
			print('\n')
			for line2 in open(parts[1].strip()+'/certFile.txt'):
				print(line2.strip())
			print('\n')
			print('------------------------------------------------------------------')
			print('\n')
			
	print(packagesToList)
	exit()
			

def newFile(command1):
	for line in fileVerb:
		line = line[8:]
		line = line.split('=')
		packagePath = line[0]
		parts = packagePath
		parts = parts.split('/')
		for part in parts:
			part = part.split("-")
			if part[0] == command1:
				print("Package Found")
				pathToApk = line[0]
				break
	fileVerb.close()
	print("Pulling APK...")
	os.system('"'+pathToAdb+'adb\" pull '+pathToApk)
	holder = line[0]
	holderparts = holder.split('/')
	#os.rename(holderparts[-1],command1+'/'+holderparts[-1])
	print("APK Pulled!")
	if os.path.isdir(command1) == False:
		os.system('mkdir '+command1)
		os.rename('packageList.txt',command1+'/packageList.txt')
		os.rename('packageListVerbose.txt',command1+'/packageListVerbose.txt')
	APKNameList = line[0]
	APKNameList = APKNameList.split("/")
	APKName = APKNameList[-1]
	pathToCWD = os.getcwd()
	print(APKName+ " saved to "+pathToCWD+"\\"+command1)
	if config == 2:
		pathToAAPT = input("Enter path to aapt: ")
		configFile.write(pathToAAPT)
		configFile.write("\n")
	if config == 1:
		pathToAAPT = configFile.readline().strip()
		print("Using AAPT path "+pathToAAPT+" from config file")
	if config ==0:
		pathToAAPT = input("Enter path to aapt: ")
	os.system('"'+pathToAAPT+'aapt" d permissions '+APKName+' > permissionsVerbose.txt')
	print("Permissions pulled to permissionsVerbose.txt")
	print('\n')
	print('Please Classify the app as one of the following:')
	print('   1 - Game')
	print('   2 - Social Media')
	print('   3 - Utilities')
	print('   4 - Finance')
	print('   5 - Digital Media')
	print('   6 - Other')
	classification = input(': ')
	if  int(classification) <= 0 or int(classification) >= 7:
		print('Improper Input. Please use an option from above')
		classification = input(': ')
	outLine = ""
	outLine += classification
	outLine += " "
	outLine += command1
	outfile.write(outLine)
	outfile.write('\n')
	outfile.close()
	signature = []
	dangerous = []
	normal = []
	otherAndroid = []
	custom = []
	sigFile = open('PROTECTION_SIGNATURE.txt','r')
	dangFile = open('PROTECTION_DANGEROUS.txt','r')
	normFile = open('PROTECTION_NORMAL.txt','r')
	
		
	if os.path.isdir(command1+'/'+command1):
		print('\n')
		print("Directory exists, skipping extraction")
	else:
		print('\n')
		print("Converting APK to zip file")
		os.system('copy '+APKName+' '+command1+'.zip > nul')
		print("Unzipping")
		os.system('powershell.exe Expand-Archive '+pathToCWD+'\\'+command1+'.zip '+pathToCWD+'\\'+command1+'\\'+command1)
		print("Finished")
		print('\n')
	if config == 2:
		pathToKeytool = input("Enter path to keytool: ")
		configFile.write(pathToKeytool)
		configFile.write("\n")
	if config == 1:
		pathToKeytool = configFile.readline().strip()
		print("Using Keytool path "+pathToKeytool+" from config file")
	if config ==0:
		pathToKeytool = input("Enter path to keytool: ")

	print("Searching for RSA file...")
	os.system("cd "+command1+'/'+command1+'/META-INF/  & dir > fileList.txt')
	searchRSA=open(command1+'/'+command1+'/META-INF/'+'fileList.txt','r')
	RSAFile = " "

	#searchRSA = open('fileList.txt','r')

	for line in searchRSA:
		parts = line.split('.')
		if parts[-1].strip() == 'RSA':
			print("Found RSA file")
			words=line.split()
			RSAFile = words[-1]
			print("PERMISSION SUMMARY:")
			permissionsFile = open('permissionsVerbose.txt','r')
			count = 1
			classified = 0
			for permline in permissionsFile:
				if count == 1:
					print(permline)
					count +=1
				else:
					longperm = permline[23:-2]
					permparts = longperm.split('.')
					if 'android' not in permparts:
						custom.append(longperm)
					else:
						sigFile = open('PROTECTION_SIGNATURE.txt','r')
						dangFile = open('PROTECTION_DANGEROUS.txt','r')
						normFile = open('PROTECTION_NORMAL.txt','r')
						for line in sigFile:
							if line.strip() == permparts[2].strip():	
								signature.append(longperm)
								classified = 1
						for line in dangFile:
							if line.strip() == permparts[2].strip():
								dangerous.append(longperm)
								classified = 1
						for line in normFile:
							if line.strip() == permparts[2].strip():
								normal.append(longperm)
								classified = 1
						if classified == 0:
							otherAndroid.append(longperm)
						classified = 0
						sigFile.close()
						normFile.close()
						dangFile.close()
			permOutFile = open('permissionsList.txt','w')
			print('\n')
			print('PROTECTION_DANGEROUS')
			permOutFile.write('PROTECTION_DANGEROUS')
			permOutFile.write('\n')
			for perm in dangerous:
				print(perm)
				permOutFile.write(perm)
				permOutFile.write('\n')
			print('\n')
			print('PROTECTION_SIGNATURE')
			permOutFile.write('PROTECTION_SIGNATURE')
			permOutFile.write('\n')
			for perm in signature:
				print(perm)
				permOutFile.write(perm)
				permOutFile.write('\n')
			print('\n')
			print('PROTECTION_NORMAL')
			permOutFile.write('PROTECTION_NORMAL')
			permOutFile.write('\n')
			for perm in normal:
				print(perm)
				permOutFile.write(perm)
				permOutFile.write('\n')
			print('\n')
			print('OTHER ANDROID PERMISSIONS')
			permOutFile.write('OTHER ANDROID PERMISSIONS')
			permOutFile.write('\n')
			for perm in otherAndroid:
				print(perm)
				permOutFile.write(perm)
				permOutFile.write('\n')
			print('\n')
			print('CUSTOM')
			permOutFile.write('CUSTOM')
			permOutFile.write('\n')
			for perm in custom:
				print(perm)
				permOutFile.write(perm)
				permOutFile.write('\n')
			permOutFile.close()
			os.rename('permissionsList.txt',command1+'/permissionsList.txt')
			print('\n')
			print('CERT DETAILS')
			print(RSAFile)
			os.system('"'+pathToKeytool+'keytool" -printcert -file '+command1+'/'+command1+'/META-INF/'+RSAFile)
			os.system('"'+pathToKeytool+'keytool" -printcert -file '+command1+'/'+command1+'/META-INF/'+RSAFile + ' > certFile.txt ' )
			os.rename('certFile.txt',command1+'/certFile.txt')
			break



config = 0
outfile = open('ResultsDatabase.txt','a')

if os.path.isfile("config.txt"):
	config = 1
	configFile = open('config.txt','r')
else:
	print("No configuration file found. Settings from this run will be saved")
	config = 2
	configFile = open('config.txt','w')
if len(sys.argv) ==2 and sys.argv[1]=='-l':
	print('Please Enter the type of app to list:')
	print('   1 - Game')
	print('   2 - Social Media')
	print('   3 - Utilities')
	print('   4 - Finance')
	print('   5 - Digital Media')
	print('   6 - Other')
	input = input()
	list(input)
if len(sys.argv)>2:
	print("Too many arguments. Please only use -f")
	exit()
if config == 2:
	pathToAdb = input("Enter path to adb.exe: ")
	configFile.write(pathToAdb)
	configFile.write("\n")
if config == 1:
	pathToAdb = configFile.readline().strip()
	print("Using ADB path "+pathToAdb+" from config file")
if config ==0:
	pathToAdb = input("Enter path to adb.exe: ")
os.system('"'+pathToAdb+'adb" shell pm list packages > packageList.txt')
os.system('"'+pathToAdb+'adb" shell pm list packages -f > packageListVerbose.txt')
print('\n')
command1 = input("Enter package name, or -l to list available packages: ")
if command1 == "-l":
	file = open('packageList.txt','r')
	for line in file:
		parts = line.split('.')
		if len(parts) > 1:
			if parts[0]== 'android':
				pass
			if parts[1] == 'android':
				pass
			else:
				print(line[8:].strip())
	file.close()
	command1 = input("Enter package name: ")
fileVerb = open('packageListVerbose.txt','r')
if os.path.isdir(command1) == False:
	newFile(command1)
else:
	print('App already analyzed, retrieving stored info...')
	print('\n')
	filePath = command1+'/permissionsList.txt'
	outFile = open(filePath,'r')
	for line in outFile:
		print(line.strip())
	filePath = command1+'/certFile.txt'
	outFile = open(filePath,'r')
	print('\n')
	print('CERT DETAILS')
	for line in outFile:
		print(line.strip())






		




