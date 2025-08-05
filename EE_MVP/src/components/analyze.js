import React, { useState } from 'react';

function GetScores() {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    async function handleResponse() {
        try {
            const response = await fetch("http://localhost:8000", {
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
    return (
        <div>
            <button onClick={handleResponse}>Analyze</button>

            {error && <p style={{ color: 'red' }}>Error: {error}</p>}

            {data && (
                <div>
                    <label>Here are the following scores:</label>
                    <p>
                        Overall Score: {data.overall}<br />
                        Impact Score: {data.impact}<br />
                        Finance Score: {data.finance}<br />
                        Local Development Score: {data.dev}<br />
                        Technical Score: {data.tech}<br />
                        Timeline Score: {data.timeline}
                    </p>
                    <p>
                        Feedback:<br />
                        {data.feed}
                    </p>
                </div>
            )}
        </div>
    );
}

export default GetScores;