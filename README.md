# Information-gathering-tool

Project 1 - Information Gathering Tool

Format:
Take screenshots of each and every task mentioned below, and prepare a report of the project in PDF format only.

Instructions:
Build a tool that will take any website name that the user provides and provide information such as location and IP address.

When the user provides the below-mentioned syntax, the command tool should be able to give information such as location and IP address.

Syntax :
python infotool.py <websiteurl>

Example Command
Python infotool.py google.com

Tasks:
1. Students are required to write a Python script.
2. The student will use Python libraries such as
    a. sys
    b. requests
    c. json
    d. sockets
3. To find the location information, you are required to make use of an API from ipinfo.io.

4 As the information obtained is required to be present in the JSON format, you can refer to the below API for your reference
https://ipinfo.io/<ip-address-from-sockets>/json
Kindly replace the <ip-address-from-sockets> with the IP address found after using the Python sockets.
