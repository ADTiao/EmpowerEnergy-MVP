import React, { useState } from 'react';

async function handleCrit(category, metric, val) {
    console.log(category, metric, val)
    const info = {
        "category" : category,
        "metric" : metric,
        "val" : val
    }
    try { const response = await fetch("url", {
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
        else { console.log("all good with parsing data")}
    } catch (error) {
        console.error("Something went wrong: ", error)

    }
}

function CritRange({category, metric, handleCrit}) {
    const [min, setMin] = useState(0)
    const [max, setMax] = useState(0)
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
        <button onClick={function() {
            handleCrit(category, metric, [min, max])
        }}>Confirm</button>
    </div>
    )
}

function CritBool({category, metric, handleCrit}) {
    const [isChecked, setChecked] = useState(true)
    return (
    <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <p>Please select the criteria for {metric}</p>
        <input type="checkbox" checked={isChecked} onChange={function (event) {
            setChecked(event.target.checked)
        }}/>
        <button onClick={function () {
            handleCrit(category, metric, isChecked)
        }}>Confirm</button>
    </div>
    )
}

function CritStr({category, metric, handleCrit}) {
    const [str, setStr] = useState("")
    return (
        <div style = {{ display : "flex", alignItems: "center", gap: "10px" }}>
            <p>Please select the criteria for {metric}</p>
            <label>tarrif type </label>
            <input type="text" value={str} onChange={function (e) {
                setStr(e.target.value)
            }}/>
            <button onClick={function () {
            handleCrit(category, metric, str)
            }}>Confirm</button>
        </div> 
    )
}

function CritInt({category, metric, handleCrit}) {
    const [thresh, setThresh] = useState(0)
    return (
        <div style = {{ display : "flex", alignItems: "center", gap: "10px" }}>
            <p>Please select the criteria for {metric}</p>
            <input type="number" value={thresh} onChange={function (event) {
                setThresh(Number(event.target.value))
            }}/>
            <button onClick={function () {
            handleCrit(category, metric, thresh)
            }}>Confirm</button>
        </div>
    )
}

// this will also be passed down from the parent node

function CreateCritOptions({metrics}) {
    // helper function 
    function chooseType(metric) {
        if (metric.type == "bool") {
            return <CritBool category={metric.category} metric={metric.name} handleCrit={handleCrit}/>
        }
        else if (metric.type == "range") {
            return <CritRange category={metric.category} metric={metric.name} handleCrit={handleCrit}/>
        }
        else if (metric.type == "int") {
            return <CritInt category={metric.category} metric={metric.name} handleCrit={handleCrit}/>
        }
        else if (metric.type == "string") {
            return <CritStr category={metric.category} metric={metric.name} handleCrit={handleCrit}/>
        }
        else return null
    }
    return (
    <div> 
        {metrics.map(function(metric) {
        return (
            <div key={metric.name}> 
                {chooseType(metric)}
            </div>
        )
    })}
    </div> )
}

export default CreateCritOptions