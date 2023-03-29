Documentation:

This Python script automates the process of scraping image search results from Pinterest and downloading them to a folder with the same name as the user input. The script uses the Selenium WebDriver to navigate to the Pinterest search page and enter the user input as a search query. The script then scrolls through the page to retrieve the image source URLs of the search results, checks each URL against a list to avoid downloading duplicates, and downloads new images to the newly created folder using the urllib library.

The script has several customizable options, such as changing the folder location where the images are downloaded, adjusting the maximum number of errors tolerated, and choosing between restarting the script, quitting, or continuing when the error count is reached.

The script requires the Selenium and urllib libraries to be installed. The script is compatible with Windows, macOS, and Linux.

Usage:

To use the script, simply run it in a Python IDE or from the command line. When prompted, enter the name of the image you want to search for on Pinterest. The script will then navigate to the Pinterest search page and automatically begin downloading images to a newly created folder with the same name as the search query.

Customization:

The script can be customized by changing the following options:

Folder location: You can change the folder location where the images are downloaded by modifying the "inputname" variable in the "makefolder()" function.
Error count: You can adjust the maximum number of errors tolerated before prompting the user to choose between restarting the script, quitting, or continuing by modifying the "error_count" variable in the "lookforimages()" function.
Keyboard input: You can modify the script to automatically input the search query without prompting the user by changing the "inputname" variable in the "imagemain()" function.
Licensing:

This script is licensed under the GNU General Public License v3.0, which is a free, copyleft license for software and other kinds of works. This license gives users the freedom to use, modify, and distribute the software, as well as the right to access and modify the source code. However, any modifications made to the software must also be released under the same GPL license, ensuring that the software remains free and open source.

The GPL v3.0 is designed to protect the user's freedoms while also ensuring that the software remains free and open source for future generations. It is compatible with many other open source licenses and has been widely adopted by the open source community.
