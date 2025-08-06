import React from 'react';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

function ScoreCircle({ value, label }) {
  return (
    <div style={{ width: 100, margin: '10px' }}>
      <CircularProgressbar
        value={value}
        text={`${value}%`}
        styles={buildStyles({
          textColor: "#000",
          pathColor: "#3e98c7",
          trailColor: "#eee",
        })}
      />
      <p style={{ textAlign: 'center' }}>{label}</p>
    </div>
  );
}

function Dashboard(data) {
    const scores = [
      { name: 'data.name', value: 85 },
      { name: 'Finance', value: 70 },
      { name: 'Tech', value: 60 },
    ];
  
    return (
      <div style={{ display: 'flex', gap: '20px' }}>
        {scores.map(score => (
          <ScoreCircle key={score.name} value={score.value} label={score.name} />
        ))}
      </div>
    );
  }