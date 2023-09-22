from config import app,db
from models import DJ, Track, Set, Show, Set_Name
from flask import request, session as flask_session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import text
from sqlalchemy import event
from sqlalchemy import or_

@app.route('/')
def home(): 
    return {}

@app.route('/tracks', methods=["GET"])
def tracks():
    if(request.method=="GET"):
        all=Track.query.all()
        tracks=[]
        # print("successful query")
        for track in all:
            # print("trying to check track")
            # print(track.name)
            # print(track.artist)
            # print(track.id)
            # print(track.sets)
            # print("checked track")
            tracks.append(track.to_dict())
        return tracks
    
@app.route('/djs', methods=["GET"])
def djs():
    if(request.method=="GET"):
        all=DJ.query.all()
        djs=[]
        for dj in all:
            djs.append(dj.to_dict())
        return djs
    
@app.route('/set_names', methods=["GET"])
def set_names():
    if(request.method=="GET"):
        all=Set_Name.query.all()
        set_names=[]
        for set_name in all:
            set_names.append(set_name.to_dict())
        return set_names
    
@app.route('/shows', methods=["GET"])
def shows():
    if(request.method=="GET"):
        all=Show.query.all()
        shows=[]
        for show in all:
            shows.append(show.to_dict())
        return shows
    
@app.route('/sets', methods=["GET"])
def sets():
    if(request.method=="GET"):
        all=Set.query.all()
        sets=[]
        for set in all:
            sets.append(set.to_dict())
        return sets
    
@app.route('/submit', methods=["POST"])
def submit():
    if(request.method=="POST"):
        data = request.json
        dj = data['dj']
        show = data['show']
        set_name = data['set_name']
        tracks = data['track_ids']
        return_list = []
        for track in tracks:
            try:
                new_set = Set()
                setattr(new_set, "dj_id", dj)
                setattr(new_set, "show_id", show)
                setattr(new_set, "set_name_id", set_name)
                setattr(new_set, "track_id", track)
                db.session.add(new_set)
                db.session.commit()
                return_list.append(new_set.to_dict())
            except(IntegrityError, ValueError) as ie:
                return {"error":ie.args},422
        return {"success":"Transaction completed successfully"},201

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    all = DJ.query.all()
    djs_converted = []
    correctUser = 0
    for dj in all:
        djs_converted.append(dj.to_dict())
    for dj in djs_converted:
        if dj['username'] == data['username']:
            correctUser = dj['id']
            return {"user": correctUser}
        else:
            pass
    return {"user": 0}
    
@app.route('/addtrack', methods=["POST"])
def addtrack():
    # if (request.method=="POST"):
        data = request.json
        sets = Set.query.all()
        sets_converted = []
        for set in sets:
            sets_converted.append(set.to_dict())
        tracks = Track.query.all()
        tracks_converted = []
        for track in tracks:
            tracks_converted.append(track.to_dict())
        dj = data['dj']
        show = data['show']
        set_name = data['set_name']
        track_list = data['track_list']
        return_list = []
        to_add_tracks = []
        for track in track_list:
            if track['add_to'] == 1:
                print("adding track to to_add_tracks")
                print(track)
                to_add_tracks.append(track)
        # for index, track in enumerate(track_list):
        #     for song in tracks_converted:
        #         if track['name'] == song['name'] and track['artist'] == song['artist']:
        #             print(track['name'])
        #             to_add_tracks.remove(track)
        #             continue
        #         else:
        #             pass
        print("made it past trimming ")
        for track in track_list:
            print("checking each track")
            print(track['name'])
            print(track['delete_flag'])
            if track['delete_flag'] == 1:
                for song in tracks_converted:
                    # print("checking song name and artist and id")
                    # print(song['name'])
                    # print(song['artist'])
                    # print(song['id'])
                    # print("checking track name and artist and id")
                    # print(track['name'])
                    # print(track['artist'])
                    # print(track['id'])
                    if song['name'] == track['name'] and song['artist'] == track['artist']:
                        print("found matching song in track list and database")
                        print("set_name_id here")
                        print(set_name)
                        for index, set in enumerate(sets_converted):
                            print("checking for matching track id and set_name_id in sets")
                            print(set['track_id'])
                            print(set['set_name_id'])
                            if song['id'] == set['track_id'] and set_name == set['set_name_id']:
                                print("makes it to commit")
                                print(sets[index])
                                db.session.delete(sets[index])
                                db.session.commit()
            if track['delete_flag'] == 0:
                for song in tracks_converted:
                    user_plays = 0
                    show_plays = 0
                    total_plays = 0
                    if song['name'] == track['name'] and song['artist'] == track['artist']:
                        match = False
                        for set in sets_converted:
                            if song['id'] == set['track_id'] and set_name == set['set_name_id'] and set['dj_id'] == dj:
                                for set in sets_converted:
                                    if song['id'] == set['track_id']:
                                        total_plays += 1
                                        if set['dj_id'] == dj:
                                            user_plays += 1
                                        if set['show_id'] == show:
                                            show_plays += 1
                                match = True
                            else:
                                pass
                        if match == False:
                            new_set = Set()
                            setattr(new_set, 'track_id', song['id'])
                            setattr(new_set, 'dj_id', dj)
                            setattr(new_set, 'set_name_id', set_name)
                            setattr(new_set, 'show_id', show)
                            for set in sets_converted:
                                if song['id'] == set['track_id']:
                                    total_plays += 1
                                    if set['dj_id'] == dj:
                                        user_plays += 1
                                    if set['show_id'] == show:
                                        show_plays += 1
                            db.session.add(new_set)
                            db.session.commit()
                        return_list.append({'name':track['name'], 'artist':track['artist'], 'user_plays':user_plays, 'show_plays':show_plays, 'total_plays':total_plays, 'delete_flag':0})
                    else:
                        pass
        for addition in to_add_tracks:
            new_track = Track()
            for attr in addition:
                setattr(new_track, attr, addition[attr])
            db.session.add(new_track)
            db.session.commit()
            added_track = Track.query.filter(Track.name == addition['name'] and Track.artist == addition['artist']).first()
            added_track_converted = added_track.to_dict()
            new_set = Set()
            setattr(new_set, 'track_id', added_track_converted['id'])
            setattr(new_set, 'dj_id', dj)
            setattr(new_set, 'set_name_id', set_name)
            setattr(new_set, 'show_id', show)
            db.session.add(new_set)
            db.session.commit()
            return_list.append({'name':track['name'], 'artist':track['artist'], 'user_plays': 1, 'show_plays': 1, 'total_plays': 1, 'delete_flag':0})
        #print("data being sent back")
        #print({'dj': dj, 'set_name': set_name, 'show': show, 'track_list': return_list})
        return {'dj': dj, 'set_name': set_name, 'show': show, 'track_list': return_list}
    # elif (request.method == "OPTIONS"):
    #     data = request.json
    #     return {data}


    
if __name__ == '__main__':
    app.run(port=5555, debug=True)