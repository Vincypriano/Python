with open("c:/Users/Elisabeth/Desktop/VINI/Python/PRINCIPAL/Let's Code/Parte 1/instalações.txt",'w',encoding='utf-8') as arquivo:
    arquivo.write('''Instalando o Python no Mac OS X
Comando para instalação do HomeBrew:

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
Instalando o Python no Linux (debian/ubuntu):
apt install python3 python3-pip
Jupyter Notebook
Com o Python instalado, você já pode abrir o prompt de comando para digitar os seguintes comandos:

Para instalar o programa Jupyter Notebook, que utilizaremos para escrever nossos códigos Python:
pip install notebook
Para garantir que estamos utilizando a versão mais recente do Jupyter Notebook:
pip install notebook --upgrade
Para iniciar o programa Jupyter Notebook:
jupyter notebook
Ao exercutar este comando, uma janela deverá se abrir em seu navegador (Chrome, Firefox, Edge, etc) com o Jupyter Notebook (uma alternativa é copiar e colar a URL que aparece em seu prompt de comando).

Apenas para dar uma pequena prévia, vamos criar um novo arquivo selecionando "New" e então "Notebook: Python 3" (nesse momento, você pode optar por selecionar alguma pasta do seu computador, como Meus Documentos, para que o novo arquivo seja criado dentro dela).

Uma nova janela se abrirá. Essa janela é a interface de escrita para o arquivo que você acabou de criar.

Como você pode ver, existe uma célula vazia nesse arquivo. Nós vamos clicar nela e escrever:

print("Hello, World!") 
E, com essa célula selecionada, vamos clicar em "Run".

Alguns comentários finais:

Existe uma versão do Jupyter Notebook online. Basta entrar no site dele para testar.
Existe ainda outra ferramenta online para escrever notebooks chamada Google Colaboratory (ou Colab), um serviço gratuito do Google que você pode acessar por aqui sem instalar nada em seu PC (nem mesmo o Python). Para utilizá-lo, basta fazer o login com uma conta do Google. Seus arquivos serão salvos no Google Drive dessa conta do mesmo modo que um Google Docs ou Google Spreadsheet.
E é isso, acabou. Ou melhor, só está começando! A partir de agora você pode seguir para as próximas aulas para aprender cada vez mais.

Obs: Os cursos digitais dos processos seletivos não contêm os exercícios citados pelo instrutor.''')
with open ("c:/Users/Elisabeth/Desktop/VINI/Python/PRINCIPAL/Let's Code/Parte 1/instalações.txt",'r',encoding='utf-8')as arquivo:
    print(arquivo.read(),end='')