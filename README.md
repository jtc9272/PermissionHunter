# PermissionHunter
PERMISSION HUNTER

On first run, you will need to enter the paths to adb, aapt, and keytool when prompted. 
They will be saved in config.txt and automatically used in the future.

When prompted to enter a package, if it errors out you spelled the package name wrong. 
Use -l at that prompt to see all available packages

Each package will get its own directory, and in it will be the files containing permissions and 
cert information as well as the unzipped apk. Right now, the zip file and apk file are not being 
moved for some reason, that will be fixed in the future

When prompted to classify the app, it will save the number and package name to ResultsDatabase
Running the tool with the -l flag will prompt you to enter a classification number and then will
list all package data for any app of that classification.
