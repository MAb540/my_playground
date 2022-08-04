import path from "node:path/win32";
import { resolve } from "path";
import { defineConfig } from "vite";
import solidPlugin from "vite-plugin-solid";
import { viteStaticCopy } from "vite-plugin-static-copy";

export default defineConfig({
  plugins: [
    solidPlugin(),
    // viteStaticCopy({
    //   targets: [
    //     {
    //       src: "/src/chrome/manifest.json",
    //       dest: "dist",
    //     },
    //   ],
    // }),
  ],
  server: {
    port: 3000,
  },
  // resolve(__dirname, "/src/chrome/manifest.json")
  // assetsInclude: ["**/*.json"],
  build: {
    // manifest: true,
    rollupOptions: {
      input: {
        index: resolve(__dirname, "index.html"),
        options: resolve(__dirname, "/src/nested/options.html"),
        popup: resolve(__dirname, "./src/nested/popup.html"),
        background: resolve(__dirname, "/src/chrome/Background/background.ts"),

        // options: resolve(__dirname, "/src/chrome/Options/index.tsx"),
      },
      // [
      //   resolve(__dirname, "index.html"),
      //   resolve(__dirname, "/src/chrome/Background/background.ts"),
      // ]
      // input: ["index.html", "/src/chrome/background.ts"],
      output: {
        dir: "dist",
        entryFileNames: "assets/[name].[hash].bundle.js",
      },
    },
    target: "esnext",
  },
});
