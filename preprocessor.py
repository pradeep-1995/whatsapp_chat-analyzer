import re # Regular expression
import pandas as pd

def preprocess(data):
    # For 12hr format
    pattern_1 = '\d{1,2}\/\d{2,4}\/\d{2,4},\s\d{1,2}:\d{1,2}\s\w{1,2}\s-\s'
    # for 24 hr format
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'

    take = [pattern,pattern_1]

    for i in take:
        message = re.split(i,data)[1:]
        if len(message) != 0:
            dates = re.findall(i,data)
            df = pd.DataFrame({'user_message':message,"message_date":dates})
        if i == pattern:
            df['message_date'] = pd.to_datetime(df['message_date'], format='%m/%d/%y, %H:%M - ')
        else:
            df['message_date'] = pd.to_datetime(df['message_date'],format = '%m/%d/%y, %I:%M %p - ').dt.strftime("%H:%M")
            df['message_date'] = pd.to_datetime(df['message_date']) 
        break

    df.rename(columns={'message_date': 'date'}, inplace=True)
    
    # User Name from message
    users =[]
    messages = []
    
    for message in df['user_message']:
        entry = re.split('([\w\W]+?):\s',message) # priyanka1stgwc: Tomorrow no hons class\n
    
        if entry[1:] : # Username == priyanka1stgwc
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('Group notification')
            messages.append(entry[0])
    
    # User list
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'],inplace=True)

    # Year,month,day
    df['year'] = df['date'].dt.year
    df['month'] =  df["date"].dt.month_name()
    df['month_number'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['only_date'] = df['date'].dt.date

    # Hours,Minute
    df['hours'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    period = []
    for hour in df[['day_name', 'hours']]['hours']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period


    return df


