%{
    #include <stdio.h>  /* For printf, etc. */
    #include <stdlib.h>
    #include <math.h>   /* For pow, used in the grammar.  */
    #include <string.h>
    #include "calc.h"   /* Contains definition of 'symrec'.  */

    int yydebug = 0;
    int yylex (void); /* llamando a la funcion yylex */
    void yyerror (char const *); /* funcion para el manejador de errores */
%}


%define api.value.type union /* Generate YYSTYPE from these types:  */
%token <double>  NUM         /* Simple double precision number.  */
%token <symrec*> VAR FNCT    /* Symbol table pointer: variable and function.  */
%type  <double>  exp

%precedence '='
%left '-' '+'
%left '*' '/'
%precedence NEG /* negation--unary minus */
%right '^'      /* exponentiation */


%% /* declaracion de la gramatica libre de contexto */
input: /* vacio */ | input line 
;

line: '\n'
      | exp '\n'   { printf ("%.10g\n", $1); }
      | error '\n' { yyerrok;                }
;

exp:  NUM                   { $$ = $1;                         }
    | VAR                   { $$ = $1->value.var;              }
    | VAR '=' exp           { $$ = $3; $1->value.var = $3;     }
    | FNCT '(' exp ')'      { $$ = (*($1->value.fnctptr))($3); }
    | exp '+' exp           { $$ = $1 + $3;                    }
    | exp '-' exp           { $$ = $1 - $3;                    }
    | exp '*' exp           { $$ = $1 * $3;                    }
    | exp '/' exp           { $$ = $1 / $3;                    }
    | '-' exp  %prec NEG    { $$ = -$2;                        }
    | exp '^' exp           { $$ = pow ($1, $3);               }
    | '(' exp ')'           { $$ = $2;                         }
;
/* fin de la gramatica  */
%%

struct init
{
  char const *fname;
  double (*fnct) (double);
};

struct init const arith_fncts[] =
{
  { "abs", fabs  },
  { "asin", asin },
  { "acos", acos },
  { "atan", atan },
  { "cos",  cos  },
  { "exp",  exp  },
  { "ln",   log  },
  { "sin",  sin  },
  { "sqrt", sqrt },
  { 0, 0 },
};

/* The symbol table: a chain of 'struct symrec'.  */
symrec *sym_table;

/* Put arithmetic functions in table.  */
static
void
init_table (void)
{
  int i;
  for (i = 0; arith_fncts[i].fname != 0; i++)
    {
      symrec *ptr = putsym (arith_fncts[i].fname, FNCT);
      ptr->value.fnctptr = arith_fncts[i].fnct;
    }
}

/* manejador de errores */
void yyerror(char *s)
{
  printf ("ERROR: %s\n", s);
  exit(0);
}

int main (int argc, char const* argv[])
{
  int i;
	printf("\nCalculadora\n");
  /* Enable parse traces on option -p.  */
  for (i = 1; i < argc; ++i)
    if (!strcmp(argv[i], "-p"))
      yydebug = 1;
  init_table ();
  return yyparse ();
}
