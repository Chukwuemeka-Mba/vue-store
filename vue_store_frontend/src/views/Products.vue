<template lang="">
  <div>
    <div class="container" v-for="product in products">
      <div class="">
        <figure><img v-bind:src="product.get_image" /></figure>
        <h1 class="title">{{ product.name }}</h1>
        <p>{{ product.description }}</p>
      </div>
      <div>
        <h2>Information</h2>
        <p>
          <strong>${{ product.price }}</strong>
        </p>
        <div>
          <div>
            <input type="number" class="input" min="1" v-model="quantity" />
          </div>

          <div class="control">
            <a href=""><button type="submit"></button></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Products",
  data() {
    return {
      product: {},
      quantity: 1,
    };
  },
  mounted() {
    this.getProduct();
  },
  methods: {
    getProduct() {
      const category_img = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      axios.get("");
    },
  },
};
</script>
<style lang=""></style>
