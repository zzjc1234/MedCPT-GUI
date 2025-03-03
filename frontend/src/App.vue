<template>
  <div class="container">
    <h1>PubMed 文献搜索</h1>
    <SearchBox @search="handleSearch" />
    <ResultsList :results="searchResults" @select="handleSelect" />
    <Download :selected="selectedResults" />
  </div>
</template>

<script>
import SearchBox from "./components/SearchBox.vue";
import ResultsList from "./components/ResultsList.vue";
import Download from "./components/DownloadComponent.vue";
import axios from "axios";

export default {
  components: { SearchBox, ResultsList, Download },
  data() {
    return {
      searchResults: [],
      selectedResults: [],
    };
  },
  methods: {
    async handleSearch(queries) {
      const res = await axios.post("http://127.0.0.1:8000/search", { queries });
      this.searchResults = res.data;
    },
    handleSelect(selected) {
      this.selectedResults = selected;
    },
  },
};
</script>

<style>
.container {
  max-width: 800px;
  margin: auto;
  text-align: center;
}
</style>
