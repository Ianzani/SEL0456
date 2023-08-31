ALL = main

all: $(ALL)

main: functions.o teste.o 
	gcc -o $@ $^ -lm 

%.o: %.c
	gcc -c $<

clean:
	rm -f *.o

distclean: clean
	rm -f $(ALL)