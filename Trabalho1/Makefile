TARGET = main
CC = gcc
LIBS = -lm
CFLAGS = -Wall -I ./$(INCDIR)

SRCDIR = src
OBJDIR = obj
INCDIR = include

SRC = $(wildcard $(SRCDIR)/*.c)
OBJ = $(patsubst $(SRCDIR)/%.c,$(OBJDIR)/%.o,$(SRC))

all: $(TARGET)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^ $(LIBS) 

$(OBJDIR)/%.o: $(SRCDIR)/%.c
	$(CC) $(CFLAGS) -c $< $(LIBS) -o $@

clean:
	rm -f ./obj/*

distclean: clean
	rm -f $(TARGET)

run:
	./main


