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
  @include respond(phone-lg) {
    padding: 0 5px;
  }
  ::v-deep .v-rating__wrapper {
    @include respond(phone-lg) {
      width: 1rem;
    }
  }
  ::v-deep .v-rating {
    @include respond(phone-lg) {
      margin-left: 1rem;
    }
  }
  &__list {
    margin-bottom: 1rem;
  }
  &__info {
    display: flex;
    h3 {
      font-weight: bold;
      align-self: center;
      @include respond(phone-lg) {
        font-size: 0.8rem;
      }
    }
  }
  &__content {
    display: flex;
    align-items: center;
    @include respond(phone-lg) {
      font-size: 0.8rem;
    }
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
