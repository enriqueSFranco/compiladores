%{
    #include "calculadora.tab.h"
%}


%%

[0-9]+      {
                /*forma de comunicar el analizar lexico con el sitactico*/
                yylval = atoi(yytext); /*yylval sera el $n*/
                return NUMERO;
            }
[\n]        return '\n';

[+]         return '+';

%%