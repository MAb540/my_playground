
import {initializeApp}  from 'firebase/app';
import {getStorage} from 'firebase/storage';

const firebaseConfig = {
    apiKey: "AIzaSyAWAT_oioFM7kjE6BV49yiZUEyWlWCu1O0",
    authDomain: "testproject-fffe3.firebaseapp.com",
    projectId: "testproject-fffe3",
    storageBucket: "testproject-fffe3.appspot.com",
    messagingSenderId: "261160250088",
    appId: "1:261160250088:web:82e99a76f507fcf5d4375d",
    measurementId: "G-F8GMZHQ6VV"
  };


export const app = initializeApp(firebaseConfig);
export const storage = getStorage(app);