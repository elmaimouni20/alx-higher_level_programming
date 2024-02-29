#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
curl -sX GET "$1" -H "X-School-User-Id: 98" -L
