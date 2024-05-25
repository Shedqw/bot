import sqlite3

class Database:
    def __init__(self ,db_file):
        self.connection =sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.connection.cursor()
    

    def user_exists(self , user_id):
        with self.connection:
            result =self.cursor.execute("SELECT * FROM `user`  WHERE `user_id`=?",(user_id,)).fetchall()
            return bool(len(result))
        
    def add_user(self,user_id , referrer_id=None):
            with self.connection:
                if referrer_id != None:
                    return self.cursor.execute("INSERT INTO `user`(user_id , referrer_id)VALUES(?,?)",(user_id,referrer_id ,))
                else:
                    return self.cursor.execute("INSERT INTO `user`(user_id )VALUES(?)",(user_id,))
    
    def count_referals(self , user_id):
         with self.connection:
              return self.cursor.execute("SELECT COUNT(`user_id`) as count FROM `user` WHERE `referrer_id`=?",(user_id,)).fetchone()[0]
         
    def add_wallet(self,user_id , message):
            with self.connection:
                return self.cursor.execute("UPDATE `user` SET (wallet_address) = ? WHERE `user_id`=?",(message,user_id, ))

    def get_wallet(self,user_id):
            with self.connection:
                return self.cursor.execute("SELECT wallet_address FROM `user` WHERE `user_id`=?",(user_id, )).fetchone()[0]

    
   