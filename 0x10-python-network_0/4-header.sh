#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -sX GET "$1" -H "X-School-User-Id: 98" -L
