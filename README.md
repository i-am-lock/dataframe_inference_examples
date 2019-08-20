# dataframe_inference_examples
full video: https://www.youtube.com/watch?v=haGvIsChF6k

Here are examples for report "dataframe inference". Theme of the report is fast synchronization of research and production code branchs.  
  
*Main idea*
The problem is necessity to synchronize preprocessing and feature engineering stages in research and production(both train and inference) code branchs and transfer stages code from jupyter to python scripts. So we decompose these stages on small steps. Each step should be implemented as python transformer. Then we can combine steps into one transformer with sklearn_pandas.DataFrameMapper.  
Due to declarative description of features we can easly transfer code from research to train production branch: just with copy. Then we can serialize mapper and deserialize it in production inference branch.   
  
  
  
В данном репозитории содержатся примеры к докладу “dataframe inference”  
  
Доклад посвящен проблемам синхронизации research и develop ветвей кода.  
*Идея в следующем*:  
основная проблема - дублирование кода стадий препроцессинга и герерации фич в ресерч ветви и в train и inference девелоп ветви,- поэтому максимально декомпозируем эти стадии на отдельные шаги, каждый шаг имплементируем в виде отдельного python-объекта типа transformer. Затем готовые трансформеры объединяем в одну стадию с помощью sklearn_pandas.DataFrameMapper.   
Благодаря декларативному описанию фич в DataFrameMapper мы можем просто копировать этот код в train-ветвь продакшн кода. А зафитенный маппер через серилизацию и десериализацию просто передаем в inference-ветвь продакшн кода.  

