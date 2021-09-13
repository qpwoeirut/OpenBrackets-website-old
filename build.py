# This program takes all the folder paths in the pages and strips out the "/OpenBracketsWebsite" from them
# Due to https://youtrack.jetbrains.com/issue/WEB-47264, "/OpenBracketsWebsite" needs to be added for local development
# When uploading the files to the server, that path prefix needs to be removed
# This program will create a copy of the file hierarchy in /build, with the "/OpenBracketsWebsite" prefix removed


import os
import shutil


DEBUG = True
OLD_DIR = "/OpenBrackets-website/"
NEW_DIR = "/OpenBrackets-website/build/" if DEBUG else '/'

if os.path.exists("./build"):
    shutil.rmtree("./build")

with open("navbar.html", 'r') as file:
    navbar_html = file.read()
with open("footer.html", 'r') as file:
    footer_html = file.read()

ignored_files = shutil.ignore_patterns("build", "*.py", ".*", "README.md", "navbar.html", "footer.html", "*0.png", "*0.jpg")
shutil.copytree(".", "./build", ignore=ignored_files, dirs_exist_ok=True)

for directory, _, filenames in os.walk('./build'):
    html_files = [directory + '/' + fn for fn in filenames if fn.endswith('.html') or fn == "setActiveNav.js"]
    for html_file in html_files:
        with open(html_file, 'r') as file:
            text = file.read()
        text = text.replace("NAVBAR PLACEHOLDER", navbar_html).replace("FOOTER PLACEHOLDER", footer_html)
        text = text.replace(OLD_DIR, NEW_DIR)
        with open(html_file, 'w') as file:
            file.write(text)

print("Done")
if DEBUG:
    print("Remember to set DEBUG to False before deploying!")