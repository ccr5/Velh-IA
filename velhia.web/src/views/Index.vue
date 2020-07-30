<template>
  <section class="hero is-light is-bold is-fullheight">
    <div class="hero-body">
      <div class="container">
        <div class="buttons is-centered">
          <b-button type="is-dark" outlined rounded tag="router-link" :to="'/pvsp'">
            Player vs Player
          </b-button>
          <b-button type="is-dark" outlined rounded>Player vs S.A</b-button>
          <b-button type="is-dark" outlined rounded>Player vs A.I</b-button>
          <b-button type="is-dark" outlined rounded>S.A vs A.I</b-button>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
</script>
<style>
</style>