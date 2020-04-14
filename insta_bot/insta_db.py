
from db_config import mysql

class InstaDB:
    def insert_user(self, username):
        try:
            sql = 'INSERT INTO user (username) VALUES ( %s )'
            data = (username, )
            cursor = mysql.cursor(dictionary=True)
            cursor.execute(sql, data)
            mysql.commit()
            return cursor.lastrowid
        except Exception as e:
            print(e)
        finally:
            cursor.close()
    
    def get_user(self, username):
        try:
            sql = 'SELECT * FROM user WHERE username=%s ORDER BY id DESC LIMIT 1'
            data = (username, )
            cursor = mysql.cursor(dictionary=True)
            cursor.execute(sql, data)
            return cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            cursor.close()

    def save_follows(self, user1, user2):
        try:
            sql = 'INSERT INTO connection (follower_id, followee_id) VALUES ( %s, %s )'
            data = (user1['id'], user2['id'])
            cursor = mysql.cursor()
            cursor.execute(sql, data)
            mysql.commit()
            return cursor.lastrowid
        except Exception as e:
            print(e)
        finally:
            cursor.close()

# instaDB = InstaDB()

# id1 = instaDB.insert_user("testuser1");
# id2 = instaDB.insert_user("testuser2");

# user1 = instaDB.get_user("testuser1")
# user2 = instaDB.get_user("testuser2")
# instaDB.save_follows(user1, user2)

# user = instaDB.get_user("testuser3")
# if not user:
#     print("user not found")
# else:
#     print(user)
