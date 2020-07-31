<template>
  <section class="hero is-light is-bold is-fullheight">
    <div class="hero-body">
      <div class="columns info-historic">
        <div class="#">
          <div class="box">
            <h1 class="title">Historic Matchs</h1>
            <b-table :data="historic_datas" :columns="historic_datas_columns"></b-table>
          </div>
          <div class="box">
            <h1 class="title">Score</h1>
            <b-table :data="match_datas" :columns="match_data_columns"></b-table>
          </div>
        </div>
      </div>
      <div class="columns info-match">
        <div class="columns">
          <div class="Col">
            <div class="Campo C1L1">
              C1L1
            </div>
            <div class="Campo C1L2">
              C1L2
            </div>
            <div class="Campo C1L3">
              C1L3
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="Col">
            <div class="Campo C2L1">
              C2L1
            </div>
            <div class="Campo C2L2">
              C2L2
            </div>
            <div class="Campo C2L3">
              C2L3
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="Col">
            <div class="Campo C3L1">
              C3L1
            </div>
            <div class="Campo C3L2">
              C3L2
            </div>
            <div class="Campo C3L3">
              C3L3
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import $ from 'jquery'
import axios from 'axios'
export default {
  data() {
    return {
      historic_datas: [],
      historic_datas_columns: [
        {
          field: 'player',
          label: 'Player',
        },
        {
          field: 'total',
          label: 'Total',
          centered: true
        },
        {
          field: 'wins',
          label: 'Wins',
          centered: true
        },
        {
          field: 'draws',
          label: 'Draws',
          centered: true
        },
        {
          field: 'losses',
          label: 'Losses',
          centered: true
        }
      ],
      match_data: [],
      match_data_columns: [
        {
          field: 'player',
          label: 'Player',
        },
        {
          field: 'total',
          label: 'Total',
          centered: true
        },
        {
          field: 'wins',
          label: 'Wins',
          centered: true
        },
        {
          field: 'draws',
          label: 'Draws',
          centered: true
        },
        {
          field: 'losses',
          label: 'Losses',
          centered: true
        }
      ]
    }
  },
  methods: {
    getHistoricData () {
      axios.get('http://localhost:5000/api/cliente').then(ret => {
        this.historic_datas = ret.data
      })
    }
  },
  mounted () {
    $(document).ready(function(){
      var Altura = $(window).height();
      $(".info-historic").height(Altura);
      $(".info-match").height(Altura);
      $(".C1L1").on("click", function (){
        alert("C1L1")
      });
      $(".C1L2").on("click", function (){
        alert("C1L2")
      });
      $(".C1L3").on("click", function (){
        alert("C1L3")
      });
      $(".C2L1").on("click", function (){
        alert("C2L1")
      });
      $(".C2L2").on("click", function (){
        alert("C2L2")
      });
      $(".C2L3").on("click", function (){
        alert("C2L3")
      });
      $(".C3L1").on("click", function (){
        alert("C3L1")
      });
      $(".C3L2").on("click", function (){
        alert("C3L2")
      });
      $(".C3L3").on("click", function (){
        alert("C3L3")
      });
    });
    this.getHistoricData()
  }
};
</script>
<style>
.info-historic {
  margin-top: 20px;
}
.info-match {
  margin-top: 20px;
  margin-left: 10%;
}
.Col {
  min-width: 250px;
}
.Campo {
  min-height: 150px;
}
.C1L2 {
  border-top-style: solid;
  border-top-color: black;
  border-bottom-style: solid;
  border-bottom-color: black;
}
.C3L2 {
  border-top-style: solid;
  border-top-color: black;
  border-bottom-style: solid;
  border-bottom-color: black;
}
.C2L1 {
  border-left-style: solid;
  border-left-color: black;
  border-right-style: solid;
  border-right-color: black;
}
.C2L2 {
  border-style: solid;
  border-color: black;
}
.C2L3 {
  border-left-style: solid;
  border-left-color: black;
  border-right-style: solid;
  border-right-color: black;
}
</style>