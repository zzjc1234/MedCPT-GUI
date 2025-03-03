<template>
  <div>
    <h2>下载选中文献</h2>
    <input v-model="savePath" placeholder="输入保存路径" />
    <button @click="download">下载</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["selected"],
  data() {
    return { savePath: "./downloads" };
  },
  methods: {
    async download() {
      await axios.post("http://127.0.0.1:8000/download", {
        pmids: this.selected,
        save_path: this.savePath,
      });
      alert("下载完成");
    },
  },
};
</script>
