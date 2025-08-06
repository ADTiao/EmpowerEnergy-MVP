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
        } catch (err) {
            setError(err.message);
        }
    }

    function ScoreCircle({ label, value }) {
        return (
            <div style={{ width: 100, margin: '10px', textAlign: 'center' }}>
                <CircularProgressbar
                    value={value}
                    text={`${value}%`}
                    styles={buildStyles({
                        textColor: '#000',
                        pathColor: '#3e98c7',
                        trailColor: '#eee',
                    })}
                />
                <p>{label}</p>
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
                        <p>{data.feed}</p>
                    </div>
                </div>
            )}
        </div>
    );
}

export default GetScores;
