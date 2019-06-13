# ThinkData Works Technical Assessment

### Objective

The _Tides, Currents, and Water Levels_ website provides predicted times and heights of high and low waters, and the hourly water levels for over seven hundred stations across Canada.
https://waterlevels.gc.ca/eng/Station/Month?type=1&sid=13320&tz=EST&pres=2&date=2019%2F06%2F30

Please write a script to capture the water/tidal level for each available city. The script is intended to run every day at a specific time, capturing any new information published since the previous run, and appending to a single file - eventually building a historical data set. The output of the script should be a CSV file that includes all useful meta data along with average water level for each day.

You are free to use any language but the resulting script should be executable.

### Solution

Python script `water.py` scrapes water/tidal information for 11 cities and compiles it in CSVs.

### How to run

1. Clone repo

2. From terminal, run command `python src/water.py`

### Areas of Improvement

- Documentation
- Make the date parameter of the URL dynamic so it works beyond the month of June 2019
