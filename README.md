# SEL0456
Repositório para os projetos da disciplina SEL0456 - Técnicas em Desenvolvimento de Software Livre

## Organização do Repositório
- **Teste**
  
  Diretório criado para testes realizados em aula.
  
- **Trabalho1**

  Diretório referente à entrega do Trabalho 1.

- **Trabalho2**

  Diretório referente à entrega do Trabalho 2.

## Funcionalidade dos Projetos

### Trabalho 1

  Este projeto consiste de um arquivo principal (_main.c_) localizado na pasta _/src_, o qual irá executar 3 funções distintas localizadas em arquivos .c distintos. Para isso, é utilizado um arquivo _Makefile_ para a compilação e controle do projeto. As funções implementadas foram:
  - ```make```: Responsável pela compilação do projeto e criação do programa main.
  - ```make run```: Responsável por executar o programa main.
  - ```make clean```: Responsável por excluir os arquivos binários criados durante a compilação.
  - ```make distclean```: Responsável por excluir o programa main.

### Trabalho 2
  Este projeto consiste em uma implementação de uma classe em pyhton para controle de usuários (_users.py_) e de um arquivo exemplificando sua utilização (_app.py_). Os atributos e métodos desta classe são:
  - Atributos:
    - ```User.username```: Nome do usuário;
    - ```User.role```: Cargo do usuário (superadmin, admin ou user). Não pode ser alterado;
    - ```User.password_hash```: Hash da senha do usuário. Não pode ser diretamente alterado.
  - Métodos:
    - ```User.verify_password(password)```: Verifica se a senha enviada equivale à senha do usuário;
    - ```User.change_password(old_password, new_password)```: Muda a senha do usuário caso senha atual do usuário informada esteja correta.
  
  Para visualizar o caso teste basta executar o arquivo _app.py_ com um interpretador python.
