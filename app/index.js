import fs from "fs";
import path from "path";
import babylon from "babylon";
import babel from "@babel/core";

// const __dirname = path.resolve();

function traverse(ast, param) {
  ast.program.body.forEach((node) => {
    if (param.hasOwnProperty(node.type)) {
      let func = param[node.type];
      func({ node });
    }
  });
}
let ID = 0;

function createAsset(filename) {
  const fileContent = fs.readFileSync(filename, "utf8");
  const AST = babylon.parse(fileContent, {
    sourceType: "module",
  });

  const dependencies = [];

  traverse(AST, {
    ImportDeclaration: ({ node }) => {
      dependencies.push(node.source.value);
    },
  });

  const id = ID++;
  const code = babel.transformFromAst(AST, null, {
    presets: ["@babel/preset-env"],
  });
  return {
    id,
    filename,
    dependencies,
    code: code.code,
  };
}

function createGraph(filename) {
  const entryPoint = createAsset(filename);

  let queue = [entryPoint];

  for (let asset of queue) {
    const dirname = path.dirname(asset.filename);
    asset.mapping = {};
    asset.dependencies.forEach((relativePath) => {
      const absolutePath = path.join(dirname, relativePath);
      const child = createAsset(absolutePath);
      asset.mapping[relativePath] = child.id;
      queue.push(child);
    });
  }
  return queue;
}

function bundle(graph) {
  let modules = "";

  graph.forEach((mod) => {
    modules += `${mod.id}:[
      function(require,module,exports){
        ${mod.code}
      },
      ${JSON.stringify(mod.mapping)}
    ],`;
  });

  const result = `(function(modules){
    function require(id){

      const [fn,mapping] = modules[id];

      function localRequireFunc(relativePath){
        return require(mapping[relativePath])
      }

      const module = {exports:{}};
    
      fn(localRequireFunc,module, module.exports);

      return module.exports
    }
    require(0);

  })({${modules}})`;

  return result;
}

const allAssets = createGraph("./exam/entry.js");

const result = bundle(allAssets);

console.log("result: ", result);
