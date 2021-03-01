// Determinando o tamanho máximo da janela
window.onresize = function (){
  if (window.outerWidth != 1080 || window.outerHeight != 768){
      window.resizeTo(1080, 768);
  }
}

// Cor dos gráficos de cada parâmetro
var colorCPU = "#ff6384"
var colorRAM = "#36a2eb"
var colorDisk = "#ffcd56"

// Variáveis dos gráficos 
var cpuChart = undefined
var ramChart = undefined
var diskChart = undefined

// Ao carregar a tela, crie os gráficos e chame as funções de dados
window.onload = function (){
  // Manipulando os gráficos
  var cpuElement = document.getElementById("cpu-chart")
  var ramElement = document.getElementById("ram-chart")
  var diskElement = document.getElementById("disk-chart")

  cpuChart = new Chart(cpuElement, {
    type: 'pie',
    data: {
      datasets: [{
          backgroundColor: ['rgba(0, 0, 0, 0.3)', colorCPU],
          data: [100, 0],
          borderWidth: 0,
          weight: 0.6,
      }],
      labels: ['Inativo', 'Ativo']
    },
    options: {
      cutoutPercentage: 50,
      legend: {
        display: false,
      }
    }
  })

  ramChart = new Chart(ramElement, {
    type: 'pie',
    data: {
      datasets: [{
          backgroundColor: ['rgba(0, 0, 0, 0.3)', colorRAM],
          data: [100, 0],
          borderWidth: 0,
          weight: 0.6,
      }],
      labels: ['Inativo', 'Ativo']
    },
    options: {
      cutoutPercentage: 50,
      legend: {
        display: false,
      }
    }
  })

  diskChart = new Chart(diskElement, {
    type: 'pie',
    data: {
      datasets: [{
          backgroundColor: ['rgba(0, 0, 0, 0.3)', colorDisk],
          data: [100, 0],
          borderWidth: 0,
          weight: 0.6,
      }],
      labels: ['Inativo', 'Ativo']
    },
    options: {
      cutoutPercentage: 50,
      legend: {
        display: false,
      }
    }
  })

  eel.get_name()((name) => {
    var titleText = document.getElementById('title-text')
    titleText.innerHTML = `Hi ${name}, how you doing?`
  })

  eel.get_data_graphs()
  eel.get_weather("get")
  eel.get_news("get")
  eel.get_value_actions("get")
}

// Informação de clima
eel.expose(loadWeather)
function loadWeather(temp, description) {
  var tmpText = document.getElementById("temp-weather")
  var descText = document.getElementById("description-weather")

  tmpText.innerHTML = temp + '° C'
  descText.textContent = description
}

// Informação de notícias
eel.expose(loadNews)
function loadNews(news) {

  var dashboard = document.getElementById('dashboard')

  var i = 2
  news.forEach((unic_new) => {
    var divNew = document.createElement('div')
    divNew.className = "news"

    divNew.onclick = () => {
      eel.access_new(unic_new['url'])
    }
    var img = document.createElement('img')
    img.className = "image-new"
    img.src = unic_new['url_image']

    var divContent = document.createElement('div')
    divContent.className = "content" + " " + (i % 2 == 0) ? 'left' : 'right'

    var titleNew = document.createElement('h1')
    titleNew.innerHTML = unic_new['title']
    titleNew.className = 'title-new'

    var descNew = document.createElement('h4')
    descNew.innerHTML = unic_new['description']
    descNew.className = "description-new"

    divContent.appendChild(titleNew)
    divContent.appendChild(descNew)

    if(i % 2 == 0) {
      divNew.appendChild(img)
      divNew.appendChild(divContent)
    } else {
      divNew.appendChild(divContent)
      divNew.appendChild(img)
    }

    dashboard.appendChild(divNew)
    i++
  })
}

// Informação das ações
eel.expose(loadActions)
function loadActions(actions) {
  var divActions = document.getElementById("actions")

  actions.forEach(action => {
    var div = document.createElement('div')
    div.className = "data-action"

    var titleAction = document.createElement('h2')
    titleAction.className = "name-action"
    titleAction.innerHTML = action['name']

    var percAction = document.createElement('h4')
    percAction.className = "value-action"

    var valueAction = action["perc"]
    percAction.innerHTML = (valueAction >= 0) ? '+' + valueAction + '%' : '-' + valueAction + '%'
    percAction.style.color = (valueAction >= 0) ? "#27AE60" : "#EB5757"

    div.appendChild(titleAction)
    div.appendChild(percAction)

    divActions.appendChild(div)
  })
}

// Manipulando os gráficos
eel.expose(loadDataGraphs)
function loadDataGraphs(cpu, ram, disk) {
  cpuChart.data.datasets[0].data = [100-cpu, cpu]
  cpuChart.update()

  ramChart.data.datasets[0].data = [100-ram, ram]
  ramChart.update()

  diskChart.data.datasets[0].data = [100-disk, disk]
  diskChart.update()

  var cpuText = document.getElementById("cpu-text")
  var ramText = document.getElementById("ram-text")
  var diskText = document.getElementById("disk-text")

  cpuText.innerHTML = cpu + '%'
  ramText.innerHTML = ram + '%'
  diskText.innerHTML = disk + '%'

  if(cpu > 90)
    cpuText.style.color = '#EB5757'
  else
    cpuText.style.color = '#27AE60'

  if(ram > 80)
    ramText.style.color = '#EB5757'
  else
    ramText.style.color = '#27AE60'

  if(disk > 70)
    diskText.style.color = '#EB5757'
  else
    diskText.style.color = '#27AE60'
}
