# Lab: Build a Simple Server

## Introduction

In this lab, I learned how to build a simple HTTP web server that supports HTML documents and pictures like PNGs and JPEGs. This lab only uses the Sockets library and knowledge of the different types of HTTP requests to facilitate the connections.

Usage: python3 server.py

## Collaboration/Citations

I used [RFC 7231](https://datatracker.ietf.org/doc/html/rfc7231) of the HTTP/1.1 to understand how to format my HTTP response headers. I also used the course textbook as a reference for building the initial server.

## Process

This lab was done in accordance with the instructions outlined in the [Build a Server Lab](https://courses.cs.usna.edu/IC322/#/assignments/week02/lab-build-a-server). Personal Additions: Two Test images (c_meme.png and dns_haiku.jpg) and 404.html.

## Questions

### Q1: Why are we focusing on the TCP server in this lab rather than the UDP server?

In this lab, we are focusing on TCP servers over UDP servers because TCP provides reliable, connection-oriented data transmission, that is crucial for web applications where correct delivery and order of data packets matter for functionaliy (displaying requested objects). UDP is not sufficient for a web server because it lacks reliability and is better used for loss-tolerant applications like real-time communication or multimedia streaming.

### Q2: Look carefully at Figure 2.9 (General format of an HTTP response message). Notice that there's a blank line between the header section and the body. And notice that the blank line is two characters: `cr` and `lf`. What are these characters and how do we represent them in our Python response string?

The cr character represents a 'Carriage Return', which is denoted by \r in Python strings. The lf character represents a 'Line Feed', denoted by \n in Python strings. These characters are typically used together to indicate the end of a line in text files. In the context of HTTP response messages, a blank line separating the header section and the body is represented by \r\n\r\n in Python strings. This sequence of characters ensures proper formatting of the response message according to the HTTP protocol.

### Q3: When a client requests the `/index.html` file, where on your computer will your server look for that file?

When a client requests the /index.html file from the server, the server will look for that file in the directory where the server script is executed from (relative path).
