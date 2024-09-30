#!/bin/bash

curl https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg > cat.png

aws s3 cp cat.png s3://ds2022-zzz2bx/

aws s3 presign --expires-in 604800 s3://ds2022-zzz2bx/cat.png

https://ds2022-zzz2bx.s3.us-east-1.amazonaws.com/cat.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2OAJTVODZSWX2RE4%2F20240930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240930T030847Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=9e3fcb59bb4dd02781f2938292b8b59edbe290c59b21581c22d4f2f18d2263b2
