<template>
  <div>
    <v-card class="card">
      <v-img
        class="align-center text-white"
        height="200"
        src="/section1.png"
        contain
      >
      </v-img>

      <v-card-subtitle class="pt-4"> 35.99 zł </v-card-subtitle>
    </v-card>
    <h3 class="text-center mt-5">Guarani Let It Snow 400g</h3>
  </div>
</template>

<script>
export default {
  name: "SectionCard",
};
</script>

<style scoped lang="scss">
.card {
  transition: all 0.3s ease-in;
  &:hover {
    transform: scale(1.05) translateY(-25px) rotate(1deg);
  }
  .v-card-subtitle {
    color: var(--primary-green);
    font-weight: bold;
    font-size: 1.5rem;
  }
}
</style>
