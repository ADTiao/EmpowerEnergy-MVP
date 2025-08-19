import React, { useState } from 'react';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';
import { Box, Heading, Text } from "@chakra-ui/react";



function InfoBox({ title, flags }) {
    return (
      <Box
        borderWidth="1px"
        borderRadius="lg"
        p={4}
        m={2}
        boxShadow="md"
        bg="black"
        color="white"           // make text readable on black
      >
        <Heading size="md">{title}</Heading>
        <Box mt={2}>{flags}</Box>   {/* NOT <Text> — avoids <p> inside <p> */}
      </Box>
    );
  }

function GetScores() {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    async function handleResponse() {
        try {
            const response = await fetch("http://localhost:8000/analyze", {
                method: "GET",
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
    
    function FeedBoxes({ feed_info }) {
        return (
          <>
            {Object.entries(feed_info).map(([key, feedback]) => {
              const flags = Object.entries(feedback).map(([metric, info], index) => (
                <Text key={index}>{index + 1}: {info}</Text>
              ));
              return <InfoBox key={key} title={key} flags={flags} />;
            })}
          </>
        );
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
                        <ScoreCircle label="Local Economic Development" value={data.dev} />
                        <ScoreCircle label="Technical" value={data.tech} />
                        <ScoreCircle label="Timeline" value={data.timeline} />
                    </div>
                    <div style={{ marginTop: '20px' }}>
                        <p><strong>FLAGS:</strong></p>
                        <FeedBoxes feed_info={data.feed}/>
                    </div>
                </div>
            )}
        </div>
    );
}

export default GetScores;
