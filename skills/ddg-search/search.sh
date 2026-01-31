#!/bin/bash
QUERY=$(echo "$*" | sed "s/ /+/g")
# Requesting Bing with a standard mobile User-Agent sometimes simplifies the layout
UA="Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
curl -sL "https://www.bing.com/search?q=$QUERY" -A "$UA" | \
grep -oE "https?://[^\"'<> ]+" | \
grep -vE "bing|microsoft|w3\.org|live\.com|schema\.org|gstatic\.com|apple\.com" | \
head -n 10
