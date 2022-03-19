import {storage} from './firebase';
import './App.css';
import { getDownloadURL, ref, uploadBytesResumable } from '@firebase/storage';
import { useState } from 'react';

function App() {
  
  const [uploadProgress, setUploadProgress] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    let file = e.target[0].files[0];
    if(!file){
      alert("file not uploaded");
      return;
    }
    fileUpload(file);
    e.target.reset();
  }

  const fileUpload = (file) => {
    if(!file){
      return;
    }
    const storageRef = ref(storage,`/file/${file.name}`);
    
    const uploadTask = uploadBytesResumable(storageRef,file);
    uploadTask.on('state_changed',(snapshot) => {
      const progress = Math.round(snapshot.bytesTransferred/snapshot.totalBytes) * 100;
      setUploadProgress(progress);
    },
    (err) => {
      console.log(err);
    },async ()=>{
      let uploadUrl = await getDownloadURL(uploadTask.snapshot.ref);
      console.log(uploadUrl);
      setUploadProgress(0);
    })
    
  }

  
  return (
    <div className="App">
      

      <form onSubmit={handleSubmit}>

        <input type="file" name="fileInput" style={{border: '1px solid grey',margin:'1rem 0.5rem'}} />

        <input type="submit" value="submit"/>

        <h3>Upload Progress :{uploadProgress}%</h3>


      </form>


    </div>
  );
}

export default App;
