<template>
  <v-carousel
    v-model="current"
    show-arrows
    hide-delimiter-background
    hide-delimiters
    class="carousel"
  >
    <template v-slot:prev="{ props }">
      <svg
        @click="props.onClick"
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        fill="currentColor"
        class="bi bi-arrow-left"
        viewBox="0 0 16 16"
      >
        <path
          fill-rule="evenodd"
          d="M15 8a.5.5 0 0 0-.5-.5H2.707l3.147-3.146a.5.5 0 1 0-.708-.708l-4 4a.5.5 0 0 0 0 .708l4 4a.5.5 0 0 0 .708-.708L2.707 8.5H14.5A.5.5 0 0 0 15 8z"
        />
      </svg>
    </template>
    <template v-slot:next="{ props }">
      <svg
        @click="props.onClick"
        xmlns="http://www.w3.org/2000/svg"
        width="32"
        height="32"
        fill="currentColor"
        class="bi bi-arrow-right"
        viewBox="0 0 16 16"
      >
        <path
          fill-rule="evenodd"
          d="M1 8a.5.5 0 0 1 .5-.5h11.793l-3.147-3.146a.5.5 0 0 1 .708-.708l4 4a.5.5 0 0 1 0 .708l-4 4a.5.5 0 0 1-.708-.708L13.293 8.5H1.5A.5.5 0 0 1 1 8z"
        />
      </svg>
    </template>
    <v-carousel-item
      v-for="(slide, i) in slides"
      :key="i"
      :style="`background-image: url(${slide}); background-position: center`"
      class="slider__image"
    >
    </v-carousel-item>
  </v-carousel>
  <div class="gallery-container">
    <div
      v-for="(slide, i) in slides"
      :key="i"
      :style="`background-image: url(${slide})`"
      :class="{ 'not-current': i !== this.current }"
      @click.prevent="this.current = i"
    ></div>
  </div>
</template>

<script>
export default {
  name: "ProductGallery",
  data() {
    return {
      slides: [
        "https://www.yerbamarket.com/pol_pm_Yerba-Mate-Green-LEMON-8183_10.jpg",
        "https://www.yerbamarket.com/pol_pm_Yerba-Mate-Green-LEMON-8183_1.png",
        "https://www.yerbamarket.com/pol_pm_Yerba-Mate-Green-LEMON-8183_2.jpg",
        "https://www.yerbamarket.com/pol_pm_Yerba-Mate-Laranjeiras-Yari-terere-limao-siciliano-500-g-15104_1.png",
      ],
      current: 0,
    };
  },
};
</script>

<style scoped lang="scss">
.not-current {
  opacity: 0.3;
}
.gallery-container {
  display: grid;
  grid-template-rows: auto;
  grid-template-columns: repeat(4, 1fr);
  margin-top: 5px;

  div {
    height: 7rem;
    width: 7rem;
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    background-color: white;
    border: 1px solid black;
    cursor: pointer;
    transition: all 0.3s ease-in-out;
    &:hover {
      transform: scale(1.05);
    }
  }
}

svg {
  cursor: pointer;
  transition: all 0.3s ease-in-out;
  &:hover {
    transform: scale(1.05);
  }
}
</style>
