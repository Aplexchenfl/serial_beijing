#ifndef __SERIAL_LIB_H__
#define __SERIAL_LIB_H__

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <termios.h>
#include <errno.h>
#include <string.h>
#include <pthread.h>
#include <signal.h>
#include <sys/time.h>

int set_opt(int fd,int nSpeed, int nBits, char nEvent, int nStop);

#endif
