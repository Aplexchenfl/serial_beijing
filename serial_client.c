#include "serial_lib.h"

int main(void)
{
    char *devname = "/dev/ttyS2", readchr[] = "01234567890abcd";
    int fd = open(devname, O_RDWR|O_NOCTTY|O_NDELAY);
    if (fd < 0)
    {
        perror(devname);
        return -1;
    }

    set_opt(fd, 115200, 8, 'n', 1);
    while(1)
    {
        bzero(readchr, sizeof(readchr));
        read(fd, readchr, sizeof(readchr));
        printf("%s\n", readchr);

        sleep(2);
    }

    close(fd);
    return 0;
}
