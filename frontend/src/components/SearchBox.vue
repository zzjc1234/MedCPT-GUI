<template>
  <div>
    <textarea
      v-model="queriesText"
      placeholder="输入多个问题，每行一个"
    ></textarea>
    <button @click="search">查询</button>
    <button @click="clear">清空</button>
  </div>
</template>

<script>
export default {
  data() {
    return { queriesText: "" };
  },
  methods: {
    search() {
      this.$emit(
        "search",
        this.queriesText.split("\n").filter((q) => q.trim() !== ""),
      );
    },
    clear() {
      this.queriesText = "";
    },
  },
};
</script>
