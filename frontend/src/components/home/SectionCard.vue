<template>
  <router-link
    :to="{
      name: 'product-detail',
      params: {
        productSlug: item.slug,
      },
    }"
  >
    <div>
      <v-card class="card">
        <v-img
          class="align-center text-white"
          height="200"
          :src="imageLocation"
          contain
        >
        </v-img>

        <v-card-subtitle class="pt-4"> {{ item.price }} zł </v-card-subtitle>
      </v-card>
      <div class="card__info">
        <h3 class="text-center mt-5 card__info__header">{{ item.name }}</h3>
        <p class="card__info__categories">
          Kategoria:
          <span>{{ item.category[0].name }}</span>
        </p>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  name: "SectionCard",
  props: {
    item: Object,
  },
  computed: {
    imageLocation() {
      return import.meta.env.VITE_STATIC_ORGIN + this.item.main_image;
    },
  },
  created() {
    console.log(this.item);
  },
};
</script>

<style scoped lang="scss">
.card {
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: all 0.3s ease-in;
  &:hover {
    transform: scale(1.05) translateY(-25px) rotate(1deg);
  }
  &__info {
    display: flex;
    flex-direction: column;
    height: 7rem;
    p {
      color: var(--primary-white);
      margin-top: auto;
    }
  }
  .v-card-subtitle {
    color: var(--primary-white);
    font-weight: bold;
    font-size: 1.5rem;
    padding: 0.5rem;
    width: max-content;
    background-color: var(--primary-green);
    border-top-right-radius: 10px;
  }
}
</style>
