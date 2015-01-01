#!/usr/bin/env python
# -*- coding:utf-8 -*-

import cgi
import mraa
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/serial':
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                                    environ={'REQUEST_METHOD':'POST'})
            code = form['code'].value
            print code

            if code == "led1":
                buzzer.write(1)
            elif code == "led2":
                buzzer.write(1)
            elif code == "reset":
                led.write(0)
                buzzer.write(0)
            self.send_response(100)
            self.send_header('Content-type', 'text/html')
            return
        return self.do_GET()

led = mraa.Gpio(13)
buzzer = mraa.Gpio(4)

server = HTTPServer(('', 8080), MyHandler).serve_forever()

