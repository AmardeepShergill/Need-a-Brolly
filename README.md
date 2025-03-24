# Need-a-Brolly
A Python API app to confirm if you need a Umberella for the day

This will use the OpenWeatherMap API to retrive real-time weather forecase data and the send me a message on with the result. 

Key Feature
- Real-Time Weather Forecasting
  - Using the OpenWeatherMap API to fetch current weather forecast data
  - Parsed and analysed the JSON response to determine weather conditions for the next several hours.
- Automated Message to Social Media
  - Integrated with the Facebook API to message weather updates automatically.
  - Included icons indicating rain or sunshine for easy parsing of the message
- Efficient Data Handling
  -  Ensured sensitive information such as API keys are securely managed through environment variables.
  -  Utilised Python's datetime module to generate current date information for the posts.
