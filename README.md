# makostats
Football Stats project: scrape for data, then rank teams

## Setup
Must have installed: requests, bs4, mock


# (Ongoing) Refactor

## Status and Next tasks
I believe I've got read stats essentially finished. I have stats, splits, and derived stats.
I've tested the new class against all 120+ teams, and they all successfully pulled and init'd. 


I've created an algos.py for storing the manually created algorithms. This has a trivial test file as well. I've managed
to recreate the original mako function in this new algos file using the new class and new attributes. All new algorithms
will be built out in this file. 

I need to create a full fledged test case for the new class, complete with dummy html. 

I need to determine how I want to store older data, pickling or otherwise. 


## Consts File
This should be done, barring any additions at a later date. 


## Storage
My initial storage solution will be pickling teams. In the future, I will look into using some kind of database, possibly
zodb. This works... sort of... pickle has shortcomings, for temporary storage (so I can stop hitting the website) this is
fine. But I will definitely need to look into a traditional DB. 

Intermediate solution is store data as JSON

## Testing
Testing is important and worthwhile.

## Scrape Improvements
Done! May want to consider further scrape obfuscation methods. 

## Parse Improvements
Done!

