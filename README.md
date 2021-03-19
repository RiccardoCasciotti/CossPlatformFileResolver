# CrossPlatformFileResolver
This program resolves compatibility issues with Mac files so that they can be used and viewed on other platforms and services such as OneDrive. More in detail:
- it renames all the files and folders which contain special characters such as * and many others by replacing the special character with _ ;
- it transforms all the .webloc files ( only Mac readables ) in URL files which are compatible with other platforms.
It creates a log.txt file in the given root directory for the webloc files:
- status=FIXED: error encountered but fixed and created a URL file successfully
- status=NOT FIXED: error encountered and not fixed, it creates .txt file where the link can be retrieved.
To be executed run: python3 main.py

Note: it has been developed using Python 3.8.2 64-bit
IMPORTANT: this program uses side-effect, so all the webloc files are going to be permantly deleted, while the files and folders just renamed.
