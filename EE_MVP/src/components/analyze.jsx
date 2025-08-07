import React, { useState } from 'react';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

function GetScores() {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    async function handleResponse() {
        try {
            const response = await fetch("http://localhost:8000/analyze", {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            });

            if (!response.ok) {
                throw new Error("Information not received");
            }
            const json = await response.json();
            setData(json);
            console.log(data)
        } catch (err) {
            setError(err.message);
        }
    }

    function ScoreCircle({ label, value }) {
        let color = "#3e98c7";  // default blue
    
        if (value <= 20) color = "#f44336";         // red
        else if (value <= 49) color = "#ff9800";    // orange
        else if (value <= 69) color = "#ffeb3b";    // yellow
        else if (value <= 89) color = "#8bc34a";    // light green
        else color = "#4caf50";                     // green
    
        return (
            <div style={{ width: 100, margin: '10px', textAlign: 'center' }}>
                <CircularProgressbar
                    value={value}
                    text={`${value}%`}
                    styles={buildStyles({
                        textColor: '#fff',
                        pathColor: color,
                        trailColor: '#444',
                    })}
                />
                <p style={{ color: '#fff' }}>{label}</p>
            </div>
        );
    }

    return (
        <div>
            <button onClick={handleResponse}>Analyze</button>
            {error && <p style={{ color: 'red' }}>Error: {error}</p>}
            {data && (
                <div>
                    <label>Here are the following scores:</label>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '20px' }}>
                        <ScoreCircle label="Overall" value={data.overall} />
                        <ScoreCircle label="Impact" value={data.impact} />
                        <ScoreCircle label="Finance" value={data.finance} />
                        <ScoreCircle label="Local Dev" value={data.dev} />
                        <ScoreCircle label="Technical" value={data.tech} />
                        <ScoreCircle label="Timeline" value={data.timeline} />
                    </div>
                    <div style={{ marginTop: '20px' }}>
                        <p><strong>Feedback:</strong></p>
                        <pre>{JSON.stringify(data.feed, null, 2)}</pre>
                    </div>
                </div>
            )}
        </div>
    );
}

export default GetScores;
