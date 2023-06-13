import { createServer, connect, createConnection } from "net";
import { Buffer } from "buffer";
import fs from "fs";
import path from "path";
import crypto from "crypto";

// const client = createConnection({ port: 8124 }, () => {
//   // 'connect' listener.
//   console.log('connected to server!');
//   client.write('world!\r\n');
// });
// client.on('data', (data) => {
//   console.log(data.toString());
//   client.end();
// });
// client.on('end', () => {
//   console.log('disconnected from server');
// });

// const count = 1;

const server = createServer(async (c) => {
  console.log("server started");

  console.log("server is up and running");

  c.on("connect", () => {
    console.log("socket has been connected");
  });
  c.on("end", () => {
    console.log("client disconnected");
  });
  c.on("close", () => {
    console.log("socket has been released");
  });

  console.log(c.localAddress);

  //   const sleep = new Promise((resolve) => {
  //     setTimeout(() => {
  //       resolve(0);
  //     }, 4000);
  //   });
  //   await sleep;

  // const isPrimse = (n: number) => {
  //   let isPrime = true;
  //   for (let i = 3; i < n; i++) {
  //     //it is not a prime break the loop,
  //     // see how long it took
  //     if (n % i === 0) {
  //       isPrime = false;
  //       break;
  //     }
  //   }
  //   console.log("isPrime: ", isPrime);
  // };

  //   isPrimse(29355126551);

  /**
   * writing using buffer
   */
  // const b = Buffer.alloc(64);
  const b = Buffer.from(
    "HTTP/1.1 200 OK\r\n\r\nHi there, this is amazing i can directly write on buffer!\r\n"
  );
  b.write(
    "HTTP/1.1 200 OK\r\n\r\nHi, there this is amazing i can directly write on buffer!\r\n"
  );
  c.write(b);

  crypto.pbkdf2(
    "somesdafsadf",
    "salt",
    10000000,
    64,
    "sha512",
    (err, derivedKey) => {
      if (err) {
        console.error("An error occurred:", err);
      } else {
        console.log(`Processed chunk ${derivedKey}`);
        c.write(derivedKey);
        c.destroy();
      }
    }
  );

  // const filePath = path.resolve("src/testFile.txt");
  // console.log("filePath: ", filePath);
  // const readStream = fs.createReadStream(filePath, "hex");
  // readStream.on("data", (chunk) => {
  //   // Process the chunk of data
  //   console.log("Received chunk of data:", chunk);
  //   // c._write(chunk);
  //   c.write(chunk);
  // });
  // // Handle end event
  // readStream.on("end", () => {
  //   console.log("Finished reading the file.");
  //   c.destroy();
  // });
  // // Handle error event
  // readStream.on("error", (error) => {
  //   console.error("An error occurred:", error);
  // });

  // c.write("HTTP/1.1 200 OK\r\n\r\nHi, there!\r\n");

  //   c.write("hello\r\n");
  //   c.writable()
  //   c.pipe(c);
});

server.on("error", (err) => {
  throw err;
});

const startServer = () => {
  server.listen(8000, () => {
    console.log("server bound, listening on port: ", 8000);
  });
};

const readFile = () => {
  const filePath = path.resolve("src/testFile.txt");
  console.log("filePath: ", filePath);

  // fs.readFile(filePath, "hex", (err, data) => {
  //   if (err) throw err;

  //   console.log("data: ", data);
  // });

  const readStream = fs.createReadStream(filePath, "base64");
  readStream.on("data", (chunk) => {
    // Process the chunk of data
    console.log("Received chunk of data:", chunk);
  });
  // Handle end event
  readStream.on("end", () => {
    console.log("Finished reading the file.");
  });
  // Handle error event
  readStream.on("error", (error) => {
    console.error("An error occurred:", error);
  });
};

console.log("working");
// readFile();
startServer();
