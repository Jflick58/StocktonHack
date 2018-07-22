import random
import pymysql
import json

def connect_to_db():
    cnx = pymysql.connect(user='Root',
                                  password='Welcome#10',
                                  host='hackathon-db.cmikvgfxob7c.us-west-2.rds.amazonaws.com',
                                  port=3306,
                                  database='hackathon',
                                  autocommit=True)
    cursor = cnx.cursor()

    return cursor





def create_user(user_json):

    cursor = connect_to_db()



    new_user = user_json
    user = new_user["User"]
    skills = new_user["Skills"]
    interests = new_user["Interests"]
    pic = new_user["profilepic"]

    userID = random.randint(100000,999999)

    cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s, %s,%s,%s,%s) ", (userID, user["Name"], user["email"], user["phoneNumber"], user["city"], user["state"], user["userType"], user["Bio"]))

    for skill in skills:
        cursor.execute("INSERT INTO userSkills values (%s,%s)", (userID, skill))

    for interest in interests:
        cursor.execute("INSERT INTO userInterest values (%s, %s)", (userID, interest))

    picID = random.randint(100000,999999)

    cursor.execute("INSERT INTO userProfilePicture values (%s, %s, %s)", (picID, pic, userID))

    return userID



def get_user(user_to_get):

    cursor = connect_to_db()
    cursor.execute("SELECT * from users where userID like %s", user_to_get["userID"])
    user_info = cursor.fetchone()
    print(user_info)

    cursor.execute('SELECT skill from userSkills where users_userID like %s', user_to_get["userID"])
    skills = cursor.fetchall()

    cursor.execute('SELECT interest from userInterest where users_userID like %s', user_to_get["userID"])
    interests = cursor.fetchall()

    cursor.execute('Select pictureLocation from userProfilePicture where users_userID like %s', user_to_get["userID"])
    pic = cursor.fetchone()

    if pic == "":
        pic = "https://s3-us-west-2.amazonaws.com/stkhacakthon/default-profile.png"




    user_profile = {
        "Name" : user_info[1],
        "email": user_info[2],
        "phoneNumber": user_info[3],
        "city": user_info[4],
        "state": user_info[5],
        "userType": user_info[6],
        "Bio": user_info[7]
    }

    user = {
        "userID": user_to_get["userID"],
        "user_profile" : user_profile,
        "Skills" : skills,
        "Interests" : interests,
        "ProfilePic" : str(pic)

    }

    return  user





if __name__ == "__main__":
    user = {
               "Name": "Test",
               "email": "test@test.com",
               "phoneNumber": "5555555555",
               "city": "Stockton",
               "state": "CA",
               "userType": "2",
               "Bio": "Cool dude",
           }

    create_user(user)

    #recrods()



