<template>
  <v-carousel
    height="500"
    show-arrows
    hide-delimiter-background
    cycle
    hide-delimiters
    style="margin-top: 5rem"
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
    <v-carousel-item v-for="(slide, i) in slides" :key="i">
      <img :src="slide" alt="Photo" class="slider__image" />
    </v-carousel-item>
  </v-carousel>
</template>

<script>
export default {
  name: "Carousel",
  data() {
    return {
      slides: [
        "/slider-image1.png",
        "/slider-image2.png",
        "/slider-image3.png",
        "/slider-image5.png",
      ],
    };
  },
};
</script>

<style scoped lang="scss">
svg {
  transition: transform 0.3s ease-in;
  cursor: pointer;
  &:hover {
    transform: scale(1.2);
  }
}
.slider__image {
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-position: center;
  -webkit-background-size: 100%;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}
</style>
