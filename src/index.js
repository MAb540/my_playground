import { render } from "solid-js/web";
import { App } from "./App";

let abc = document.URL;
console.log("abc: URL ", abc);

const div = document.createElement("div");
div.id = "testExt";

// const shadowRoot = div.attachShadow({ mode: "open" });
document.body.insertBefore(div, document.body.firstChild);

render(() => <App />, document.getElementById("testExt"));

// options: {
//   presets: ["solid"],
//   plugins: [
//     "@babel/plugin-transform-runtime",
//     "@babel/plugin-proposal-object-rest-spread",
//   ],
//   cacheDirectory: true,
// },
