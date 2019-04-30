# makostats
Football Stats project: scrape for data, then rank teams

## Setup
Must have installed: requests, bs4, mock


# (Ongoing) Refactor

## Status and Next tasks
I believe I've got read stats essentially finished in scratch. I have stats, splits, and derived stats.
I've tested the new class against all 120+ teams, and they all successfully pulled and init'd. I need to actually go in
and replace the exisiting code in fbReadStats with the new scratch code. All stats and derived stats should be present.

I've updated the consts file to be a dict of dicts. This could use some pretty-ifing. I've added simple test for this
module as well. 

I've created an algos.py for storing the manually created algorithms. This has a trivial test file as well. I've managed
to recreate the original mako function in this new algos file using the new class and new attributes. 

I need to create a full fledged test case for the new class, complete with dummy html. 

I need to determine how I want to store older data, pickling or otherwise. 


## Consts File
The bulk of the content of this module is random bits of regex and small snippets of logic for parsing. It's a bit of a mess. I think the biggest improvement could be made by breaking these random regexes and logic nuggets into a constants file separate from the logic of the rankings, etc. 

I imagine the constants file would be dict mapping of attr name, ie "winPercent" to a list of: corresponding regex, corresponding filter logic (as simple lambda func), regex group number for that attr, and whatever else may be needed. 

This way you can simply loop through all of the keys in these dict, and then add the attributes on the class as:

    setattr( self, constsDictKey, htmlRegex -> logicFunc )


## Storage
It seems fairly obvious that older data should be stored for backtesting purposes and historical records. Whether that's some kind of DB or even just pickling the teams. 

## Testing
Testing is important and worthwhile.

## Scrape Improvements
Should probably be using requests. Should consider using other websites/sources of data. Should consider adding in random sleeps to obfuscate the scrape.

## Parse Improvements
In addition to the larger refactor mentioned above, should consider alternative parsing solutions, ie BeautifulSoup.

