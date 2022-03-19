
// using node js to upload file to firebase bucket
import path from 'path';
import fs from 'fs';
import {initializeApp} from 'firebase/app';
import {getStorage,ref,uploadBytesResumable,getDownloadURL} from 'firebase/storage';


const firebaseConfig = {
    apiKey: "AIzaSyAWAT_oioFM7kjE6BV49yiZUEyWlWCu1O0",
    authDomain: "testproject-fffe3.firebaseapp.com",
    projectId: "testproject-fffe3",
    storageBucket: "testproject-fffe3.appspot.com",
    messagingSenderId: "261160250088",
    appId: "1:261160250088:web:82e99a76f507fcf5d4375d",
    measurementId: "G-F8GMZHQ6VV"
  };


const app = initializeApp(firebaseConfig);

const storage = getStorage(app);

// const storageRef = ref(storage,`/file/${file.name}`);
    
// const uploadTask = uploadBytesResumable(storageRef,file);


// const drawImageRef = ref(storage,'test.png');

const drawImagesRef = ref(storage,`/nodeImages/test.png)}`);

// path.join('Desktop','test.png')

const img_file = fs.readFileSync('testNode.png',(err,file) => {
    if(err) throw err;

    return file;
})

// console.log(img_file);

const uploadTask = uploadBytesResumable(drawImagesRef,img_file); // second argument read from buffer

uploadTask.on('state_changed',(snapshot)=>{
    const progress = Math.round(snapshot.bytesTransferred/snapshot.totalBytes) * 100;
    console.log(progress);
},(err)=>{
    console.log('from here ',err);
},async ()=>{
    let imageUploadUrl = await getDownloadURL(uploadTask.snapshot.ref);
    console.log(imageUploadUrl);
})



