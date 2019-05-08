# makostats
Football Stats project: scrape for data, then rank teams

## Setup
Must have installed: requests, bs4, mock


# Further Development
In addition to the below refactors, this is an actively developed project. 

I would like to further expand the algorithms with hand-curated ranking algorithms and play around a bit with some very 
simple machine learning concepts.

I would like to replace the existing data storage solution(s) with an object store capable of time-travel, to enable
back-testing of ranking algorithms. Alternatively, I could pursue boring/traditional DBs. 

At some point in the distant future, I would like to integrate all of this with a simple web framework (just because). 

# (Ongoing) Refactor

## Status and Next tasks
Working release. All initial functionality at least at a trivial level. Check stored/archived data, scrape for new data,
rank teams based upon ranking algorithms defined in a separate algos module. Team objects are created with dynamic attrs
based off of the elements scraped & cleaned from website. 

I need to create a full fledged test case for the new class, complete with dummy html. In general, new functionality 
demands tests. I've been too lax with testing thus far.  

I need to determine how I want to store older data. Pickling is memory and time inefficient. Intermediate improvement: 
store data as JSON. Create load_from_JSON and dump_to_JSON class methods on Team. Build dynamic init. Long term ideas
to explore: zodb (object store which may support time-travel), traditional DBs. 


## Consts File
This should be done, barring any additions at a later date. 


## Storage
Currently pickling, intermediate solution is JSON. In the future, I will look into using some kind of database, possibly
zodb. This works... sort of... pickle has shortcomings, for temporary storage (so I can stop hitting the website) this is
fine. But I will definitely need to look into a traditional DB. 

## Testing
Testing is important and worthwhile.

## Scrape Improvements
Done! May want to consider further scrape obfuscation methods. 

## Parse Improvements
Done!

