TARGET = main
CC = gcc
LIBS = -lm
SRCS = main.c pow2.c sqrt2.c div2.c
OBJS = $(SRCS:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) -o $@ $^ $(LIBS) 

%.o: %.c
	$(CC) -c $< $(LIBS)

clean:
	rm -f $(OBJS)

distclean: clean
	rm -f $(TARGET)


