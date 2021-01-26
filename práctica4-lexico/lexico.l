%{
/*codigo C*/
#include<stdio.h>

int i = 0;
%}

/* variables -> tipo_dato id <operador asignacion> valor || tipo_dato id <separador>; */
DIGITO    			[0-9]

KEYWORDS "auto"|"break"|"case"|"const"|"continue"|"default"|"do"|"else"|"enum"|"extern"|"for"|"goto"|"if"|"register"|"return"|"signed"|"sizeof"|"static"|"typedef"|"union"|"unsigned"|"volatile"|"while"

TIPOSDATO 			"char"|"int"|"long"|"short"|"float"|"double"|"void"

DIRECTIVAS			"#"[a-zA-Z]+

LIBS				"<"[a-z]+("."[a-zA-Z]+|"")">"

OPERADORES_ARITMETICOS 	("+"|"-"|"*"|"/"|"%")|"="|("+"|"-"|"*"|"/"|"%")"="|"++"|"--"

OPERADORES_COMPARACION 	"<"|">"|">="|"<="|"!="|"=="|"!"|"&&"|"||"

OPERADORES_BIT 		">>"|">>="|"<<"|"<<="|"~"|"&"|"&="|"|"|"|="|"^"|"^="

OPERADORES			{OPERADORES_ARITMETICOS}|{OPERADORES_COMPARACION}|{OPERADORES_BIT}

DELIMITADOR 			"{"|"}"|"["|"]"|"("|")"|";"|","

ID       			([a-zA-Z]|"_")([a-zA-Z0-9]|"_")*

NUMEROS 			{DIGITO}+"."{DIGITO}+|{DIGITO}+

SECUENCIAS_ESCAPE 		"\\""\""|"\\""n"

CARACTERES_ESPECIALES 		"."|" "|"'"|"#"|"?"|":"|"\\"|"@"

CHARS "'"({SECUENCIAS_ESCAPE}|[a-zA-Z0-9]|{CARACTERES_ESPECIALES}|{DELIMITADOR}|{OPERADORES}|{ID}|{KEYWORDS}|{TIPOSDATO}|{LIBS}|{DIRECTIVAS}|{NUMEROS})*"'"

STRINGS "\""({SECUENCIAS_ESCAPE}|[a-zA-Z0-9]|{CARACTERES_ESPECIALES}|{DELIMITADOR}|{OPERADORES}|{ID}|{KEYWORDS}|{TIPOSDATO}|{LIBS}|{DIRECTIVAS}|{NUMEROS})*"\""

CADENAS {STRINGS}|{CHARS}

COMENTARIOS_MULTIPLES "/""*"+([a-zA-Z0-9]|{CARACTERES_ESPECIALES}|{DELIMITADOR}|{OPERADORES}|{ID}|{KEYWORDS}|{TIPOSDATO}|{CADENAS}|{LIBS}|{DIRECTIVAS}|{NUMEROS}|{SECUENCIAS_ESCAPE})*"*"+"/"

COMENTARIOS_UNALINEA ("/"|"")"*"([a-zA-Z0-9]|{CARACTERES_ESPECIALES}|{DELIMITADOR}|{OPERADORES}|{ID}|{KEYWORDS}|{TIPOSDATO}|{CADENAS}|{LIBS}|{DIRECTIVAS}|{NUMEROS}|{SECUENCIAS_ESCAPE})*

COMENTARIOS {COMENTARIOS_UNALINEA}|{COMENTARIOS_MULTIPLES}


%%

{COMENTARIOS}		{ /*comentarios*/ 
				printf("<comentarios>\n"); 
			}

{LIBS}			{ /*comentarios*/ 
				printf("<libreria>\n"); 
			}
			
{SECUENCIAS_ESCAPE}	{ /*secuencias de escape*/ 
				printf("<secuencia de escape>\n"); 
			}	
		

{TIPOSDATO}		{/*tipo de dato C*/
				printf("<tipo de dato>");
			}

{NUMEROS}		{/*numeros*/
				printf("<numero>");
			}


{CADENAS}		{/*cadenas*/
				printf("<cadenas>");
			}


{DELIMITADOR} 		{/*separadores*/
				printf("<delimitador>"); 
			}

{KEYWORDS}		{/*palabras reservadas*/ 
				printf("<palabra reservada>");
			}


{OPERADORES}		{/*operadores*/  
				printf("<operador>"); 
			}
	
{ID}			{/*id*/
				printf("<id>");
			}

{DIRECTIVAS}		{/*directiva*/
				printf("<directiva>");
			}

%%



