# dataframe_inference_examples
В данном репозитории содержатся примеры к докладу “dataframe inference”  
  
Доклад посвящен проблемам синхронизации develop и research ветвей кода.  
*Идея в следующем*:  
основная проблема - перенос стадий препроцессинга и фиче инжиниринг, поэтому максимально декомпозируем эти стадии на отдельные шаги, каждый шаг имплементируем в виде отдельного python-объекта типа transformer. Затем готовые трансформеры объединяем в одну стадию с помощью sklearn_pandas.DataFrameMapper.   
Благодаря декларативному описанию фич в DataFrameMapper мы можем просто копировать этот код в train-ветвь продакшн кода. А заниженный маппер через стерилизацию и десериализацию просто передаем в inference-ветвь продакшн кода.  

