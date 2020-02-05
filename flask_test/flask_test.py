from flask import Flask, json
import pandas as pd
from sklearn.externals import joblib 
from sklearn.neighbors import NearestNeighbors



def make_app():
    app = Flask(__name__)
    @app.route('/id/<int:post_id>')

    def home(post_id):
        songs100 = pd.read_csv('http://www.zernach.com/wp-content/uploads/2020/02/songs100.csv')
        model = joblib.load('./flask_test/nn100.joblib')
        track = songs100[songs100['track_index_num'] == post_id]
        track = track.drop(['artist_name', 'track_id', 'track_name', 'track_index_num', 'album_cover_url'], axis=1)
        preds = model.kneighbors(track) 
        # app = Flask(__name__)
        df = songs100[(songs100['track_index_num'] == preds[1][0][0]) | (songs100['track_index_num'] == preds[1][0][1]) | (songs100['track_index_num'] == preds[1][0][2]) | (songs100['track_index_num'] == preds[1][0][3]) | (songs100['track_index_num'] == preds[1][0][4])]
        dict_set = [{
        'track_index_num' : x[0],
        'track_id' : x[1],
        'track_name' : x[2],
        'artist_name' : x[3],
        'album_cover_url' : x[4]
        }
        for x in df[['track_index_num', 'track_id', 'track_name', 'artist_name', 'album_cover_url']].values]

        json_preds = json.dumps(dict_set)

        return json_preds
    return app





if __name__ == "__main__":
     app.run(debug=True, port = 8080)



# r = requests.get(url = URL, params = PARAMS) 