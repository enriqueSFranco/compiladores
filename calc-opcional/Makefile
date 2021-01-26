run: a.out
	./a.out
clean: 
	rm -f a.out main.o calc.o mfcalc.tab.* lex.yy.*
lex.yy.c: mfcalc.l mfcalc.tab.c calc.h
	flex mfcalc.l
mfcalc.tab.c: mfcalc.y
	bison -d mfcalc.y
lex.yy.o: lex.yy.c
	gcc -c lex.yy.c
mfcalc.tab.o: mfcalc.tab.c
	gcc -c mfcalc.tab.c
calc.o: calc.c
	gcc -c calc.c
a.out: lex.yy.o mfcalc.tab.o calc.o
	gcc mfcalc.tab.o lex.yy.o calc.o -lm -ll
