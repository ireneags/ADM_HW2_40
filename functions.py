def dateparse(time_in_secs):
  return pd.to_datetime(time_in_secs, unit='s')
  
def reviews_interval(time_intervals):
  reviews = []
  for interval in time_intervals:
    initial_time, final_time = interval
    initial_time = pd.to_datetime(initial_time).time()
    final_time = pd.to_datetime(final_time).time()
    num_reviews = len(dfs[dfs['timestamp_created'].dt.time.apply(lambda x: x > initial_time and x < final_time)])
    reviews.append(num_reviews) 
    
  intervals = [(lambda x: str(x))(x) for x in time_intervals]
  plt.figure(figsize=(14,10))
  plt.xticks(rotation=90)
  plt.xlabel('Time Intervals')
  plt.ylabel('NUmber of Reviews')
  sns.barplot(x=intervals, y=reviews, edgecolor='none')
  return
  
def lang_function(dataset_name, langs_list):
  if(dataset_name == 'dfs'):
    return dfs[dfs['language'].isin(langs_list)]