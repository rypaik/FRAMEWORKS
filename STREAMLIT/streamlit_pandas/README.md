
Streamlit_pandas
[Creating an Interactive Datetime Filter with Pandas and Streamlit](https://towardsdatascience.com/creating-an-interactive-datetime-filter-with-pandas-and-streamlit-156e1ea12e90)


Initially, we will invoke the Streamlit slider widget which is documented as follows.

    streamlit.slider(label, min_value, max_value, value, step)

    Parameters

    label (str or None) — A short label explaining to the user what this slider is for.

    min_value (a supported type or None) — The minimum permitted value. Defaults to 0 if the value is an int, 0.0 if a float, value — timedelta(days=14) if a date/datetime, time.min if a time

    max_value (a supported type or None) — The maximum permitted value. Defaults to 100 if the value is an int, 1.0 if a float, value + timedelta(days=14) if a date/datetime, time.max if a time

    value (a supported type or a tuple/list of supported types or None) — The value of the slider when it first renders. If a tuple/list of two values is passed here, then a range slider with those lower and upper bounds is rendered. For example, if set to (1, 10) the slider will have a selectable range between 1 and 10. Defaults to min_value.

    step (int/float/timedelta or None) — The stepping interval. Defaults to 1 if the value is an int, 0.01 if a float, timedelta(days=1) if a date/datetime, timedelta(minutes=15) if a time (or if max_value — min_value < 1 day)

Please note that our slider will return two values, i.e. the start datetime and end datetime values. Therefore we must declare the initial value of the slider using an array as:

`[0,len(df)-1]`

And we must equate the widget to two variables as shown below, i.e. the start and end datetime indices that will be used to filter the data frame:

`slider_1, slider_2 = st.slider('%s' % (message),0,len(df)-1,[0,len(df)-1],1)`

Subsequently, we need to remove any trailing decimal places from our start/end time column and add leading zeroes in case the time is less than a whole hour, i.e. 12:00AM quoted as 0, as shown below:

`while len(str(df.iloc[slider_1][1]).replace('.0','')) < 4:
    df.iloc[slider_1,1] = '0' + str(df.iloc[slider_1][1]).replace('.0','')
`

Then we need to append our date to time and parse our datetime in a format that is comprehensible by using the datetime.strptime binding in Python as shown below:

`start_date = datetime.datetime.strptime(str(df.iloc[slider_1][0]).replace('.0','') + str(df.iloc[slider_1][1]).replace('.0',''),'%Y%m%d%H%M%S')`


To display our selected datetimes we can use the strftime function to reformat the start/end as follows:

`start_date = start_date.strftime('%d %b %Y, %I:%M%p')`

In order to use other datetime formatting’s please refer to this article. Finally, we will display the selected datetimes and will apply the filtered indices to our dataset as shown below:

`st.info('Start: **%s** End: **%s**' % (start_date,end_date))
filtered_df = df.iloc[slider_1:slider_2+1][:].reset_index(drop=True)`