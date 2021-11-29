# OpenBracketsWebsite

## THIS REPOSITORY IS NOW DEPRECATED. PLEASE SEE [https://github.com/qpwoeirut/OpenBrackets-website](https://github.com/qpwoeirut/OpenBrackets-website) FOR THE CURRENT VERSION OF THE WEBSITE.

This repository contains the source code for [openbrackets.us](http://openbrackets.us/).
The actual website is hosted using AWS S3.

This website was developed with PyCharm's builtin server.
Due to this [quirk](https://youtrack.jetbrains.com/issue/WEB-47264) of the server, "/OpenBracketsWebsite" needs to be added to all links for local development.
This prefix is stripped out for production by [build.py](/build.py).

build.py also places the navbar and footer code directly into the HTML code on each page.
This avoids any issues where the navbar/footer doesn't load for a few seconds, and it helps search engines discover the website.
