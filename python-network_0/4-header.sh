#!/bin/bash
# Send the required user ID header and display the response body.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
