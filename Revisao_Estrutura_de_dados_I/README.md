RESUMO DE ESTRUTURA DE DADOS I

Nesta disciplina, revisamos as estruturas de decisão e repetição e aprofundamos os estudos em vetores, matrizes e structs utilizando a linguagem C.




Questão de uma prova da disciplina:

Fernanda é a bibliotecária da escola e precisa de sua ajuda para organizar as informações dos livros disponíveis na biblioteca. Ela quer saber quantos livros existem por categoria e por estado de conservação.

Sua tarefa é criar um programa em C que:

Leia os dados de 15 livros.
Para cada livro, leia:
Categoria (1 para matemática, 2 para ciências e 3 para geografia)
Conservação (1 para novo, 2 para bom e 3 para ruim)
Ao final, mostre:
Quantidade de livros por categoria
Quantos livros eram novos na categoria matemática


Regras:

Use estrutura de repetição
Use estrutura de decisão
Não pode usar estrutura de dados composta
Não pode usar modularização
Resposta


#include <stdio.h>

int main() {

  int i =0;

  int categoria = 0;

  int conservacao = 0;

  int contadorM= 0;

  int contadorC= 0;

  int contadorG= 0;

  int contadorNM = 0;

  int contadorBM =0;

  int contadorRM = 0;

  int contadorNC = 0;

  int contadorBC = 0;

  int contadorRC = 0;

  int contadorNG = 0;

  int contadorBG = 0;

  int contadorRG =0;

  for(i = 0; i < 15; i++){

    printf("Digite o número correspondente a cada categoria(1 - Matemática, 2 - Ciências, 3 - Geografia \n");

    scanf("%i", &categoria);

    

    printf("Digite o número correspondente a cada conserção(1 - Novo, 2 - Bom, 3 - Ruim\n");

    scanf("%i", &conservacao);

    

    if(categoria == 1){

      contadorM++;

    }

    

    if(categoria == 1 && conservacao == 1){

      contadorNM++;

    }

    

    

    if(categoria == 1 && conservacao == 2){

      contadorBM++;

    }

    

    

    if(categoria == 1 && conservacao == 1){

      contadorRM++;

    }

    

    if(categoria == 2){

      contadorC++;

    }

    

    if(categoria == 2 && conservacao == 1){

      contadorNC++;

    }

    

    if(categoria == 2 && conservacao == 2){

      contadorBC++;

    }

    

    if(categoria == 2 && conservacao == 3){

      contadorRC++;

    }

    

     

    if(categoria == 3){

      contadorG++;

    }

    

    if(categoria == 3 && conservacao == 1){

      contadorNG++;

    }

    

     

    if(categoria == 3 && conservacao == 1){

      contadorBG++;

    }

     

    if(categoria == 3 && conservacao == 1){

      contadorRG++;

    }

  
  }

  printf("Quantidade de livros por categoria: Matemática %i,Ciências %i, Geografia %i ",contadorM, contadorC,contadorG );

  printf("Quantos livros eram novos na categoria matemática:%i ", contadorNM);

  return 0;

}

