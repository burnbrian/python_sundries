#!/bin/bash

# URL
url="https://localhost/login?next=%2F"
for i in {1..10000}
do
	curl -k $url &
	curl -k $url &
	curl -k $url &
	curl -k $url &
	curl -k $url &	
done
