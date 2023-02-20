<template>
  <div class="review-list">
    <div v-for="review in reviews" :key="review.id" class="review">
      <div class="review__info">
        <h3>{{ review.author.first_name }} {{ review.author.last_name }}</h3>
        <v-rating
          color="#04b60e"
          v-model="review.stars"
          readonly
          size="small"
        />
      </div>
      <div class="review__content">
        <p>{{ review.content }}</p>
        <small>{{ review.created_at }}</small>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ReviewsList",
  props: {
    reviews: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style scoped lang="scss">
.review {
  margin-top: 1rem;
  background-color: var(--primary-white);
  color: var(--color-background);
  border-radius: 5px;
  padding: 0.5rem;
  &__list {
    margin-bottom: 1rem;
  }
  &__info {
    display: flex;
    h3 {
      font-weight: bold;
      align-self: center;
    }
  }
  &__content {
    display: flex;
    align-items: center;
    p {
      text-align: start;
      margin: 0 0 5px 0;
    }
    small {
      margin-left: auto;
    }
  }
}
</style>
