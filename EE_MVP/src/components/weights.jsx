import React, { useRef, useState, useEffect } from 'react';

async function handleWeight(weights){
  try { const response = await fetch("http://localhost:8000/weights", {
      method : "POST",
      headers : {"Content-Type" : "application/json"},
      body : JSON.stringify(weights)
      })
      if (!response.ok) {
          throw new Error("information not registered")
      }
      else {
        console.log("Weights are registered")
      }
  } catch (error) {
      console.error("Something went wrong: ", error)
  }
}

// Dropdown component
function Dropdown({ infoRef, category, metric, init }) {
  const [weight, setWeight] = useState(init)  
  useEffect(function () {
    if (!infoRef.current[category]) {
      infoRef.current[category] = {};
    }
    infoRef.current[category][metric] = weight;
  }, [weight]);
  return (
  <div>
    <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
      <p>Please select the desired weight for {metric}</p>
      <select value={weight} onChange={function (event) {
        setWeight(parseFloat(event.target.value))
      }}>
        {[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1].map(function (val) {
          return (
            <option key={val} value={val}>
              {val}
            </option>
          );
        })}
      </select>
    </div>
  </div>
);
}

function CreateDropdown({ weights }) {
  const groupedWeights = {
    grand: [],
    impact: [],
    finance: [],
    dev: [],
    tech: [],
    timeline: [],
  };

  const infoRef = useRef({})

  // Group metrics by category
  weights.forEach((weight) => {
    if (groupedWeights[weight.category]) {
      groupedWeights[weight.category].push(weight);
    }
  });

  const setWeights = {
      "impact" : .2, "finance" : .2, "dev" : .2, "tech" : .2, "timeline" : .2,
      "carbon": .4, "connections": .1, "women_consideration": .1, "track_women": .1, 
      "w_comm_prog": .1, "pue": .1, "econ_focus": .1,
      "capex": .2, "opex": .2, "cpc": .1, "lev_ratio": .1, "tariff_type": .1, "tariff": .1, "lcoe": .1,
      "requested_funds": .1,
      "per_local_tech": 1,
      "scalable": .3, "solution": .5, "monitering" : .1, "backup" : .1,
      "duration": 1
  }

  function getName(category) {
    let name = ""
    if (category == "dev") {
      name = "LOCAL INCLUSION"
    }
    else if (category == "grand") {
      name = "GENERAL"
    }
    else {
      name = category.toUpperCase()
    }
    return name
  }

  return (
  <div>
  {Object.entries(groupedWeights).map(function ([category, weights]) {
    return (
      <div key={category}>
        <h3>{getName(category)}</h3>
        <p>Total Weight Must Equal 1</p>
        {weights.map(function (weight) {
          return (
            <Dropdown
              key={weight.name}
              infoRef={infoRef}
              category={weight.category}
              metric={weight.name}
              init={setWeights[weight.name]}
            />
          );
        })}
      </div>
    );
  })
  }
  <button onClick={function() { handleWeight(infoRef.current) }}> Submit Weight Choices </button>
  </div>
)
}

export default CreateDropdown