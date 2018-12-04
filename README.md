# PermissionHunter


On first run, you will need to enter the paths to adb, aapt, and keytool when prompted. 
They will be saved in config.txt and automatically used in the future.

When prompted to enter a package, if it errors out you spelled the package name wrong. 
Use -l at that prompt to see all available packages

The tool checks all of the permissions in the app against Androids list of Normal, Dangerous, 
and Signed permissions and then lists them as well as custom and other unclassified android 
permissions.

Each package will get its own directory, and in it will be the files containing permissions and 
cert information as well as the unzipped apk. 

When prompted to classify the app, it will save the number and package name to ResultsDatabase
Running the tool with the -l flag will prompt you to enter a classification number and then will
list all package data for any app of that classification.

