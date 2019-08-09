# makostats
Football Stats project: scrape for data, then rank teams

[![Coverage Status](https://coveralls.io/repos/github/krkimery/makostats/badge.svg?branch=master)](https://coveralls.io/github/krkimery/makostats?branch=master)

## Setup
Must have installed: requests, bs4, mock


# Further Development
In addition to the below refactors, this is an actively developed project. 

I would like to further expand the algorithms with hand-curated ranking algorithms and play around a bit with some very 
simple machine learning concepts.

I would like to replace the existing data storage solution(s) with an object store capable of time-travel, to enable
back-testing of ranking algorithms. Alternatively, I could pursue boring/traditional DBs. 

At some point in the distant future, I would like to integrate all of this with a simple web framework (just because). A
more medium-term front-end development would be to use a simple plotting library like matplotlib to visualize data. 

# (Ongoing) Refactor

## Status and Next tasks
Working release. All initial functionality at least at a trivial level. Check stored/archived data, scrape for new data,
rank teams based upon ranking algorithms defined in a separate algos module. Team objects are created with dynamic attrs
based off of the elements scraped & cleaned from website. 

Tests are complete but could (like always) be added to and improved upon. 

I need to determine how I want to store older data. Pickling is memory and time inefficient. Intermediate improvement: 
store data as JSON. Create load_from_JSON and dump_to_JSON class methods on Team. Build dynamic init. Long term ideas
to explore: zodb (object store which may support time-travel), traditional DBs. 

The JSON refactor is complete!


## Consts File
This should be done, barring any additions at a later date. 


## Storage
The JSON refactor is complete! Longer term I would like to look into time-travelable DBs (zodb?) or a more traditional 
DB. 

## Testing
Testing is important and worthwhile.

## Scrape Improvements
Done! May want to consider further scrape obfuscation methods. 

## Parse Improvements
Done!

