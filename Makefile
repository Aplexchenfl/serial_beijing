
all :
	arm-linux-gnueabihf-gcc serial_server.c  serial_lib.c -o serial_server
	arm-linux-gnueabihf-gcc serial_lib.c  serial_client.c  -o serial_client

clean :
	rm serial_server -rf
	rm serial_client -rf
