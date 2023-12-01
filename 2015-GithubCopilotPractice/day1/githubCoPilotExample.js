// press tab to select the option and esc to abort
function calculateDaysBetweenDates(begin, end) {
    const beginDate = new Date(begin);
    const endDate = new Date(end);
    const millisecondsPerDay = 1000 * 60 * 60 * 24;
    const millisBetween = endDate.getTime() - beginDate.getTime();
    const days = millisBetween / millisecondsPerDay;
    return Math.floor(days);
}

// OPTION + ] to select the next suggestion
function calculateDaysBetweenDates(begin, end) {
    const beginDate = new Date(begin);
    const endDate = new Date(end);
    const millisecondsPerDay = 1000 * 60 * 60 * 24;
    const millisBetween = endDate.getTime() - beginDate.getTime();
    const days = millisBetween / millisecondsPerDay;
    return Math.floor(days)
}

// Try Ctrl + Enter for suggestions in a new tab
function calculateDaysBetweenDates(begin, end) {

}

// find all images without alternate text
// and give them a red border
func process() {
    const images = document.querySelectorAll('img');
    for (const image of images) {
        if (!image.alt) {
            image.style.border = '5px solid red';
        }
    }
}

// suggestions for api or framework
// Express server on port 3000
const express = require('express');
const app = express();
app.get('/', (req, res) => {
    res.send('Hello World!');
}
);
app.listen(3000, () => console.log('Server ready'));

// Return the current time
function getTime() {
    return new Date().toLocaleTimeString();
}