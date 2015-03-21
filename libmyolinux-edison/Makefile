    all:
	gcc -c -Wall -Werror -fpic myolinux.c -I/opt/poky-edison/1.6.1/sysroots/core2-32-poky-linux/usr/include/
	gcc -shared -o libmyolinux.so myolinux.o -L/opt/poky-edison/1.6.1/sysroots/core2-32-poky-linux/lib/ -L/opt/poky-edison/1.6.1/sysroots/core2-32-poky-linux/ --sysroot /opt/poky-edison/1.6.1/sysroots/core2-32-poky-linux/
	rm -f myolinux.o
	export LD_LIBRARY_PATH=$(LD_LIBRARY_PATH):`pwd`
	gcc -L`pwd` -Wall -o example example.c -lmyolinux -I/opt/poky-edison/1.6.1/sysroots/core2-32-poky-linux/usr/include/ -L/opt/poky-edison/1.6.1/sysroots/core2-32-poky-linux/lib/ -L/opt/poky-edison/1.6.1/sysroots/core2-32-poky-linux/ --sysroot /opt/poky-edison/1.6.1/sysroots/core2-32-poky-linux/

    clean:
	rm -f libmyolinux.so
	rm -f example
