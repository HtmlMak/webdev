import './scss/styles.scss';
import { Tooltip } from 'bootstrap';
import jQuery from 'jquery';
import { Tabulator, AjaxModule } from 'tabulator-tables';

import * as echarts from 'echarts';

window.$ = jQuery

if (document.getElementById('example-table')) {
  const table = new Tabulator("#example-table", {
    data: [],
    layout: "fitColumns",
    columns: [
      { title: "Name", field: "name", width: 150, sorter: "string" },
      { title: "Age", field: "age", hozAlign: "left", formatter: "progress" },
      { title: "Favourite Color", field: "col", sorter: "string" }
    ],
  });

  fetch('http://localhost:5000/table-row-data')
    .then(response => response.json())
    .then(result => {
      setTimeout(() => {
        table.replaceData(result)
      }, 1500)
      setTimeout(() => {
        table.addData(result)
      }, 2000)

    })
}


if (document.getElementById('chart')) {
  const chart = document.getElementById('chart');

  const widhtInput = chart.querySelector('[name="width"]')
  const labelsInput = chart.querySelector('[name="labels"]')
  const baseUrl = chart.querySelector('img').getAttribute('data-url')


  chart.querySelector('button').addEventListener('click', (e) => {
    e.preventDefault()
    const newUrl = new URL(baseUrl);

    if (widhtInput.value) {
      newUrl.searchParams.append('width', Number(widhtInput.value));
    }
    if (labelsInput.value) {
      labelsInput.value.split(',').forEach(label => {
        newUrl.searchParams.append('labels', label);
      })

    }

    chart.querySelector('img').setAttribute('src', newUrl.toString());
  })
}

if (document.getElementById('echarts')) {
  const echartDom = document.getElementById('echarts');

  const myChart = echarts.init(echartDom);

  myChart.showLoading()

  fetch('http://localhost:5000/chart/proxy')
    .then(response => response.json())
    .then(graph => {

      graph.nodes.forEach((node) => {
          node.label = {
            show: node.symbolSyze > 30
          }
      })

      myChart.setOption({
        title: {
          text: 'Les Miserables',
          subtext: 'Default layout',
          top: 'bottom',
          left: 'right'
        },
        tooltip: {},
        legend: [
          {
            // selectedMode: 'single',
            data: graph.categories.map(function (a) {
              return a.name;
            })
          }
        ],
        animationDuration: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
          {
            name: 'Les Miserables',
            type: 'graph',
            layout: 'none',
            data: graph.nodes,
            links: graph.links,
            categories: graph.categories,
            roam: true,
            label: {
              position: 'right',
              formatter: '{b}'
            },
            lineStyle: {
              color: 'source',
              curveness: 0.3
            },
            emphasis: {
              focus: 'adjacency',
              lineStyle: {
                width: 10
              }
            }
          }
        ]
      });
      myChart.hideLoading();
    })

}