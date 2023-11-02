import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)

ind = [0,0,1303460009,1735288618,1153400878,1668851054,1203352160,1082861746,2049380647,1612294989,0,1196509690,
       1202390893,1118648643,1463862718,0,761831397,1958898376,1644355420,0,
       1433174395,1349375141,1332512027,1310469611,1298983887,1200998361,1351307952,0,0,0,0,0,0,0]


db = firestore.client()

users_ref = db.collection('Evo1')
docs = users_ref.stream()

i = 1
print(ind[2])