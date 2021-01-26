
%{
    #include <stdio.h>
    #include <stdlib.h>

    int yylex(void); /* cabecera */

    /*manejador de error*/
    void yyerror(char *mensaje) {
        printf("ERROR: %s",mensaje);
        exit(0);
    }
%}


%token NUMERO

%%
programa :                          
;

programa: linea programa            
;

linea: '\n'                             
;

linea: expresion '\n'                   { printf("Valor = %d\n", $1); }              
;

expresion: NUMERO                       { $$ =  $1; }
;

expresion: expresion '+' expresion      {$$ = $1 + $3;}

%%