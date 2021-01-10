import sqlite3

class Comment():
    def __init__(self,StudentID,Time,Content):
        self.__StudentID = StudentID
        self.__Time = Time
        self.__Content = Content
        self.__DbName = './Group7_database'

    def postComment(self):
        '''write to DB'''
        conn = sqlite3.connect(self.__DbName)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comment WHERE StudentID = "+str(self.__StudentID))
        rows = cur.fetchall()
        if rows is None or len(rows) == 0:
            cur.execute("INSERT INTO Comment VALUES(?,?,?)", (self.__StudentID, self.__Time, self.__Content ))
            conn.commit()
        else:
            cur.execute("UPDATE Comment SET Time = "+str(self.__Time) +", Content = "+self.__Content+" WHERE StudentID = "+str(self.__StudentID))
            conn.commit()

        conn.close()
        return True

    def deleteOwnedComment(self):
        conn = sqlite3.connect(self.__DbName)
        cur = conn.cursor()
        cur.execute("SELECT * FROM Comment WHERE StudentID = " + str(self.__StudentID))
        rows = cur.fetchall()
        if rows is None or len(rows) == 0:
            pass
        else:
            sqlstr = "DELETE FROM Comment WHERE StudentID = "+str(self.__StudentID)
            cur.execute(sqlstr)
            conn.commit()

        conn.close()
        return True


if __name__ =='__main__':
    comm = Comment(10,20210111,'666')
    '''test_post_comment'''
    comm.postComment()
    comm.viewDB()

    print('=================')

    '''test_delete_owned_comment'''
    comm.deleteOwnedComment()
    comm.viewDB()




