# Success-Prediction-Option2

This project employs a Keras LSTM (2-layer at the moment) to predict future KickStarter Project success.  The data come from WebRobots, and required a good bit of cleaning to get around memory constraints in Python and on a local machine.  The data can be found here (future hyperlink).  

The api server is storing the keras model

Flask backend server is storing and running a keras model, expects input from POST and returns a prediction in json

-- When using requirements.txt, it may be neccessary to install dash individually after venv creation. \('')/
																										 ||
																										 /\
