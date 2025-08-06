import React, { useState } from 'react';

function UploadForm() {
    const [file, setFile] = useState(null)
    async function send_file(file){
        // create form
        const form = new FormData();
        form.append("file", file)
        // send request
        try {
          const response = await fetch("http://localhost:8000/upload_file", {
          method : "POST",
          body : form
          });
          if (!response.ok){
            throw new Error("response not registered -- api failed")
          }
        } catch (error) {
          console.error("Something went wrong: ", error)
        }
      }
    
    return (
      <div>
        <input type="file" onChange={function(event) {
            setFile(event.target.files[0])
        }}/>
        <button onClick={ function () {
          send_file(file)} }
          >Confirm</button>
      </div>
    )
  }

export default UploadForm;