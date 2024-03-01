#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
