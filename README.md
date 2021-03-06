# OpenBracketsWebsite

This repository contains the source code for [openbrackets.us](http://openbrackets.us/).
The actual website is hosted using AWS S3.

This website was developed with PyCharm's builtin server.
Due to this [quirk](https://youtrack.jetbrains.com/issue/WEB-47264) of the server, "/OpenBracketsWebsite" needs to be added to all links for local development.
This prefix is stripped out for production by [strip_path_prefixes.py](/strip_path_prefixes.py).
