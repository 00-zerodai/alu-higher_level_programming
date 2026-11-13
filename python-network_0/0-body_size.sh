#!/bin/bash
# Display the size in bytes of the response body.
curl -s "$1" | wc -c
