// import path from "path";
// import common from "./webpack.common";
// import merge from "webpack-merge";

const path = require("path");
const common = require("./webpack.common");
const { merge } = require("webpack-merge");

module.exports = merge(common, {
  mode: "development",
  output: {
    // filename: "[name].bundle.js",
    filename: "static/js/[name].bundle.js",
    path: path.resolve(__dirname, "dist"),
  },
  devtool: "cheap-source-map",
});
