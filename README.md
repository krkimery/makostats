# makostats
Football Stats project: scrape for data, then rank teams


#(Ongoing) Refactor


##Consts File
The bulk of the content of this module is random bits of regex and small snippets of logic for parsing. It's a bit of a mess. I think the biggest improvement could be made by breaking these random regexes and logic nuggets into a constants file separate from the logic of the rankings, etc. 

I imagine the constants file would be dict mapping of attr name, ie "winPercent" to a list of: corresponding regex, corresponding filter logic (as simple lambda func), regex group number for that attr, and whatever else may be needed. 

This way you can simply loop through all of the keys in these dict, and then add the attributes on the class as:

    setattr( self, constsDictKey, htmlRegex -> logicFunc )


##Storage
It seems fairly obvious that older data should be stored for backtesting purposes and historical records. Whether that's some kind of DB or even just pickling the teams. 

##Testing
Testing is important and worthwhile.

##Scrape Improvements
Should probably be using requests. Should consider using other websites/sources of data. Should consider adding in random sleeps to obfuscate the scrape.

##Parse Improvements
In addition to the larger refactor mentioned above, should consider alternative parsing solutions, ie BeautifulSoup.

