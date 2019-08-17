"""
    Consts file for scraping, parsing, and ranking

"""
import os

HTTP_HEADERS = {
                            "User-Agent":   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                                            "(KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
                }

DATA_FILENAME = os.getcwd() + "\\data\\" + "data_"

JSON_FILE = "json_data"

DATA = {

    'Florida State Seminoles':          {"URL": 234,
                                        "Conference": "ACC",
                                        },
    'Purdue Boilermakers':              {"URL": 559,
                                        "Conference": "B10",
                                        },
    'Vanderbilt Commodores':            {"URL": 736,
                                        "Conference": "SEC",
                                        },
    'Miami (Florida) Hurricanes':       {"URL": 415,
                                        "Conference": "ACC",
                                        },
    'Arizona Wildcats':                 {"URL": 29,
                                        "Conference": "PAC12",
                                        },
    'Utah Utes':                        {"URL": 732,
                                        "Conference": "PAC12",
                                        },
    'Nevada Wolf Pack':                 {"URL": 466,
                                        },
    'Ohio Bobcats':                     {"URL": 519,
                                        },
    'California Golden Bears':          {"URL": 107,
                                        "Conference": "PAC12",
                                        },
    'Michigan Wolverines':              {"URL": 418,
                                        "Conference": "B10",
                                        },
    'Florida Atlantic Owls':            {"URL": 229,
                                        },
    'Duke Blue Devils':                 {"URL": 193,
                                        "Conference": "ACC",
                                        },
    'Bowling Green Falcons':            {"URL": 71,
                                        },
    'Fresno State Bulldogs':            {"URL": 96,
                                        },
    'Wake Forest Demon Deacons':        {"URL": 749,
                                        "Conference": "ACC",
                                        },
    'Utah State Aggies':                {"URL": 731,
                                        },
    'Minnesota Golden Gophers':         {"URL": 428,
                                        "Conference": "B10",
                                        },
    'Ball State Cardinals':             {"URL": 47,
                                        },
    'BYU Cougars':                      {"URL": 77,
                                        },
    'Auburn Tigers':                    {"URL": 37,
                                        "Conference": "SEC",
                                        },
    'Navy Midshipmen':                  {"URL": 726,
                                        },
    'Colorado Buffaloes':               {"URL": 157,
                                        "Conference": "PAC12",
                                        },
    'Northwestern Wildcats':            {"URL": 509,
                                        "Conference": "B10",
                                        },
    'Rutgers Scarlet Knights':          {"URL": 587,
                                        "Conference": "B10",
                                        },
    'Maryland Terrapins':               {"URL": 392,
                                        "Conference": "B10",
                                        },
    'North Carolina Tar Heels':         {"URL": 457,
                                        "Conference": "ACC",
                                        },
    'Kent State Golden Flashes':        {"URL": 331,
                                        },
    'South Florida Bulls':              {"URL": 651,
                                        },
    'Oklahoma State Cowboys':           {"URL": 521,
                                        "Conference": "B12",
                                        },
    'Buffalo Bulls':                    {"URL": 86,
                                        },
    "Hawai'i Warriors":                 {"URL": 277,
                                        },
    'North Texas Mean Green':           {"URL": 497,
                                        },
    'SMU Mustangs':                     {"URL": 663,
                                        },
    'Oregon State Beavers':             {"URL": 528,
                                        "Conference": "PAC12",
                                        },
    'Army Black Knights':               {"URL": 725,
                                        },
    'Northern Illinois Huskies':        {"URL": 503,
                                        },
    'Illinois Fighting Illini':         {"URL": 301,
                                        "Conference": "B10",
                                        },
    'Iowa Hawkeyes':                    {"URL": 312,
                                        "Conference": "B10",
                                        },
    'West Virginia Mountaineers':       {"URL": 768,
                                        "Conference": "B12",
                                        },
    'UCF Knights':                      {"URL": 128,
                                        },
    'Western Michigan Broncos':         {"URL": 774,
                                        },
    'Rice Owls':                        {"URL": 574,
                                        },
    'Kansas Jayhawks':                  {"URL": 328,
                                        "Conference": "B12",
                                        },
    'TCU Horned Frogs':                 {"URL": 698,
                                        "Conference": "B12",
                                        },
    'Syracuse Orange':                  {"URL": 688,
                                        "Conference": "ACC",
                                        },
    'Virginia Cavaliers':               {"URL": 746,
                                        "Conference": "ACC",
                                        },
    'Mississippi Rebels':               {"URL": 433,
                                        "Conference": "SEC",
                                        },
    'Louisiana Tech Bulldogs':          {"URL": 366,
                                        },
    'Texas A&M Aggies':                 {"URL": 697,
                                        "Conference": "SEC",
                                        },
    'Washington Huskies':               {"URL": 756,
                                        "Conference": "PAC12",
                                        },
    'San Diego State Aztecs':           {"URL": 626,
                                        },
    'Colorado State Rams':              {"URL": 156,
                                        },
    'UCLA Bruins':                      {"URL": 110,
                                        "Conference": "PAC12",
                                        },
    'Arkansas State Red Wolves':        {"URL": 30,
                                        },
    'Connecticut Huskies':              {"URL": 164,
                                        },
    'North Carolina State Wolfpack':    {"URL": 490,
                                        "Conference": "ACC",
                                        },
    'Central Michigan Chippewas':       {"URL": 129,
                                        },
    'Eastern Michigan Eagles':          {"URL": 204,
                                        },
    'Texas Tech Red Raiders':           {"URL": 700,
                                        "Conference": "B12",
                                        },
    'Notre Dame Fighting Irish':        {"URL": 513,
                                        "Conference": "ACC",
                                        },
    'Alabama Crimson Tide':             {"URL": 8,
                                        "Conference": "SEC",
                                        },
    'South Carolina Gamecocks':         {"URL": 648,
                                        "Conference": "SEC",
                                        },
    'San Jose State Spartans':          {"URL": 630,
                                        },
    'UTEP Miners':                      {"URL": 704,
                                        },
    'UNLV Rebels':                      {"URL": 465,
                                        },
    'Louisville Cardinals':             {"URL": 367,
                                        "Conference": "ACC",
                                        },
    'Indiana Hoosiers':                 {"URL": 306,
                                        "Conference": "B10",
                                        },
    'Air Force Falcons':                {"URL": 721,
                                        },
    'Georgia State Panthers':           {"URL": 254,
                                        },
    'Florida International Golden Panthers': {"URL": 231,
                                              },
    'Georgia Tech Yellow Jackets':      {"URL": 255,
                                        "Conference": "ACC",
                                        },
    'Middle Tennessee Blue Raiders':    {"URL": 419,
                                        },
    'Texas Longhorns':                  {"URL": 703,
                                        "Conference": "B12",
                                        },
    'Missouri Tigers':                  {"URL": 434,
                                        "Conference": "SEC",
                                        },
    'New Mexico State Aggies':          {"URL": 472,
                                        },
    'Miami (Ohio) RedHawks':            {"URL": 414,
                                        },
    'Boston College Eagles':            {"URL": 67,
                                        },
    'Mississippi State Bulldogs':       {"URL": 430,
                                        "Conference": "SEC",
                                        },
    'Florida Gators':                   {"URL": 235,
                                        "Conference": "SEC",
                                        },
    'East Carolina Pirates':            {"URL": 196,
                                        },
    'Western Kentucky Hilltoppers':     {"URL": 772,
                                        },
    'Penn State Nittany Lions':         {"URL": 539,
                                        "Conference": "B10",
                                        },
    "Louisiana-Lafayette Ragin' Cajuns": {"URL": 671,
                                          },
    'Memphis Tigers':                   {"URL": 404,
                                        },
    'Boise State Broncos':              {"URL": 66,
                                        },
    'Wyoming Cowboys':                  {"URL": 811,
                                        },
    'Tennessee Volunteers':             {"URL": 694,
                                        "Conference": "SEC",
                                        },
    'Wisconsin Badgers':                {"URL": 796,
                                        "Conference": "B10",
                                        },
    'New Mexico Lobos':                 {"URL": 473,
                                        },
    'Houston Cougars':                  {"URL": 288,
                                        },
    'Washington State Cougars':         {"URL": 754,
                                        "Conference": "PAC12",
                                        },
    'UTSA Roadrunners':                 {"URL": 706,
                                        },
    'Ohio State Buckeyes':              {"URL": 518,
                                        "Conference": "B10",
                                        },
    'South Alabama Jaguars':            {"URL": 646,
                                        },
    'Virginia Tech Hokies':             {"URL": 742,
                                        "Conference": "ACC",
                                        },
    'Toledo Rockets':                   {"URL": 709,
                                        },
    'Georgia Southern Eagles':          {"URL": 253,
                                        },
    'Tulsa Golden Hurricane':           {"URL": 719,
                                        },
    'Arkansas Razorbacks':              {"URL": 31,
                                        "Conference": "SEC",
                                        },
    'Clemson Tigers':                   {"URL": 147,
                                        "Conference": "ACC",
                                        },
    'Tulane Green Wave':                {"URL": 718,
                                        },
    'Idaho Vandals':                    {"URL": 295,
                                        },
    'Oregon Ducks':                     {"URL": 529,
                                        "Conference": "PAC12",
                                        },
    'Massachusetts Minutemen':          {"URL": 400,
                                        },
    'Cincinnati Bearcats':              {"URL": 140,
                                        },
    'Marshall Thundering Herd':         {"URL": 388,
                                        },
    'LSU Tigers':                       {"URL": 365,
                                        "Conference": "SEC",
                                        },
    'Louisiana-Monroe Warhawks':        {"URL": 498,
                                        },
    'Georgia Bulldogs':                 {"URL": 257,
                                        "Conference": "SEC",
                                        },
    'Michigan State Spartans':          {"URL": 416,
                                        "Conference": "B10",
                                        },
    'Pittsburgh Panthers':              {"URL": 545,
                                        "Conference": "ACC",
                                        },
    'Southern Mississippi Golden Eagles': {"URL": 664,
                                           },
    'Baylor Bears':                     {"URL": 51,
                                        "Conference": "B12",
                                        },
    'Old Dominion Monarchs':            {"URL": 523,
                                        },
    'Iowa State Cyclones':              {"URL": 311,
                                        "Conference": "B12",
                                        },
    'USC Trojans':                      {"URL": 657,
                                        "Conference": "PAC12",
                                        },
    'Oklahoma Sooners':                 {"URL": 522,
                                        "Conference": "B12",
                                        },
    'Charlotte 49ers':                  {"URL": 458,
                                        },
    'Stanford Cardinal':                {"URL": 674,
                                        "Conference": "PAC12",
                                        },
    'Arizona State Sun Devils':         {"URL": 28,
                                        "Conference": "PAC12",
                                        },
    'Kansas State Wildcats':            {"URL": 327,
                                        "Conference": "B12",
                                        },
    'Kentucky Wildcats':                {"URL": 334,
                                        "Conference": "SEC",
                                        },
    'Troy Trojans':                     {"URL": 716,
                                        },
    'Temple Owls':                      {"URL": 690,
                                        },
    'Nebraska Cornhuskers':             {"URL": 463,
                                        "Conference": "B12",
                                        },
    'Texas State Bobcats':              {"URL": 670,
                                        },
    'Appalachian State Mountaineers':   {"URL": 27,
                                        },
    'Akron Zips':                       {"URL": 5,
                                        },

    }

