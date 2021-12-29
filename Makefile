IDIR =../include
CC=gcc
CFLAGS=-I$(IDIR) src/keygen.c

_DEPS = keygen.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))


key.gen: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ 