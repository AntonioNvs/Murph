# Dashboard

Dashboard de notícias, clima, ações e informações de desempenho do computaodr, feito em HMTL, CSS e JavaScript e com a integração com Python pela biblioteca EEL. Além disso, o programa é desbloqueado por reconhecimento facial, utilizando a biblioteca OpenCV. 

![](https://i.ibb.co/t8Y3y13/gif-murph.gif)

## Interface

Para a interface realizada, foi utilizado a biblioteca [EEL](https://pypi.org/project/Eel/), a qual realiza a integração entre o Python com as tecnologias Web, com a finalidade de construir uma aplicação Desktop. Diante disso, é visto a facilidade do desenvolvimento de aplicações que exigem designs mais complexos e com animações e integrações com outros meios (como o Chart.js, utilizado para os gráficos).

Portanto, a aplicação foi construída com HTML, CSS e manipulação por JavaScript, de tal forma, foi possível realizar todas as animações de forma dinâmica e funcional.

Para os gráficos, foi utilizado o [Chart.js](https://www.chartjs.org/), o qual as animações e a construção dos gráficos é de sua responsabilidade, tornando simples sua utilização.

## Reconhecimento Facial

O reconhecimento facial foi feito com a biblioteca OpenCV a partir da classificação do tipo LBPH, que sua função é rotular os pixels de uma imagem ao limitar a vizinhança de cada pixel e considera o resultado como um número binário. Por meio disso, foi criado dois arquivos, o de [captura de fotos](/capture.py) e o de [treinamento](/training.py) do modelo.

A partir disso, o algoritmo identifica as diferentes pessoas da captura por um id, localizado no nome da imagem, e no treinamento classifica os indivíduos com base nesse identificador. E com base nele, é relacionado com o nome da pessoa que já está pré determinado.

## Funcionalidades

As funcionalidades para o Dashboard foram quatro: informações do desempenho do hardware, notícias, clima e ações.

#### Hardware

Para capturar as informações de desempenho do computador, foi utilizado a biblioteca [psutil](https://pypi.org/project/psutil/), que somente com a chamada de funções, já retorna
o valor desejado. Portanto, para captura do desempenho do CPU **.cpu_percent()**, a de RAM **.virtual_memory()** e o de disco **disk_usage('/')**.

#### Notícias

Para tal funcionalidade, foi utilizado a API [News API](https://newsapi.org/), a qual a partir de um *request*, o retorno em JSON é transformado em *dict*, sendo manipulado dentro do código.

#### Clima

O clima é definido pela API [Open Weather](openweathermap.org), que traz informações completas sobre o clima da determinada região enviada por parâmetro na URL.

#### Ações

Utilizando a biblioteca **yahooquery**, é definido tipos de ações as quais vão ser buscadas, e o retorno é uma lista de parâmetros de análise, sendo utilizados somente a previsão de fechada da bolsa e por quanto ela foi aberta, assim, conseguindo prever o aumento ou descréscimo do preço da ação da empresa.
