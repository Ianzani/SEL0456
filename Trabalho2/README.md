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
