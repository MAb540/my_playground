import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const extensionManifestKeys = {
  background: "background.bundle.js",
};

const distPath = path.join(__dirname, "dist");

const allFilesNamesInAssets = [];
fs.readdirSync(`${distPath}/assets`).forEach((file) =>
  allFilesNamesInAssets.push(file)
);

const namesMapper = {};

const basePath = `./assets/`;
Object.values(extensionManifestKeys).forEach((key) => {
  let keyFound = allFilesNamesInAssets.find((name) => {
    let matchName = `${name.slice(
      name.indexOf("background"),
      name.indexOf(".")
    )}.${name.slice(name.indexOf("bundle"))}`;
    return key === matchName;
  });
  console.log("keyFound: ", keyFound);
  if (keyFound) {
    namesMapper[`${basePath}${key}`] = `${basePath}${keyFound}`;
  }
});

const content = fs.readFileSync("dist/manifest.json", "utf-8");
const parsed = JSON.parse(content);

console.log(parsed);

for (const name of Object.keys(extensionManifestKeys)) {
  console.log("naem: ", name);

  if (typeof parsed[name] === "object" && parsed[name].service_worker) {
    parsed[name]["service_worker"] =
      namesMapper[parsed[name]["service_worker"]];
  }
}

console.log(parsed);

// Write to assets directory
fs.writeFileSync(`${distPath}/manifest.json`, JSON.stringify(parsed), "utf-8");
