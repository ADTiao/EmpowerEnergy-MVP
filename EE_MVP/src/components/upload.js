import React, { useState } from 'react';

function UploadForm() {
    const [file, setFile] = useState(null)
    async function send_file(file){
        // create form
        const form = new FormData();
        form.append("file", file)
        // send request
        try {
          const response = await fetch("https://localhost:8000", {
          method : "POST",
          body : form
          });
          if (!response.ok){
            throw new Error("response not properly registered")
          }
          const data = response.json()
          if (!data.message) {
            throw new Error("Response not parsed properly")
          }
        } catch (error) {
          console.error("Something went wrong: ", error)
        }
      }
    
    return (
      <div>
        <h1> Upload Proposal Here </h1>
        <input type="file" onChange={function(event) {
            setFile(event.target.files[0])
        }}/>
        <button onClick={function() {send_file(file)}}>Confirm</button>
      </div>
    )
  }

export default UploadForm;