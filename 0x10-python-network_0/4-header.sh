#!/usr/bin/env bash
# Send a GET request to a given URL with a header variable.
# A header variable X-School-User-Id must be sent with the value 98

curl -sH "X-School-User-Id: 98" "$1"
