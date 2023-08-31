teste: functions.o teste.o 
	gcc -o teste teste.o functions.o -lm 

functions.o: functions.c
	gcc -c functions.c

distclean:
	rm -f teste *.o

teste.o: teste.c
	gcc -c teste.c