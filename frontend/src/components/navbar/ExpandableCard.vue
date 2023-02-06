<template>
  <v-menu open-on-hover>
    <template v-slot:activator="{ props }">
      <li v-bind="props">{{ text }}</li>
    </template>
    <div class="card-container" :class="`col${cols}`">
      <div v-if="cols === 3" class="card-container__wrapper">
        <div class="card-container__flex-container">
          <h2>Kraje</h2>
          <p v-for="(country, index) in items['countries']" :key="index">
            {{ country }}
          </p>
        </div>
        <div class="card-container__flex-container">
          <h2>Rodzaje</h2>
          <p v-for="(country, index) in items['type']" :key="index">
            {{ country }}
          </p>
        </div>
        <div class="card-container__flex-container">
          <h2>Producenci</h2>
          <p v-for="(country, index) in items['brand']" :key="index">
            {{ country }}
          </p>
        </div>
      </div>

      <p v-for="(item, index) in items" :key="index" v-else>
        {{ item.title }}
      </p>
    </div>
  </v-menu>
</template>

<script>
export default {
  name: "ExpandableCard",
  props: {
    text: String,
    cols: Number,
    items: Array,
  },
};
</script>

<style scoped lang="scss">
li {
  transition: all 0.3s ease-in;
  cursor: pointer;
  &:hover {
    transform: scale(1.03);
    color: var(--primary-green);
  }
}
.card-container {
  display: grid;
  grid-template-rows: auto;
  background-color: var(--primary-white);
  padding: 1rem 2rem;
  border-radius: 5px;
  color: var(--color-background);
  &__wrapper {
    display: grid;
    column-gap: 5rem;
    grid-template-columns: repeat(3, 1fr);
  }
  &__flex-container {
    display: flex;
    flex-direction: column;
  }
}

.col1 {
  grid-template-columns: repeat(1, 1fr);
}
.col2 {
  grid-template-columns: repeat(2, 1fr);
}
.col3 {
  grid-template-columns: repeat(1, 1fr);
}
</style>
