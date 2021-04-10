<template>
<div class="max-w-full mx-4 py-6 sm:mx-auto sm:px-6 lg:px-8">
    <div class="lg:text-center">
      <p class="mt-2 text-2xl leading-8 font-extrabold tracking-tight text-gray-900">
        Prediction of Machine Learning Models
      </p>
    </div>
    <div class="sm:flex sm:space-x-4">
      <div v-for="(m, index) in models" v-bind:key="m" 
      class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-md transform transition-all mb-4 w-full sm:w-1/3 sm:my-8">
          <div class="bg-white p-5">
              <div class="sm:flex sm:items-start">
                  <div class="text-center sm:mt-0 sm:ml-2 sm:text-left">
                      <h3 class="text-sm leading-6 font-medium text-gray-400">{{m}}</h3>
                      <p v-if="results[index] === 0" class="text-2xl font-bold text-green-500">Good</p>
                      <p v-else class="text-2xl font-bold text-purple-700">Phishing</p>
                  </div>
              </div>
          </div>
      </div>
    </div>
</div>
  <v-chart class="chart" :option="option" />
</template>

<script>
import { use } from "echarts/core";
import { BarChart } from "echarts/charts";
import { CanvasRenderer } from "echarts/renderers";
import {
  TooltipComponent,
  GridComponent,
  LegendComponent,
  TitleComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { ref, defineComponent } from "vue";

use([
  BarChart,
  CanvasRenderer,
  GridComponent,
  TooltipComponent,
  TitleComponent,
  LegendComponent,
]);

export default defineComponent({
  name: "HelloWorld",
  components: {
    VChart,
  },
  provide: {
    [THEME_KEY]: "light",
  },
  props: {
    url: String,
    data: Object
  },
  setup: (props) => {
    let models = []
    let benignProbability = []
    let phishingProbability = []
    let results = []
    props.data.forEach(m => {
        console.log(m)
        models.push(m['ML Model'])
        benignProbability.push(-(m['Probability'][0][0]*100).toFixed(4))
        phishingProbability.push((m['Probability'][0][1]*100).toFixed(4))
        results.push(m['Result'][0])
    });
    const option = {
      tooltip: {
        trigger: "axis",
        axisPointer: {
          type: "shadow", //'line' | 'shadow'
        },
      },
      title: {
        text: "Probability",
        left: "center"
      },
      legend: {
        data: ["Benign", "Phishing"],
        left: "right"
      },
      grid: {
        left: "3%",
        right: "4%",
        bottom: "3%",
        containLabel: true,
      },
      xAxis: [
        {
          type: "value",
          position: "top",
          min: function (value) {
            return Math.round(value.min/10)*10 - 10
          },
          max: function (value) {
            return Math.round(value.max/10)*10 + 10
          },
          axisLabel: {
            formatter: function (value, index) {
                return Math.abs(value) + ' %'
            }
          },
        },
      ],
      yAxis: [
        {
          type: "category",
          axisTick: {
            show: false,
          },
          inverse:true,
          data: models,
        },
      ],
      series: [
        {
          name: "Benign",
          type: "bar",
          stack: 'total',
          itemStyle: {
              color : "#6EE7B7"
          },
          label: {
            show: true,
            position: "left",
            formatter: function(d) {
                return -d.data + " %"
            }
          },
          emphasis: {
            focus: "series",
          },
          data: benignProbability,
        },
        {
          name: "Phishing",
          type: "bar",
          stack: 'total',
          itemStyle: {
              color : "#6366F1"
          },
          label: {
            show: true,
            position: "right",
            formatter: function(d) {
                return d.data + " %"
            }
          },
          emphasis: {
            focus: "series",
          },
          data: phishingProbability,
        },
      ],
    };
    return { option, models, results };
  },
});
</script>

<style scoped>
.chart {
  height: 400px;
}
</style>