import React, { useState, useEffect, useRef } from 'react';

async function handleCrit(infoRef) {
    try { const response = await fetch("http://localhost:8000/criteria", {
        method : "POST",
        headers : {"Content-Type" : "application/json"},
        body : JSON.stringify(infoRef)
        })
        if (!response.ok) {
            throw new Error("api call failed")
        }        
    } catch (error) {
        console.error("Something went wrong: ", error)

    }
}

function CritRange({infoRef, category, metric, def}) {
    const [min, setMin] = useState(def[0])
    const [max, setMax] = useState(def[1])
    useEffect(function() {
        if (!infoRef.current[category]) {
            infoRef.current[category] = {}
        }
        infoRef.current[category][metric] = [min, max]
    }, [min, max])

    return(
    <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <p>Please select the criteria for {metric}</p>
        <div style = {{ display: "flex", alignItems: "center", gap: "8px"}}>
            <input type="number" value={min} onChange={function(event) {
                setMin(Number(event.target.value))
            }}/>
            <input type="number" value={max} onChange={function(event) {
                setMax(Number(event.target.value))
            }}/>
        </div>
    </div>
    )
}

function CritBool({infoRef, category, metric, def}) {
    const [isChecked, setChecked] = useState(def)
    useEffect(function() {
        if (!infoRef.current[category]) {
            infoRef.current[category] = {}
        }
        infoRef.current[category][metric] = isChecked
    }, [isChecked])

    return (
    <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <p>Please select the criteria for {metric}</p>
        <input type="checkbox" checked={isChecked} onChange={function (event) {
            setChecked(event.target.value)
        }}/>
    </div>
    )
}

function CritStr({infoRef, category, metric, def}) {
    const [str, setStr] = useState(def)
    useEffect(function() {
        if (!infoRef.current[category]) {
            infoRef.current[category] = {}
        }
        infoRef.current[category][metric] = str
    }, [str])

    return (
        <div style = {{ display : "flex", alignItems: "center", gap: "10px" }}>
            <p>Please select the criteria for {metric}</p>
            <input type="text" value={str} onChange={function (e) {
                setStr(e.target.value)
            }}/>
        </div> 
    )
}

function CritInt({infoRef, category, metric, def}) {
    const [thresh, setThresh] = useState(def)
    useEffect(function() {
        if (!infoRef.current[category]) {
            infoRef.current[category] = {}
        }
        infoRef.current[category][metric] = thresh
    }, [thresh])

    return (
        <div style = {{ display : "flex", alignItems: "center", gap: "10px" }}>
            <p>Please select the criteria for {metric}</p>
            <input type="number" value={thresh} onChange={function (event) {
                setThresh(Number(event.target.value))
            }}/>
        </div>
    )
}

// this will also be passed down from the parent node

function CreateCritOptions({metrics}) {
    
    const infoRef = useRef({})

    // set defaul values for all critera
    const setVals = {
        carbon: [230, 300], connections: 150, women_consideration: true, 
        track_women: 3, w_comm_prog: 2, pue: 5, econ_focus: 4,

        capex: [50000, 300000], opex: [15000, 30000], cpc: [0.5, 4.0], 
        lev_ratio: 2, tariff_type: 'mixed tier', tariff: [0, 3.5], lcoe: [0.2, 0.4], 
        requested_funds: [0, 190000],

        per_local_tech: 75.0,

        scalable: true, solution: 'mini grid', monitering: true, backup: true,

        duration: [100, 366],
    }
    
    // create a new object with everything grouped
    const groupedMetrics = {
        impact: [],
        finance: [],
        dev: [],
        tech: [],
        timeline: [],
      };
    
      // using the non-grouped metrics, put into the categories object
      metrics.forEach((metric) => {
        if (groupedMetrics[metric.category]) {
          groupedMetrics[metric.category].push(metric);
        }
      });
   
    // helper function -- directs which metrics will use which eval system
    function chooseType(metric) {
        if (metric.type == "bool") {
            return <CritBool infoRef={infoRef} category={metric.category} metric={metric.name} def={setVals[metric.name]}/>
        }
        else if (metric.type == "range") {
            return <CritRange infoRef={infoRef} category={metric.category} metric={metric.name} def={setVals[metric.name]}/>
        }
        else if (metric.type == "int") {
            return <CritInt infoRef={infoRef} category={metric.category} metric={metric.name} def={setVals[metric.name]}/>
        }
        else if (metric.type == "string") {
            return <CritStr infoRef={infoRef} category={metric.category} metric={metric.name} def={setVals[metric.name]}/>
        }
        else return null
    }
    return (
        <div>
          {Object.entries(groupedMetrics).map(([category, metricList]) => (
            <div>
            <div key={category}>
              <h3>
                {category.toUpperCase() === "DEV"
                  ? "LOCAL INCLUSION"
                  : category.toUpperCase()}
              </h3>
              {metricList.map(function(metric) {
                return(<div key={metric.name}>{chooseType(metric)}</div>)}
          )}
            </div>   
        </div>
          ))}
          <button onClick={function() {
            handleCrit(infoRef.current)
          }}> Submit Criteria Choices </button>
        </div>
      );
    }

export default CreateCritOptions