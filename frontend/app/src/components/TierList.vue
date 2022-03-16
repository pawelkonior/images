<template>
  <div>
    <v-card
      class="mx-auto"
      max-width="25%"
      v-for="tier in tiers"
      v-bind:key="tier.id"
    >
      <v-card-header-text>
        <v-card-title>{{ tier.name }}</v-card-title>
        <v-btn
          :icon="show ? 'mdi-chevron-up' : 'mdi-chevron-down'"
          @click="show = !show"
        ></v-btn>
      </v-card-header-text>
      <!-- <v-card-actions>
        <v-btn rounded variant="outlined" text> Rozwiń</v-btn>
      </v-card-actions> -->
    </v-card>
  </div>
</template>

<script>
export default {
  name: "TierList",
  data() {
    return {
      tiers: [],
    };
  },
  methods: {
    async fetchTiers() {
      const response = await fetch("http://localhost:3000/tiersList");
      this.tiers = await response.json();
    },
  },
  mounted() {
    this.fetchTiers();
  },
};
</script>
<style lang="scss" scoped></style>
