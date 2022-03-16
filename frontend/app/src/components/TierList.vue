<template>
    <div>
        <v-expansion-panels>
            <v-expansion-panel
                v-for="(item, i) in tiers"
                :key="i"
                :title="item.name"
                :text="JSON.stringify(item)"
                @click="fetchDetail('1')"
            >
            </v-expansion-panel>
        </v-expansion-panels>
    </div>
</template>

<script>
import {toRaw} from "vue";
import {retrieveData} from "@/utils/api";

export default {
    name: "TierList",
    data() {
        return {
            tiers: [],
        };
    },
    methods: {
        async fetchTiers() {
            this.tiers = await retrieveData("tiersList");
        },
        async fetchDetail(id) {
            const tier = await retrieveData(`tiers/${id}`);
            this.tiers = this.tiers.map((item) => {
                return toRaw(item).id === id ? tier : item;
            });
        },
    },
    mounted() {
        this.fetchTiers();
    },
};
</script>

<style lang="scss" scoped></style>
