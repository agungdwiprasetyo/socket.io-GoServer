# Web Server for Socket.IO using Golang

## Install Golang on Ubuntu

Download and install Golang:
```sh
$ sudo add-apt-repository ppa:gophers/archive
$ sudo apt-get update
$ sudo apt-get install golang-1.8  #latest version (Mar 2017)
$ sudo ln /usr/lib/go-1.8/bin/go /usr/bin/go1.8
```
Edit environment variable in ~/.bashrc :
```sh
$ export PATH=$PATH:/usr/local/go/bin
$ export GOPATH=$HOME/Go
$ export GOBIN=$GOPATH/bin
$ export PATH=$PATH:$GOPATH/bin
$ source ~/.bashrc
```

Get package for socket.io server-side:
```sh
$ go get github.com/googollee/go-socket.io
```

Compile main.go:
```sh
$ go build main.go
```

Run program:
```sh
$ ./main
```

Open ```localhost:1993``` 