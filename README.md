## Read this!

This is a **modified version of [W3C-httpd(CERN httpd)](https://www.w3.org/Daemon/)**

A few lines of code were changed in order to build and run this project properly on modern systems.
No functional changes were made beyond compatibility fixes.

## Quick Start Guide

### 1. install csh
```
$ sudo apt-get install csh
```

### 2. Build file
**you should follow this order**
```
$ make
$ make clean
$ make
```

### 3. make **Document Root**
```
$ mkdir test_server
$ echo "<html><head></head><body>Hello World!</body></html>" > test_server/index.html
```


### 4. create config (httpd.conf)
```
# Be sure to set the correct absolute path!
echo "Pass /* /home/your_username/w3c-httpd/test_server/*" > httpd.conf
```

### 5. run
```
./Daemon/linux/httpd -v -r ./httpd.conf -p 8080
```

### 6. Open in browser
Visit : [localhost:8080/index.html](http://localhost:8080/index.html)



---

Below is original version of README.

---

This is a small upgrade release of the CERN server (a.k.a. W3C
httpd). It includes a set of bug fixes and some improvements. The
release comes ASIS - that is - there is _no_ support available. Take
it or leave it :-)

The release does only include source code, you must compile the binary
yourself.

THIS PACKAGE INCLUDES:
  * source code under the WWW directory [where this README file is]
    To compile just type

		make

    and binaries will appear in Daemon/xxx where xxx is your host's
    architecture, like sun4 or next.

  * README-SOCKS explaining how to compile and use SOCKSified httpd
  * server_root/ directory containing:
     * Sample configuration files for httpd in config/
	- httpd.conf for normal use as HTTP server
	- prot.conf for normal use as HTTP server with access control
	- proxy.conf for proxy use without caching
	- caching.conf for proxy use with caching
	- all.conf that contains all the configuration directives
	  understood by httpd

     * Sample icons in icons/
	- to be used for directory listings, and also for ftp listings
	  when using httpd as a proxy
	- simplist way to make use of the icons is to define the
	  server root directory to be server_root under this current
	  directory [where this README file sits], by specifying in
	  the configuration file:

		ServerRoot  /what/ever/server_root


ONLINE DOCUMENTATION for this software is in:

	http://www.w3.org/pub/WWW/Daemon/

Security bugs can be sent to

	httpd@w3.org

Remember to run httpd in VERBOSE MODE [with the -v or -vv command line
option] when things seem to be going wrong and attach the output to
your mail message.  This will make our job a lot easier.

If httpd crashes and a core image is generated, run "dbx /path/httpd"
and say "where" to see where the execution was when the program
crashed.

Have fun!
