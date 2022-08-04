// import baseManifest from "./src/chrome/manifest.json";
// import WebpackExtensionManifestPlugin from "webpack-extension-manifest-plugin";
// import CleanWebpackPlugin from "lean-webpack-plugin";

const baseManifest = require("./src/chrome/manifest.json");
const WebpackExtensionManifestPlugin = require("webpack-extension-manifest-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = {
  entry: {
    main: "./src/index.js",
    background: "./src/chrome/background.js",
  },

  plugins: [
    new WebpackExtensionManifestPlugin({
      config: {
        base: baseManifest,
      },
    }),
    new CleanWebpackPlugin(),
  ],
  resolve: {
    extensions: [".js", ".jsx"],
  },

  module: {
    rules: [
      {
        test: /\.((js)|(jsx))$/,
        // /\.(js|jsx|ts\tsx)$/

        use: [
          {
            loader: "source-map-loader",
          },
          {
            loader: "babel-loader",
          },
        ],
        exclude: /(node_modules|bower_components)/,
      },
    ],
  },
};
