from platform import system
import os

working_platform = system()
print("[*] working OS : " + working_platform.lower())
# really cool module, that generate requirements.txt file for any project based on imports 
# the requirements.txt contains the list of imported module missing in the working system.
os.system("pip3 install pipreqs")	#installing the pipreqs itself if its missing.
os.system("pipreqs --force .")		# generates the requirements.txt for the current directory python files
									#--force to replace the previous requirements.txt if exists.
os.system("pip3 install -r requirements.txt")	#install all the missing modules.
# os.remove("./requirements.txt")	#uncomment to remove the requirements.txt automatically.


'''
Source:
https://github.com/bndr/pipreqs
https://stackoverflow.com/questions/46419607/how-to-automatically-install-required-packages-from-a-python-script-as-necessary/46419642#:~:text=You%20can%20use%20pipreqs%20to,pip%20install%20pipreqs%20pipreqs%20.
'''