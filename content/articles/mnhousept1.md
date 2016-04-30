Title: What Happened to the State House in 2014? - pt1
Date: 2016-4-30 9:55
Category: Blog
Tags: Tutorial, MNHouse
Slug: mnhouse1
Author: Nick Conti
Summary: Part 1 in series examining MN State House 2014 election results.

# <em>Minnesota 2014 State House Results</em>


### Overview

This will be a multi-part post looking at what happened to the DFL candidates for State House in 2014.  It will be focused on the numbers rather than message or issues, mainly because we have more access to the numbers.  In later parts we will create more metrics (such as democratic base and DPI) and visualize the results with maps.  When I was working on this, I used a few Jupyter notebooks that are available [here](www.github.com/NickyThreeNames).  Fair warning, they are pretty disorganized but do show all of the steps (albeit out of order).

### 2014 Results
In this post we are going to gather data from the [Minnesota Secretary of State](www.sos.state.mn.us) and [Wikipedia](http://www.wikipedia.com) to get some election results

Let's start with results from the most recent general election, 2014.  The following Python code will initialize needed packages and put the results into a [Pandas](http://pandas.pydata.org/index.html "Pandas Documentation") dataframe made from the excel file.  
    
    :::python
    import pandas as pd
    import numpy as np
    url14 = 'http://www.sos.state.mn.us/Modules/ShowDocument.aspx?documentid=14542'
    e2014 = pd.read_excel(url14)
    e2014['Year'] = '2014'
    e2014.shape[0]
    
The last command gives us the number of rows in the data as a quick check that everything downloaded correctly.  We have also added a column for year and set it to 2014.  

The data returned is at precinct level, and is pretty messy.  First we'll rename the columns.
    
    :::python
    cols2014 = ['MNLEGDIST', 'TOTVOTING', 'USSENDFL', 'USSENTOTAL', 'USREPDFL', 'USREPTOTAL', 'MNLEGDFL', 'MNLEGTOTAL', 'MNGOVDFL', 'MNGOVTOTAL', 'MNSOSDFL', 'MNSOSTOTAL', 'MNAUDDFL', 'MNAUDTOTAL','MNAGDFL', 'MNAGTOTAL']
    e2014 = e2014[cols2014]
Next we will aggregate the data to the State House level and take a look at our data.
    
    :::python
    e14 = e2014.groupby('MNLEGDIST', as_index = False).sum()
    e14.head()
    
The Secretary of State only has raw vote totals but this not how we usually look at election results.  The following code creates  percentages for the DFL candidates as new columns in our dataframe. (We'll come back later and filter down to the just the State House candidates.)
   
    :::python
    e14['USSENPERC'] = e14['USSENDFL']/e14['USSENTOTAL']
    e14['USREPPERC'] = e14['USREPDFL']/e14['USREPTOTAL']
    e14['MNLEGPERC'] = e14['MNLEGDFL']/e14['MNLEGTOTAL']
    e14['MNGOVPERC'] = e14['MNGOVDFL']/e14['MNGOVTOTAL']
    e14['MNSOSPERC'] = e14['MNSOSDFL']/e14['MNSOSTOTAL']
    e14['MNAUDPERC'] = e14['MNAUDDFL']/e14['MNAUDTOTAL']
    e14['MNAGPERC'] = e14['MNAGDFL']/e14['MNAGTOTAL']

    stateHouseStats2016 = e14
### Candidate information

As part of our analysis, we will want to see which representatives are incumbents.  Luckily, Wikipedia has legislator data for the Minnesota House complete with a table of when they were elected [here](https://en.wikipedia.org/wiki/Minnesota_House_of_Representatives).  The following code loads our libraries and starts our webscrape using [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).
    
    :::python
    import matplotlib.pyplot as plt
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import re
    import numpy as np
    import string

    url = 'https://en.wikipedia.org/wiki/Minnesota_House_of_Representatives'
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    print(soup.prettify())

The last line in the code prints out the text from the website and can be used to figure out the rest of your scraper.  You can leave it out for this tutorial.  After reviewing the output, we are interested in the table that includes when they were first elected.  Let's select that table and initialize some Python lists to put our data into:
    
    :::python
    legis_tbl = soup.find('table', class_ = "wikitable sortable")
    print(legis_tbl)

The above code prints out all of the lines in the table(s) that have the class "wikitable sortable".  Let's select that table and initialize some Python lists to put our data into:
    
    :::python
    district = []
    name = []
    party = []
    elected = []

    
Our next step is to parse that table and append the data to the lists. There are a few legislators who have served non-consecutive terms and have multiple dates in their "Elected" column.  The sample code grabs the most recent date, which is fine for my purposes.  In our analysis, they will <em>not</em> be considered incumbents if their most recent win was in 2014.

    :::python
    for row in legis_tbl.findAll('tr'):
        cells = row.findAll('td')
        if len(cells) > 0:
            district.append(cells[0].find(text=True))
            name.append(cells[1].find(text=True))
            party.append(cells[2].find(text=True))
            elected.append(cells[4].find(text=True))
    
Next we will add them to a Pandas data frame with the following code.

    :::python
    legislator_info = pd.DataFrame(district,columns=['District'])
    legislator_info['District'] = district
    legislator_info['Name'] = name
    legislator_info['Party'] = party
    legislator_info['Elected'] = elected
    legislator_info.head()
    
Now that the data is in a data frame, we have some more cleanup to do.  First we'll remove extraneous punctuation and then convert the year column to an integer.

    :::python
    def remove_punctuation(s):
    s = ''.join([i for i in s if i not in frozenset(string.punctuation)])
    return s
    
    legislator_info['FirstElected'] = legislator_info['Elected'].apply(remove_punctuation)
    
While we are cleaning up data, let's add a column to show if they were DFL or Republican pickup (as opposed to a incumbent retaining their seat).  We will use two functions to accomplish this. The first one will see if the candidate is newly elected and the second one codes them based on party affiliation.  The second function assigns them a numeric code we can use later to visualize the data.

    :::python
    def newly_elected(x):
    if x['YearElected'] == 2014 or x['YearElected'] == 2015:
        return x['Party']
    else:
        return 'Incumbent'
        
    def new_elected_code(x):
    if x['Pickup'] == 'Republican':
        return 0
    elif x['Pickup'] == 'Incumbent':
        return 1
    else:
        return 2
        
    legislator_info['Pickup'] = legislator_info.apply(newly_elected, axis = 1)
    legislator_info['Pickup_code'] = legislator_info.apply(new_elected_code, axis = 1)
  
Let's trim it down to just columns we want to use later

    :::python
    to_keep = ['District', 'Name', 'Party', 'Pickup', 'Pickup_code', 'YearElected']
    legislators = legislator_info[to_keep]
    
Next we merge it with our data from earlier.  (If you are looking at the notebook in github, there are a couple of extra fields in the example that I will cover in a later blog post.)

    :::python
    stateHouseStats2016 = pd.merge(stateHouseStats, legislators, left_on = 'District', right_on = 'District', how = 'inner')

    
At this point we have our data for further analysis. If I was doing this as part of a campaign, I would either dump it to a SQL database or an Excel spreadsheet (depending on the campaign).  Since we will use this data to create some maps in a future post, I will write it out to a csv.

Thanks for reading the first tutorial!
