<script lang="ts">
import axios from 'axios'
export default {

  data() {
    return {
      series: null,
      chartOptions: {
        labels: ['Com Infraestrutura', 'Sem Infraestrutura']
      },
    }
  },

  mounted(): void {
      axios.get('http://localhost:8000/relatorios/')
      .then((response: any) => {
        this.series = response.data[0].unidades_apoiadas
        console.log(this.series)
      })
  },
}
</script>

<template>
  <div>
    <h1>Unidades com Infraestrutura ALFA3BD</h1>
    <apexchart width="600" type="pie" 
      :options="chartOptions" 
      :series="series">
    </apexchart>
  </div>
</template>

<style scoped>
</style>
