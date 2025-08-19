import React from 'react'
import './App.css'
import UploadFile from './components/upload'
import CriteriaOptions from './components/criteria'
import WeightDropdown from './components/weights'
import AnalyzeInfo from './components/analyze'



function App() {
  // ---------- WEIGHTS/CRITERIA --------

  const metrics = [
    {category : "impact", name : "carbon", type : "range", label : "the # carbon emissions avoided"},
    {category : "impact", name : "connections", type : "int", label : "the # of connections"},
    {category : "impact", name : "women_consideration", type : "bool", label : "women's inclusion in the development process"},
    {category : "impact", name : "track_women", type : "int", label : "the # of mechanisms to track women's progress"},
    {category : "impact", name : "w_comm_prog", type : "int", label : "the # of female community programs"},
    {category : "impact", name : "pue", type : "int", label : "the # of PUEs"},
    {category : "impact", name : "econ_focus", type : "int", label : "the focus on economic development"},

    {category : "finance", name : "capex", type : "range", label : "the project's CAPEX"},
    {category : "finance", name : "opex", type : "range", label : "the project's OPEX"},
    {category : "finance", name : "cpc", type : "range", label : "the project's CPC"},
    {category : "finance", name : "lev_ratio", type : "int", label : "the project's leverage ratio"},
    {category : "finance", name : "tariff_type", type : "string", label : "the type of tariff used"},
    {category : "finance", name : "tariff", type : "range", label : "the tariff cost per user"},
    {category : "finance", name : "lcoe", type : "range", label : "the LCOE"},
    {category : "finance", name : "requested_funds", type : "range", label : "the amount of funds requested"},

    {category : "dev", name : "per_local_tech", type : "int", label : "the percent of local technicians employed"},

    {category : "tech", name : "scalable", type : "bool", label : "project scalability"},
    {category : "tech", name : "solution", type : "string", label : "the project's energy solution"},
    {category : "tech", name : "monitering", type : "bool", label : "the project's monitering capacities"},
    {category : "tech", name : "backup", type : "bool", label : "the project's backup generation capacities"},

    {category : "timeline", name : "duration", type : "range", label : "the length of the project"},
  ]
  const weights = [
   
    {category : "grand", name : "impact", label : "the project's impact performance"},
    {category : "grand", name : "finance", label : "the project's financial performance"},
    {category : "grand", name : "tech", label : "the project's technical performance"},
    {category : "grand", name : "dev", label : "the project's local development and inclusion performance"},
    {category : "grand", name : "timeline", label : "the project's timeline"},
    
    {category : "impact", name : "carbon", label : "the # carbon emissions avoided"},
    {category : "impact", name : "connections", label : "the # of connections"},
    {category : "impact", name : "women_consideration", label : "including women in the development process"},
    {category : "impact", name : "track_women", label : "the # of mechanisms to track women's progress"},
    {category : "impact", name : "w_comm_prog", label : "the # of female community programs"},
    {category : "impact", name : "pue", label : "the # of PUEs"},
    {category : "impact", name : "econ_focus", label : "the focus on economic development"},

    {category : "finance", name : "capex", label : "the CAPEX"},
    {category : "finance", name : "opex", label : "the OPEX"},
    {category : "finance", name : "cpc", label : "the CPC"},
    {category : "finance", name : "lev_ratio", label : "the leverage ratio"},
    {category : "finance", name : "tariff_type", label : "the type of tarrif implemented"},
    {category : "finance", name : "tariff", label : "the tariff cost"},
    {category : "finance", name : "lcoe", label : "the LCOE"},
    {category : "finance", name : "requested_funds", label : "the amount of funds requested"},

    {category : "dev", name : "per_local_tech", label : "the percent of local technicians employed"},

    {category : "tech", name : "scalable", label : "project scalability"},
    {category : "tech", name : "solution", label : "the project's energy solution"},
    {category : "tech", name : "monitering", label : "the project's monitering capabilities"},
    {category : "tech", name : "backup", label : "the project's backup generation capacities"},

    {category : "timeline", name : "duration", label : "the length of the project"},
  ]

  return (
    <>
        <h1>EmpowerEnergy MVP</h1>
        <p> This is a draft of the EmpowerEnergy MVP </p>
        <hr />
        <h2>Upload Proposal PDF</h2>
        <UploadFile/>
        <hr />
        <hr />
        <hr />
        <h2>Input Desired Criteria</h2>
        <CriteriaOptions metrics={metrics}/>
        <hr />
        <hr />
        <hr />
        <h2>Input Desired Weights</h2>
        <WeightDropdown weights={weights}/>
        <hr />
        <hr />
        <hr />
        <AnalyzeInfo/>
        
    </>
  )
}

export default App
