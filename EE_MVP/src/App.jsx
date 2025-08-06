import React from 'react'
import './App.css'
import UploadFile from './components/upload'
import CriteriaOptions from './components/criteria'
import WeightDropdown from './components/weights'
import AnalyzeInfo from './components/analyze'

function App() {
  // ---------- WEIGHTS/CRITERIA --------

  const metrics = [
    {category : "impact", name : "carbon", type : "range"},
    {category : "impact", name : "connections", type : "int"},
    {category : "impact", name : "women_consideration", type : "bool"},
    {category : "impact", name : "track_women", type : "int"},
    {category : "impact", name : "w_comm_prog", type : "int"},
    {category : "impact", name : "pue", type : "int"},
    {category : "impact", name : "econ_focus", type : "int"},

    {category : "finance", name : "capex", type : "range"},
    {category : "finance", name : "opex", type : "range"},
    {category : "finance", name : "cpc", type : "range"},
    {category : "finance", name : "lev_ratio", type : "int"},
    {category : "finance", name : "tariff_type", type : "string"},
    {category : "finance", name : "tariff", type : "range"},
    {category : "finance", name : "lcoe", type : "range"},
    {category : "finance", name : "requested_funds", type : "range"},

    {category : "dev", name : "per_local_tech", type : "int"},

    {category : "tech", name : "scalable", type : "bool"},
    {category : "tech", name : "solution", type : "string"},
    {category : "tech", name : "monitering", type : "bool"},
    {category : "tech", name : "backup", type : "bool"},

    {category : "timeline", name : "duration", type : "range"},
  ]
  const weights = [
   
    {category : "grand", name : "impact"},
    {category : "grand", name : "finance"},
    {category : "grand", name : "tech"},
    {category : "grand", name : "dev"},
    {category : "grand", name : "timeline"},
    
    {category : "impact", name : "carbon"},
    {category : "impact", name : "connections"},
    {category : "impact", name : "women_consideration"},
    {category : "impact", name : "track_women"},
    {category : "impact", name : "w_comm_prog"},
    {category : "impact", name : "pue"},
    {category : "impact", name : "econ_focus"},

    {category : "finance", name : "capex"},
    {category : "finance", name : "opex"},
    {category : "finance", name : "cpc"},
    {category : "finance", name : "lev_ratio"},
    {category : "finance", name : "tariff_type"},
    {category : "finance", name : "tariff"},
    {category : "finance", name : "lcoe"},
    {category : "finance", name : "requested_funds"},

    {category : "dev", name : "per_local_tech"},

    {category : "tech", name : "scalable"},
    {category : "tech", name : "solution"},
    {category : "tech", name : "monitering"},
    {category : "tech", name : "backup"},

    {category : "timeline", name : "duration"},
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
