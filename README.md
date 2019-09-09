Application does not work correctly

It is possible to run the program, open http://127.0.0.1:5000/ and enter the following key when prompted
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.y5w4khCBL-iBkSyjgLfmMcGImc7UdCmSAXaK5ZmyG6M

Which will give you a result similar to {"Location":"Leeds","data":{"Max Temperature":"14.44 C","Sunset Time":"18:39:20"}}


CURL -H 'ACCEPT: APPLICATION/JSON' -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.y5w4khCBL-iBkSyjgLfmMcGImc7UdCmSAXaK5ZmyG6M" http://127.0.0.1:5000/weather\