### Trabalho 4
  #### Geral
  Este projeto consiste na criação de uma API responsável por retornar o valor do fatorial de um número e o valor do enésimo elemento da sequência de Fibonacci. A estrutura de dados recebida pela API é um arquivo JSON, o qual pode ser composto pelos seguintes objetos:
  ```
  "fib": "val1",
  "fact": "val2"
  ```
  Recebida uma sintaxe válida, a API retornará o valor de interesse em seus respectivos objetos, sendo eles: o fatorial em ```"fact"``` e o elemento da Fibonacci em ```"fib"```.

  #### Execução
  Para a execução da API, deve-se executar o código abaixo em seu terminal:
   ```
  python3 run.py
  ```
  Vale ressaltar que as bibliotecas necessárias estão localizadas no arquivo _requirements.txt_, podendo serem instaladas pelo seguinte comando:
   ```
  pip install -r requirements.txt
  ```
  #### Tratamento de Erro
  A API desenvolvida possui um tratamento de erro que é baseado nos seguintes tópicos:
  - **JSON com mais de 2 objetos**: Será retornado o erro ```400``` junto à mensagem "Json too long";
  - **Valor diferente de _int_**: Será retornado o erro ```400``` junto à mensagem "Invalid type";
  - **Valor fora do _range_ de 0 à 1001**: Será retornado o erro ```400``` junto à mensagem "Invalid range (0 < value < 1001)".
    
  Vale notar que, caso seja enviado um arquivo JSON com menos de 2 objetos porém com objetos diferentes de ```"fib"``` e ```"fact"```, a API retornará o arquivo JSON sem realizar modificações nos objetos desconhecidos.

  #### Informações Adicionais
  As configurações de hospedagem e _debugging_ podem ser modificadas no arquivo _config.py_. As funções utilizadas podem ser encontradas no arquivo _functions.py_.
