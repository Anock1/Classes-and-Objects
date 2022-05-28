class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    
# Expected methods

# change_name method
    def change_name(self,name):
     self.name = name
# change_age method
    def change_age(self,age):
     self.age = age
# change_track method
    def add_track(self,track):
     self.tracks.append(track)
# get score method
    def get_score(self):
     print(self.score)

Bob = Student("Bob", 26, ["Fullstack","Front-End"],20.90)

# calling the methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
#checking that mycode works
#print(Bob.name)
#print(Bob.age)
#print(Bob.tracks)
#Bob.get_score()


