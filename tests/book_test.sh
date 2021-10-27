#!/bin/bash

echo "############ POST TEST ###########"
response=$(curl -s -X POST http://localhost:5000/books/create/dziady)
echo -e "$response"
id=$(echo -e "$response" | grep id | cut -d' ' -f 4 | cut -d',' -f 1)

echo "############ GET TEST ############"
response=$(curl -s http://localhost:5000/books/?id=$id)
echo -e "$response"

echo "############ PATCH TEST ##########"
response=$(curl -s -X PATCH http://localhost:5000/books/update/$id?title=ferdydurke)
echo -e "$response"

echo "############ DELETE TEST #########"
response=$(curl -s -X DELETE http://localhost:5000/books/delete/$id)
echo -e "$response"
