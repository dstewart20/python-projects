import requests
from bs4 import BeautifulSoup
import datetime as dt
cpi_page='this is a global variable'
def init():
    url = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'
    #Good way to manipulate the user agent for the get functions
    response = requests.get(url, headers ={'user-agent': 'cs'} )
    html = response.text
    file = open('pages/fed.html','w')
    file.write(html)
    print(html)
    file.close()
#init()
def download_CPI():
    url = 'https://www.investing.com/economic-calendar/cpi-733'
    response = requests.get(url, headers ={'user-agent': 'cs'} )
    html = response.text
    file = open('pages/cpi.html','w')
    file.write(html)
    file.close()



def get_fomc_calendar():
    file = open('pages/fed.html','r')
    data=file.read()
    soup = BeautifulSoup(data,'html.parser')
    #SOUP Syntax goes, the tag, then the second argument will specify the class with => class_=''
    """
    The goal here is to essentially isolate the fomc-meeting-row divs and get the dates of the 2024 meetings only!
    so I have to 
    1. navigate through the tree to find all divs that match that attr
    2. filter out the row children only
    3. convert the text from the tags that contain the month and date data to a date format and append to a dates list
    4. give these commands to a bot to create a list of events 
    """
    try:
        #get the first panel of fomc meetings
        meetings = soup.find('div', class_='panel panel-default')

        #get the rows of the meeting
        rows = meetings.find_all('div',class_="row")
        
        #get the tags that have the month + date only from each row
        dates_list=[]
        for row in rows:
            """Doing something a little special here.
            It takes special characters ('/','-') to slice the date ranges
            and return the first day of the fomc meeting not the full two days. 
            """
            month=row.contents[1].text
            month_index= month.find('/')
            if month_index !=-1:
                month=month[:month_index]
                if month == 'Apr':
                    month='April'
            
            date=row.contents[3].text
            date_index=date.find('-')
            if date_index !=-1:
                date=date[:date_index]
            else:
                print('index not found')
            date_string = f'{month} {date} {2024}'
            #convert the string into a date object
            dates_list.append(date_string)
        return dates_list
    except Exception as e:
        print('uh oh')
        print(e)
    #convert the dates_list into a date object

def get_next_meeting():
    '''
    Now i need to get the list of meeting dates
    Then get the NEXT meeting which is essentially the first item that returns true
    '''
    today= dt.datetime.today()
    calender=get_fomc_calendar()

    next_meeting= next(meeting for meeting in calender if dt.datetime.strptime(meeting,'%B %d %Y')>today)
    return next_meeting

def get_cpi_report():
    '''
    This function returns the Date, Actual, forecast, and previous data from the latest CPI Report.
    '''
    file= open('pages/cpi.html','r') #open and read the file
    page=file.read()
    file.close()
    soup = BeautifulSoup(page,'html.parser')
    try:
        '''
        This TryCatch gets the latest report tag from the CPI page.
        Then creates a dictionary with the labels as keys and 
        the data as values from the releaseInfo div
        '''
        report = soup.find('div',id='releaseInfo')
        print('--------LATEST REPORT------')
        data={}
        #since each span has a text and div in it the label is the key. and the text of the next element is the value.
        for x in range(1,len(report.contents)):
           data[report.contents[x].next_element]=report.contents[x].next_element.next_element.text
        
        return data
    except Exception as e:
        print(f'something went wrong:{e}')

def update_cpi_data(soup: BeautifulSoup):
    '''
    check to see if the data needs to be updated based on Latest Release.
    if true then call download_CPI and run get_cpi_data again,
    else return latest report
    '''
    try:
        '''
        This try catch gets the header row, and the first row from the 
        historic data table and makes it into a dictionary.
        It compare's the latest report data to the release data to check 
        if the cpi_data needs to be updated.
        '''
        event_table = soup.find('div',id='eventTabDiv_history_0')
        header_row=[th for th in event_table.thead.tr.stripped_strings]
        first_row=[td for td in event_table.tbody.tr.stripped_strings]
        event_dict=dict(zip(header_row,first_row))
        print(event_dict)
    #cpi_report_date= dt.datetime.strptime(latest['Latest Release'],'%b %d, %Y')
    #update_cpi= historic_data_latest_date.date() ==  cpi_report_date.date()
    except Exception as e:
        print(f"couldn't update data: {e}")