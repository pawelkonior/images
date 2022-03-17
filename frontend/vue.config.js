const { defineConfig } = require("@vue/cli-service");
module.exports = defineConfig({
  devServer: {
    proxy: {
      '^api': {
        target:  'http://backend:8000'
      }
    }
  },

  transpileDependencies: true,

  css: {
    sourceMap: true,
  },

  configureWebpack: {
    devtool: "source-map",
  },

  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    },
  },
});
