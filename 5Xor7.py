'''
The maintenance man is tired of following the complicated rules
 enforced by the management. He will give you a clue about the 
 password if you help him solve his problem:

The maintenance man is responsible for delivering the internal 
mail to all employees. In the company, there are different 
buildings with different room numbering schemes. 
In the first building, room numbers must contain a digit 5 or 
a digit 7, but not both of them. For example 5, 17, 52, 55, 177 
are all valid room numbers, but 24, 157 or 7005 are not.

All rooms in the building are placed on one very long hallway. 
All valid room numbers are - of course - arranged in ascending 
order: 5, 7, 15 , 17 ...

The maintenance man needs to bring mail to the 1000th room in the hallway.
 What is the room number of this room?
'''

# Create a loop and check if the room number is valid. Don't stop until the 1000th room is found
room_number = 0
valid_room_count = 0

while valid_room_count < 1000:
    room_number += 1
    if '5' in str(room_number) and '7' not in str(room_number) or '7' in str(room_number) and '5' not in str(room_number):
        valid_room_count += 1
    
print(room_number)