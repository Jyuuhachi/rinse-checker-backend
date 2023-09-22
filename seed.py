from config import app, db
from models import DJ, Track, Set, Show, Set_Name

with app.app_context():
    
    db.drop_all()
    db.create_all()

    newshow = Show(name="Burning Hot")
    db.session.add(newshow)
    db.session.commit()

    newdj = DJ(name="DJSETUP", username="test", password="junk")
    db.session.add(newdj)
    db.session.commit()

    setname = Set_Name(name="Test Case")
    db.session.add(setname)
    db.session.commit()

    track = Track(name="Everyman (Joey Negro's Salsoul Strut)", artist="Double Exposure")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="test", artist="case")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Blue Eyes", artist="The Who")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    newdj = DJ(name="18STEPS", username="karellen", password="password")
    db.session.add(newdj)
    db.session.commit()

    setname = Set_Name(name="BURN V HOT VI")
    db.session.add(setname)
    db.session.commit()

    track = Track(name="Everyman (Joey Negro's Salsoul Strut)", artist="Double Exposure")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Just Like Muzik (Michele Chiavarini Instrumental Remix)", artist="Terrence Parker & Merachka")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="I Have A Dream (Miriko & Meex Extended Remix)", artist="Miriko & Meex")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Gimme Gimme", artist="Louis La Roche")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Once In A While", artist="Darius")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Artwater", artist="Cherokee & Kartell")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Baby Baby", artist="Noizu")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="The Vibe", artist="J Paul Getto")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Avenue", artist="Aran")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="New Love (Armand Van Helden Remix)", artist="Silk City & Ellie Gouldin feat. Diplo & Mark Ronson")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Wanting (with Josh Sahunta)", artist="kryptogram")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Do It Again", artist="Cherokee")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Mambo Jet", artist="Cherokee")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Disco Cop (Original Mix)", artist="Makito")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Feels Right feat. Durie", artist="Darius")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()

    track = Track(name="Let Me See You (Clap Your Hands) (Terrence Parker Re-Edit)", artist="Michele Chiavarini, Terrence Parker")
    db.session.add(track)
    db.session.commit()

    newset = Set(dj_id=newdj.id, track_id=track.id, set_name_id=setname.id, show_id=newshow.id)
    db.session.add(newset)
    db.session.commit()


    print("Successfully seeded database")

