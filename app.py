import streamlit as st 
from streamlit_lottie import st_lottie
import pandas as pd
import preprocessor,helper
import matplotlib.pyplot as plt
import requests
import seaborn as sns

#col1,col2 = st.columns(2)
#with col1:
#    ''' ## Chat analysis
#    Here we find Overal stats, Monthly and Daily activity,
#    Most uses Word, Most Active User and Avialabel timming '''
#with col2:
# Lotti_file image
#    def load_lottieurl(url: str):
#        r = requests.get(url)
#        if r.status_code != 200:
#            return None
#        return r.json()
#    lottie_url2 = "https://assets9.lottiefiles.com/packages/lf20_QgETPxz4nq.json"

#    st_lottie(load_lottieurl(lottie_url2),height=200)


# side Bar
st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.read()#uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df_data = preprocessor.preprocess(data) # Assing the dataframe

    # Fetch Unique user
    user_list = df_data['user'].unique().tolist()
    user_list.remove('Group notification')
    
    user_list.insert(0,'Overall')

    selected_user = st.sidebar.selectbox('Show Analysis',user_list) 

    if st.sidebar.button("Show Analysis"):

        # Stats Area
        num_messages,words,num_link,num_media_msg = helper.fetch_stats(selected_user,df_data)

        st.subheader('**Top Statistics :**')
        col1, col2, col3, col4 = st.columns(4)

        # Total Message
        with col1:
            st.subheader('Total Message')
            st.subheader(num_messages)
        # Total words
        with col2:
            st.subheader('Total Words')
            st.subheader(words)
        # Total Link Shared
        with col3:
            st.subheader('Link Shared')
            st.subheader(num_link)
        # Total media shared
        with col4:
            st.subheader('Media Shared')
            st.subheader(num_media_msg)


        col1, col2 = st.columns(2)
        # Monthly Timeline
        with col1:
            mon_timeline = helper.monthly_timeline(selected_user,df_data)
            st.subheader('Monthly Timeline :')
            fig,ax = plt.subplots()
            ax.plot(mon_timeline['time'], mon_timeline['message'],color='green')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        # Daily timeline
        with col2:
            st.subheader('Daily Timeline')
            daily_timelines = helper.daily_timeline(selected_user,df_data)
            fig,ax = plt.subplots()
            ax.plot(daily_timelines['only_date'], daily_timelines['message'], color='black')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)   

        # Activity Map
        st.subheader("Activity Map :")
        col1,col2 = st.columns(2)
        # Most Busy day
        with col1:
            busy_day = helper.weekly_activity_map(selected_user,df_data)
            st.subheader('Most Busy Day')
            st.bar_chart(busy_day)
        # Most Busy Month
        with col2:
            busy_month = helper.month_activity_map(selected_user,df_data)
            st.subheader('Most Busy Month')
            #fig, ax = plt.subplots()
            #ax.bar(busy_month.index, busy_month.values,color='orange')
            #plt.xticks(rotation='vertical')
            #st.pyplot(fig)
            st.bar_chart(busy_month)
        
        # Activity Heat Map
        st.subheader("Weekly Activity Map")
        user_week_heatmap = helper.activity_heatmap(selected_user,df_data)
        fig,ax = plt.subplots()
        ax = sns.heatmap(user_week_heatmap)
        st.pyplot(fig)

        # finding the busiest users in the group(Group level)
        if selected_user == 'Overall':
            st.subheader('Most Busy Users')
            x,new_df = helper.most_busy_users(df_data)
            fig, ax = plt.subplots()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader('Top 5 Most active User')
                st.bar_chart(x)
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        
        col1, col2 = st.columns(2)
        with col1:
            # Word Cloud
            st.subheader("Word Cloud :")
            df_wc = helper.wordcloud(selected_user,df_data)
            fig,ax = plt.subplots()
            ax.imshow(df_wc)
            st.pyplot(fig)

        with col2:
            # most common words
            most_common_df = helper.most_common_words(selected_user,df_data)

            fig,ax = plt.subplots()
            ax.barh(most_common_df[0],most_common_df[1])
            plt.xticks(rotation='vertical')
            st.subheader('Most commmon words')
            st.pyplot(fig)

        # emoji analysis
        st.subheader("Emoji Analysis")
        emoji_df = helper.emoji_helper(selected_user,df_data)
        
        col1,col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax = plt.subplots()
            ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
            st.pyplot(fig)

        




