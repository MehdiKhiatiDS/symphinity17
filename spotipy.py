from flask import request
import pickle 
@app.route("/swords", methods=['POST'])
def swords():
    ''' a route, expects json object with 2 keys'''
    # receive input
    lines = request.get_json(force=True)
    # get data from json
    blessed_blade = lines['thunderfury'] # json keys that backend abides
    ashbringer = lines['corrupted'] 
    # validate input (optional)
    assert isinstance(blessed_blade, int)
    assert isinstance(ashbringer, str)
    # deserialize the pretrained model. 
    with open('model.pickle', 'rb') as mod: 
        model = pickle.load(mod)
    # predict
    output = model.predict([[blessed_blade, ashbringer]])
    # use a dictionary to format output for json
    send_back = {'prediction': output}
    send_back_dummy = {'dummy': 1} # minimal functionality for testing
    send_back_input = { # verify that input is working as expected
        'blessed_blade': blessed_blade, 
        'ashbringer': ashbringer
        }
    # give output to sender.
    return app.response_class(
        response=json.dumps(send_back),
        status=200,
        mimetype='application/json'