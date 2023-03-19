from app import db
from app.models.Groups import Groups
from app.models.Bills import Bills
from app.models.UserGroup import UserGroup
from app.models.User import User


db.create_all()

group1 = Groups("Trip to SF")
group2 = Groups("Trip to NY")

db.session.add_all([group1, group2])
db.session.commit()


bill1 = Bills(group1.id, "Bus Tickets", 25.5)
bill2 = Bills(group1.id, "Drinks", 47.8)
bill3 = Bills(group1.id, "Food", 102.25)
bill4 = Bills(group1.id, "Amusement Park", 40)
bill5 = Bills(group2.id, "Train Tickets", 45.5)
bill6 = Bills(group2.id, "Food and drinks", 85.75)

db.session.add_all([bill1, bill2, bill3, bill4, bill5, bill6])
db.session.commit()

user1 = User(
    email="aisvais@gmail.com",
    password="$2b$12$lvvIrO57SwMTmPcqRH71P.Z4obg4kzSPk3qNTMjm9t0xO.IMOzqgy",
)
db.session.add_all([user1])
db.session.commit()

user_group1 = UserGroup(group_id=group1.id, user_id=user1.id)

db.session.add_all([user_group1])
db.session.commit()
