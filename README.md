<h1>OWM-Application</h1>
<p>A short experiment for a job interview I made. Thank you to * for allowing this to be public</p>

<h2>cURL</h2>
<p>Application works correctly... to an extent.
<br>Try the following in cURL:</p>
CURL -H "ACCEPT: APPLICATION/JSON" -H "Authorization: BEARER eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.y5w4khCBL-iBkSyjgLfmMcGImc7UdCmSAXaK5ZmyG6M" http://127.0.0.1:5000/weather
<p><br>Please note this was designed for <strong>Windows</strong> cURL, not Linux cURL.
<br>Additional Rules: BEARER must be in uppercase or it won't work. 

<h2>Web Browser + IDE</h2>
<p>It is possible to run the program, open http://127.0.0.1:5000/ while running in an IDE. <em>(I made this in PyCharm)</em> and enter the following key when prompted in the console:</p>
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2NhdGlvbiI6IkxlZWRzIiwiYXBwSUQiOiJjMDI0ZTg1Y2VmOGYwZmM5MjhjM2YwZWY4NWQ3YWQwMCJ9.y5w4khCBL-iBkSyjgLfmMcGImc7UdCmSAXaK5ZmyG6M

<h2>Result</h2>
Running either case will give you a result similar to {"Location":"Leeds","data":{"Max Temperature":"14.44 C","Sunset Time":"18:39:20"}}