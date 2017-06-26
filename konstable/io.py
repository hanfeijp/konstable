"""
    Input-output functions

    - Save a Keras model in a Konstable compatible way.
"""

import os
import keras
from .utils.io import create_folder, timestamp_string

def konstablize(model, name=None, meta={}):
    """
        Saves a Keras model in a folder `name`
        :param model: A Keras Model instance that has been trained
        :param name: The name of the experiment
        :param meta: Meta information for the model
        :return:
    """
    # use model.history to obtain loss curves
    name = name + '-' + timestamp_string() if name else timestamp_string()
    path = os.path.abspath(os.path.join(os.getcwd(), name))
    print(path)
    create_folder(path)
    if str(type(model)) == "<class 'keras.models.Sequential'>":
        print('Converting sequential to model')
        history = model.model.history
    else:
        history = model.history
    print(model.to_json())
    print(history.history)