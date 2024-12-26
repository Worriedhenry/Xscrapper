const mongoose = require('mongoose');
const express = require('express');
const cors = require('cors');
const { exec } = require('child_process')
const path = require('path'); 
require('dotenv').config();
const TrendSchema=require('./db');
const app = express();
app.use(cors());
app.use(express.json());



// API endpoint to scrape trends
app.get('/scrape',async (req, res) => {
    try {
        // Run the Python scraper script using child_process
        exec('python ./scrapper.py', (error, stdout, stderr) => {
            if (error) {
                console.error(`exec error: ${error}`);
                return res.status(500).json({ error: `Error executing scraper: ${error.message}` });
            }
            if (stderr) {
                console.error(`stderr: ${stderr}`);
                return res.status(500).json({ error: `Error in scraper execution: ${stderr}` });
            }

            // Parse the stdout to get the result
            const result = JSON.parse(stdout); // Assuming the scraper script outputs JSON
            console.log(result);
            const Trend= TrendSchema(result);
            Trend.save(); 
            res.status(200).json({ message: 'Scraping successful', data: result ,Trend });
        });
    } catch (error) {
        res.status(500).json({ error: `Error: ${error.message}` });
    }
});

// API endpoint to fetch the latest trends from DB
// app.get('/latest', async (req, res) => {
//     try {
//         const data = await fetchLatest();
//         res.status(200).json(data);
//     } catch (error) {
//         res.status(500).json({ error: error.message });
//     }
// });

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