TEAMS = DATA.keys()

YEARS = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]

BASE_URL = 'http://www.cfbstats.com/{YEAR}/team/{NUMBER}/index.html'

URL_LIST = [721, 5, 8, 27, 29, 28, 31, 30, 725, 37, 77, 47, 51, 66, 67, 71, 86, 107, 129, 458, 140, 147, 157, 156, 164,
            193, 196, 204, 235, 229, 231, 234, 96, 257, 253, 254, 255, 277, 288, 295, 301, 306, 312, 311, 328, 327, 331,
            334, 365, 366, 671, 498, 367, 388, 392, 400, 404, 415, 414, 418, 416, 419, 428, 433, 430, 434, 726, 463,
            466, 473, 472, 457, 490, 497, 503, 509, 513, 519, 518, 522, 521, 523, 529, 528, 539, 545, 559, 574, 587,
            663, 626, 630, 646, 648, 651, 664, 674, 688, 698, 690, 694, 703, 697, 670, 700, 709, 716, 718, 719, 128,
            110, 465, 657, 704, 706, 732, 731, 736, 746, 742, 749, 756, 754, 768, 772, 774, 796, 811]


AP_RANKING = {
                2018: ["Clemson Tigers", "Alabama Crimson Tide", "Ohio State Buckeyes", "Oklahoma Sooners", "Notre Dame Fighting Irish", "LSU Tigers", "Florida Gators", "Georgia Bulldogs", "Texas Longhorns", "Washington State Cougars", "UCF Knights", "Kentucky Wildcats", "Washington Huskies", "Michigan Wolverines", "Syracuse Orange", "Texas A&M Aggies", "Penn State Nittany Lions", "Fresno State Bulldogs", "Army Black Knights", "West Virginia Mountaineers", "Northwestern Wildcats", "Utah State Aggies", "Boise State Broncos", "Cincinnati Bearcats", "Iowa Hawkeyes" ],
                2017: ["Alabama Crimson Tide", "Georgia Bulldogs", "Oklahoma Sooners", "Clemson Tigers", "Ohio State Buckeyes", "UCF Knights", "Wisconsin Badgers", "Penn State Nittany Lions", "TCU Horned Frogs", "Auburn Tigers", "Notre Dame Fighting Irish", "USC Trojans", "Miamia (Florida) Hurricanes", "Oklahoma State Cowboys", "Michigan State Spartans", "Washington Huskies", "Northwestern Wildcats", "LSU Tigers", "Mississippi State Bulldogs", "Stanford Cardinal", "South Florida Bulls", "Boise State Broncos", "North Carolina State Wolfpack", "Virginia Tech Hokies", "Memphis Tigers"],
                2016: ["Clemson Tigers", "Alabama Crimson Tide", "USC Trojans", "Washington Huskies", "Oklahoma Sooners", "Ohio State Buckeyes", "Penn State Nittany Lions", "Florida State Seminoles", "Wisconsin Badgers", "Michigan Wolverines", "Oklahoma State Cowboys", "Stanford Cardinal", "LSU Tigers", "Florida Gators", "Western Michigan Broncos", "Virginia Tech Hokies", "Colorado Buffaloes", "West Virginia Mountaineers", "South Florida Bulls", "Miami (Florida) Hurricanes", "Louisville Cardinals", "Tennessee Volunteers", "Utah Utes", "Auburn Tigers", "San Diego State Aztecs", ],
                2015: ["Alabama Crimson Tide","Clemson Tigers","Stanford Cardinal","Oklahoma Sooners","Ohio State Buckeyes","Michigan State Spartans","TCU Horned Frogs","Mississippi Rebels", "Notre Dame Fighting Irish", "Michigan Wolverines","Baylor Bears","North Carolina Tar Heels","Florida State Seminoles","Oklahoma State Cowboys","LSU Tigers","Utah Utes","Oregon Ducks","Florida Gators","Tennessee Volunteers","Northwestern Wildcats","USC Trojans","Mississippi State Bulldogs","Georgia Bulldogs"],
                2014: ["Ohio State Buckeyes","Oregon Ducks","TCU Horned Frogs","Alabama Crimson Tide","Florida State Seminoles","Michigan State Spartans","Baylor Bears","Georgia Tech Yellow Jackets","Georgia Bulldogs","UCLA Bruins","Mississippi State Bulldogs","Arizona State Sun Devils","Wisconsin Badgers","Missouri Tigers","Clemson Tigers","Mississippi Rebels","Kansas State Wildcats","Arizona Wildcats","USC Trojans","Utah Utes","Auburn Tigers","Louisville Cardinals","Notre Dame Fighting Irish","Stanford Cardinal","Nebraska Cornhuskers",],
                2013: ["Florida State Seminoles","Auburn Tigers","Michigan State Spartans","South Carolina Gamecocks","Missouri Tigers","Oklahoma Sooners","Alabama Crimson Tide","Clemson Tigers","Oregon Ducks","Stanford Cardinal","Ohio State Buckeyes","Baylor Bears","LSU Tigers","Louisville Cardinals","UCLA Bruins","Oklahoma State Cowboys","Texas A&M Aggies","USC Trojans","Notre Dame Fighting Irish","Arizona State Sun Devils","Wisconsin Badgers","Duke Blue Devils","Vanderbilt Commodores","Washington Huskies","Texas Tech Red Raiders",],
                2012: ["Alabama Crimson Tide","Oregon Ducks","Ohio State Buckeyes","Notre Dame Fighting Irish","Georgia Bulldogs","Texas A&M Aggies","Stanford Cardinal","South Carolina Gamecocks","Florida Gators","Florida State Seminoles","Clemson Tigers","Kansas State Wildcats","Louisville Cardinals","LSU Tigers","Oklahoma Sooners","Northwestern Wildcats","Texas Longhorns","Oregon State Beavers","Vanderbilt Commodores","Michigan Wolverines","Nebraska Cornhuskers","Baylor Bears","Penn State Nittany Lions","Oklahoma State Cowboys","UCLA Bruins",],
                2011: ["Alabama Crimson Tide","LSU Tigers","Oklahoma State Cowboys","Oregon Ducks","Arkansas Razorbacks","USC Trojans","Stanford Cardinal","South Carolina Gamecocks","Wisconsin Badgers","Michigan State Spartans","Michigan Wolverines","Baylor Bears","TCU Horned Frogs","Kansas State Wildcats","Oklahoma Sooners","West Virginia Mountaineers","Georgia Bulldogs","Virginia Tech Hokies","Clemson Tigers","Florida State Seminoles","Nebraska Cornhuskers","Auburn Tigers","Missouri Tigers","Texas Longhorns","Rutgers Crimson Knights",],
                2010: ["Auburn Tigers","TCU Horned Frogs","Oregon Ducks","Stanford Cardinal","Ohio State Buckeyes","Oklahoma Sooners","Wisconsin Badgers","LSU Tigers","Alabama Crimson Tide","Arkansas Razorbacks","Oklahoma State Cowboys","Michigan State Spartans","Mississippi State Bulldogs","Virginia Tech Hokies","Florida State Seminoles","Missouri Tigers","Texas A&M Aggies","Nebraska Cornhuskers","South Carolina Gamecocks","Maryland Terrapins","North Carolina State Wolfpack","Utah Utes","West Virginia Mountaineers","Arizona Wildcats","Iowa Hawkeyes",],
                2009: ["Florida Gators","Texas Longhorns","Oklahoma Sooners","USC Trojans","Alabama Crimson Tide","Ohio State Buckeyes","Virginia Tech Hokies","Mississippi Rebels","Oklahoma State Cowboys","Penn State Nittany Lions","LSU Tigers","California Golden Bears","Georgia Bulldogs","Georgia Tech Yellow Jackets","Oregon Ducks","TCU Horned Frogs","Florida State Seminoles","Utah Utes","North Carolina Tar Heels","Iowa Hawkeyes","Notre Dame Fighting Irish","Nebraska Cornhuskers","Kansas Jayhawks","Texas Tech Red Raiders","Oregon State Beavers",],
                2008: ["Florida Gators","Utah Utes","USC Trojans","Texas Longhorns","Oklahoma Sooners","Alabama Crimson Tide","TCU Horned Frogs","Penn State Nittany Lions","Ohio State Buckeyes","Oregon Ducks","Texas Tech Red Raiders","Georgia Bulldogs","Mississippi Rebels","Virginia Tech Hokies","Oklahoma State Cowboys","Oregon State Beavers","Missouri Tigers","Iowa Hawkeyes","Florida State Seminoles","Georgia Tech Yellow Jackets","West Virginia Mountaineers","Michigan State Spartans","Northwestern Wildcats","Pittsburgh Panthers","Iowa Hawkeyes",],
                }
