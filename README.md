<h1 align="center"> 
 UM ESTUDO SOBRE DIFERENTES APLICAÇÕES DAS TÉCNICAS DE DATA AUGMENTATION PARA UM CONJUNTO DE DADOS LIMITADO
</h1> 

Tabela de Conteúdos
=================
<!--ts-->
   * [Tabela de Conteúdos](#Tabela-de-conteúdos)
   * [Descrição do Projeto](#Descrição-do-Projeto)
   * [Status do Projeto](#Status-do-Projeto)
   * [Como usar](#como-usar)
   * [Métodos de Aumento Aplicados e Teste](#Métodos-de-Aumento-Aplicados-e-Teste)
      * [Métodos de Aumento](#Métodos-de-Aumento)
      * [Teste](#teste)
   * [Tecnologias](#tecnologias)
   * [Conclusão](#conclusão)
   * [Autor](#autor)
<!--te-->

# Descrição do Projeto

<p align="justify">
Esse projeto foi desenvolvido para explorar as técnicas de aumento de dados como uma alternativa para solucionar o problema da limitação dos dados, seja pela pouca quantidade de exemplos disponíveis, falta de profissionais capacitados para rotulagem ou necessidade de autorização para seu uso. O algoritmo recebe como entrada um conjunto de dados composto por imagens no formato PNG(Portable Network Graphics), executa os métodos de aumento para cada imagem que compõe o banco e retorna um conjunto de dados expandido.   
</p>

# Status do Projeto

- Finalizado :chart:

# Como usar

<p align="justify">

Considerando que já tenha instalado as dependências da seção [Tecnologias](#tecnologias). Esse projeto é composto por duas funções 'PadronizacaoFormato' e 'main'.

PadronizacaoFormato -  Função auxiliar responsável por converter o formato das imagens para PNG(Portable Network Graphics), caso não estejam nele.

main - Função principal que realiza o aumento de dados propriamente dito.

A função 'PadronizacaoFormato' pode ser executada da seguinte forma:
- Recebe como entrada imagens que estejam em qualquer formato dentro de uma pasta como nome 'ImagensOriginais';
- Caso não exista, criar uma pasta com o nome 'ImagensPadronizadas' para receber as imagens com formato modificado. 

A função 'main' possui alguns requisitos e detalhes que precisam ser salientados para sua correta execucação:
- Recebe imagens apenas no formato PNG;
- As imagens de entrada precisam estar numa pasta com nome 'ImagensPadronizadas';
- Caso não exista, criar uma pasta com nome 'aumento_dados' para receber as novas imagens geradas.
  
# Métodos de Aumento Aplicados e Teste

Esta seção está dividida em dois tópicos, o primeiro é responsável por apresentar as técnicas de aumento utilizadas e alguns esquemas para exemplifica-los. No segundo, temos o resultado da aplicação das técnicas de aumentos pelo algoritmo desta pesquisa para um conjunto de dados limitado.  

## Métodos de Aumento

As técnicas de aumento de dados usadas para essa pesquisa são baseadas em transformações geométricas, que permite modificações na forma, tamanho e posição de elementos dentro da imagem, e também transformações fotométricas, que alteram as propriedades das cores na imagem, através de mudanças nos valores dos pixels.

</p>

### Translação
Na translação a imagem é deslocada ao longo do eixo x ou eixo y, permitindo ir para esquerda (b), direita (c), acima (d) ou abaixo (e). 

<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/228076566-3209aec4-d19f-48cd-a32e-33f4be1d3d19.png"width="600px"
</p>

Existem diferentes abordagens para aplicação da translação, pode ocorrer apenas com os deslocamentos citados anteriormente que foi a metodologia aplicada neste trabalho, como também realizar uma combinação entre eles.

  
### Espelhamento
Método que realiza espelhamento, girando a imagem em um eixo vertical ou horizontal, movendo linhas e colunas inteiras de pixels. No espelhamento vertical a inversão será no eixo horizontal, sendo (a) à imagem original, temos o resultado dessa manipulação em (b).

<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/228076484-66b66fc9-1a53-4687-8524-0be66c1956a7.png"width="600px"
</p>

Em relação ao espelhamento horizontal a inversão dos valores de pixels ocorre no eixo vertical, gerando uma imagem como mostrado abaixo:

<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/228076447-9da5d55d-0d83-4b87-a631-049c94e57a0b.png"width="600px"
</p>

### Rotação

Técnica que modifica a imagem fazendo um rotacionamento no sentido horário (b) ou anti-horário (c) em um eixo de 1º e 359º. É importante ressaltar que dependendo do ângulo escolhido pode ocorrer perda de informação, por isso fixamos as modificações em ângulos de 90°.
  
<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/228077172-f7242fb5-adf3-48fc-b12d-c364153c0490.png"width="600px"
</p>

### Brilho Aleatório

Rotina responsável por alterar a imagem em diferentes níveis de iluminação, resultando em uma imagem mais clara (b) ou mais escura (c), quando comparado com a original (a).

<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/228077077-367f009f-4cad-41c9-84e8-24d24806bb13.png"width="500px"
</p>
  
Esse método recebe um valor delta para gerar imagens no intervalo fechado (-delta, delta), quanto mais próximo de 1.0 for esse valor, mais brilho receberá a imagem e quanto mais distante de 1.0, mais escura será a imagem.

### Zoom Aleatório

Essa técnica pode ser usada para ampliar ou diminuir a imagem aleatoriamente, nesta pesquisa apenas a ampliação (b) está sendo utilizada. 

<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/228079175-fe6aa2ad-8402-4aec-98a8-c4a7fe2f1127.png"width="600px"
</p>

Nesse método os números decimais negativos são responsáveis por realizar a ampliação da imagem, os valores definidos foram -0,2 e -0,4 que se referem a gerar imagens ampliadas no intervalo fechado que varia entre 20\% e 40\%.

## Teste
 
 Para execução desse teste foram reunidas 558 imagens micróscopicas de sangue através dos seguintes bancos dispinibilizados na internet:
 - [ImageBank](http://imagebank.hematology.org/collection/list)
 - [ALL-IDB](https://scotti.di.unimi.it/all/)
 
 É importante ressaltar que mesmo o conjunto de dados inicial sendo pequeno para tarefas de classificação e não possuindo características de generalidade e robustez, é inviável anexar todas as imagens do conjunto inicial ou do conjunto final nessa pesquisa, portanto os exemplos serão dados por meio de amostras.
 
Logo abaixo está uma figura como uma amostra dos dados de entrada para realização do aumento:
 
<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/228130942-197b651e-21cc-44e8-8a61-f3800ed49d9a.png"width="600px"
</p>
 
 Após a execução temos como resultado 6708 imagens no conjunto aumentado dentro da pasta 'aumento_dados', abaixo está uma amostra dessas imagens: 
 
<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/228130976-3300843e-ee56-4415-b14a-6a895aa121bd.png"width="500px"
</p>

Também é importante salientar que a forma como o algoritmo foi estruturado é possível conhecer o tamanho do conjunto final antes da execução, basta substituir a variável N, que representa o tamanho do banco de dados original na fórmula abaixo: 

<p align="center">
    <img src="[https://user-images.githubusercontent.com/56489559/228386437-a61e585f-9a77-4390-ae76-eefbd72d7ab5.png](https://user-images.githubusercontent.com/56489559/250131076-6e14e340-d014-4eb2-92a5-4dd514a6b427.png)"width="500px"
</p>

<p align="justify">
No qual, o número inteiro 8 está associado com a variável N pelo fato de alguns métodos de aumento serem aplicados mais de uma vez, por exemplo, o espelhamento é feito de maneira horizontal e vertical, algo semelhante ocorre com os métodos de rotação e translação. Enquanto, o segundo termo N se refere aos dados originais, sem qualquer aumento que são anexadas ao conjunto final. Por fim, para o teste realizado nessa pesquisa, temos aplicação do valor que corresponde a quantidade de dados no conjunto inicial na fórmula:
</p>
<p align="center">
    <img src="https://user-images.githubusercontent.com/56489559/250128821-deb4051b-efc3-4f93-bff7-9f30554c526f.png"width="500px"
</p>

<p align="justify">
A importância de determinar previamente a quantidade de dados no conjunto final é principalmente por questões de armazenamento, dependendo do tamanho no conjunto inicial talvez não seja viável guardar todos os dados gerados para posteriomente realizar o treinamento, logo isso envolverá decisões se o aumento deverá se feito de modo online ou offline, de acordo com a viabilidade.
</p>

# Tecnologias

As seguintes ferramentas foram utilizadas na construção desse projeto:

- [Python](https://www.python.org/)
- [TensorFlow](https://www.tensorflow.org/install?hl=pt-br)
- [Keras](https://keras.io/)
- [Skimage](https://scikit-image.org/docs/stable/install.html)
- [OS](https://www.python.org/)
- [OpenCV](https://pypi.org/project/opencv-python/)

# Conclusão
<p align="justify">
Neste estudo, foi proposto a exploração de métodos que realizam o aumento sintético de dados em um conjunto limitado composto por imagens microscópicas de sangue. Nosso experimento aumentou a quantidade de dados no conjunto de 558 imagens para 5022 imagens. Deixamos como trabalhos futuros a adição de mais métodos de \emph{Data Augmentation} como filtro gaussiano e contraste aleatório, para aumentar a variedade dos dados. Também a implementação de uma rede neural convolucional para identificação de células cancerígenas no conjunto de dados produzido nessa pesquisa, avaliar o impacto do aumento de dados em um ambiente com restrição de dados e comparar os resultados alcançados com trabalhos semelhantes encontrados na literatura. 
</p>

# Autor
- [Diêgo Marcelino Santos Silva](https://github.com/marcelinodiego)
