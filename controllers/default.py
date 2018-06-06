
def signup():
    return dict()

def store():
    submitted_studentname = request.vars.studentname
    submitted_id = request.vars.id
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    results = db.users.insert(
      db_studentname = submitted_studentname,
      db_id = submitted_id,
      db_email= submitted_email,
      db_password= submitted_password,
     )

    if results:
        return "User Saved Successfully"
    else:
         return "An error Occured"


def seeUsers():
    users=db().select(db.users.ALL) 
    return dict(users=users)  


def login():
    return dict()


def authenticate():
    submitted_email = request.vars.email
    submitted_password = request.vars.password

    if db(db.users.db_email==submitted_email
              and db.users.db_password==submitted_password) .count()>0:
        return "User Logged in Successfully" 
    else:
        return "User Not Found.Please Sign Up"    
        

             