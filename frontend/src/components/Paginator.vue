<template>
  <div class="text-center">
    <v-container>
      <v-row justify="center">
        <v-col cols="8">
          <v-container class="max-width">
            <v-pagination
              :model="pageNum"
              class="my-4"
              :length="length"
            ></v-pagination>
          </v-container>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
export default {
  name: "Paginator",
  props: {
    pageNum: Number,
    length: Number,
  },
};
</script>

<style scoped></style>
