import React, { useState } from 'react';

async function handleWeight(category, weight, metric){
  const info = {
      "category" : category,
      "metric" : metric,
      "weight" : weight
  }
  try { const response = await fetch("https://localhost:8000", {
      method : "POST",
      headers : {"Content-Type" : "application/json"},
      body : JSON.stringify(info)
      })
      if (!response.ok) {
          throw new Error("information not registered")
      }
      const data = await response.json()
      console.log(data)
      if (!data.message) {
          throw new Error("Something went wrong")
      }
  
  } catch (error) {
      console.error("Something went wrong: ", error)
  }
}

// Dropdown component
function Dropdown({ category, metric }) {
  const [weight, setWeight] = useState(.1)

  return (
  <div>
    <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
      <p>Please select the desired weight for {metric}</p>
      <select
        value={weight}
        onChange={function (event) {
          setWeight(parseFloat(event.target.value));
        }}
      >
        {[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1].map(function (val) {
          return (
            <option key={val} value={val}>
              {val}
            </option>
          );
        })}
      </select>
      <button onClick={function () {
          handleWeight(category, weight, metric)
      }}>Submit</button>
    </div>
    <p>Total must be equal to 1</p>
  </div>
);
}

function CreateDropdown({ weights }) {
  return (
    <div>
      {weights.map(function(weight) {
          return (
              <Dropdown
              key={weight.name}
              category={weight.category}
              metric={weight.name}
            />
          )
      })}
  </div>
)
}

export default CreateDropdown