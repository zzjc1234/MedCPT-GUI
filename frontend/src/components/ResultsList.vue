<template>
  <div>
    <h2>搜索结果</h2>
    <ul>
      <li v-for="(query, index) in results" :key="index">
        <h3>{{ query.query }}</h3>
        <ul>
          <li v-for="result in query.results" :key="result.pmid">
            <input
              type="checkbox"
              :value="result.pmid"
              v-model="selectedPmids"
            />
            PMID: {{ result.pmid }} - Score: {{ result.score.toFixed(2) }}
          </li>
        </ul>
      </li>
    </ul>
    <button @click="select">选择</button>
  </div>
</template>

<script>
export default {
  props: ["results"],
  data() {
    return { selectedPmids: [] };
  },
  methods: {
    select() {
      this.$emit("select", this.selectedPmids);
    },
  },
};
</script>
