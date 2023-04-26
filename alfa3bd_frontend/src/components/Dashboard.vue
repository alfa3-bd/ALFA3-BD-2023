<script lang="ts">
import axios from 'axios'
export default {

  data: function () {
    return {
      data: {
        series!: any,
      },
      series: [1,2],
      chartOptions: {
        labels: ['Com Infraestrutura', 'Sem Infraestrutura']
      },
    }
  },

  mounted(): void {
      axios.get('http://localhost:8000/relatorios/').then((response: any) => {
        this.data.series = [response.escolas_com_infra, response.escolas_sem_infra]
        console.log(response.data)
      })
  },
}
</script>

<template>
  <div>
    <h1>Unidades com Infraestrutura ALFA3BD</h1>
    <apexchart width="600" type="pie" 
      :options="chartOptions" 
      :series=[data.escolas_com_infra, data.escolas_sem_infra]>
    </apexchart>
  </div>
</template>

<style scoped>
</style>
