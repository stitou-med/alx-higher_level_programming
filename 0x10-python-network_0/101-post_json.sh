#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument,displays the body
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
