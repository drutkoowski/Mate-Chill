<template>
  <ModalOverlay @closeModal="$emit('closeModal')">
    <div class="review-modal">
      <h3>Wybierz produkt dotyczący zamówienia</h3>
      <form @submit.prevent="reviewProduct">
        <v-select
          :items="order.products"
          item-title="product.name"
          return-object
          label="Produkt"
          bg-color="white"
          v-model="commentedProduct.value.value"
        />
        <v-textarea
          label="Treść Twojej opinii"
          bg-color="white"
          v-model="commentContent.value.value"
        />
        <p class="review-modal__error">{{ reviewErrorMessage }}</p>
        <div>
          <v-rating
            color="#04b60e"
            hover
            v-model="starsCount.value.value"
          ></v-rating>
        </div>
        <Button :text="'Dodaj opinię'" type="submit" />
      </form>
    </div>
  </ModalOverlay>
</template>

<script>
import { useField, useForm } from "vee-validate";
import ModalOverlay from "@/components/ModalOverlay.vue";
import Button from "@/components/Button.vue";
import { ref } from "vue";
import axios from "axios";
import useToastStore from "@/stores/toast";
export default {
  name: "OrderProductReview",
  components: {
    ModalOverlay,
    // eslint-disable-next-line vue/no-reserved-component-names
    Button,
  },
  props: {
    order: {
      type: Object,
      required: true,
    },
  },
  emits: ["isReviewPosted", "closeModal"],
  setup(props, { emit }) {
    const reviewErrorMessage = ref("");
    const { handleSubmit } = useForm({});
    const commentedProduct = useField("commentedProduct");
    const commentContent = useField("commentContent");
    const starsCount = useField("starsCount");
    const reviewProduct = handleSubmit(async function (values) {
      reviewErrorMessage.value = "";
      const toastStore = useToastStore();
      try {
        await axios.post("reviews/create", {
          stars: values.starsCount,
          content: values.commentContent,
          product: values.commentedProduct.product.id,
        });
        toastStore.displayToast("Pomyślnie zamieszczono opinię,", "success");
        emit("isReviewPosted");
      } catch (error) {
        toastStore.displayToast(
          "Wystąpił błąd przy zamieszczaniu opinii.",
          "#E85959FF"
        );
        reviewErrorMessage.value = "Wystąpił błąd przy zamieszczaniu opinii.";
      }
    });
    return {
      reviewProduct,
      commentContent,
      commentedProduct,
      starsCount,
      reviewErrorMessage,
    };
  },
};
</script>

<style scoped lang="scss">
.review-modal {
  width: 35rem;
  @include respond(tab-port) {
    width: 30rem;
  }
  @include respond(tab-sm) {
    width: 25rem;
  }
  @include respond(phone-lg) {
    width: 100%;
  }
  h3 {
    color: var(--primary-white);
    font-size: 1.5rem;
    @include respond(phone-md-sm) {
      font-size: 1.25rem;
    }
  }
}
</style>
