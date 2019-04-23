"""
'Python-is-Easy' Homework #7 (Sets and Dictionaries)
DESCRIPTION: 
The main goal of this file created, is to get acquianted with Sets and Dictionaries in Python.  It is the seventh homework assigment in the
'Python is Easy' course, from Pirple.


Originally, the details below are attributes to a song, which have been created as variables in the file.

Refactor all variables of the song as a Dictionary dataset, then create a loop that prints the Keys and Values from the dictionary.

 
"""

# 1 - Refactored variables into dictionary Keys and Values. 

SongAttributesDict = {"Title":"In the End",
"Artist":"Linkin Park",
"Album":"Hybrid Theory",
"Genre":"Nu metal - Rap Rock",
"DurationInSeconds":216,
"DurationInMinutes":3.6,
"RecordedDate":2000,
"ReleaseDate":"October 9, 2001",
"Label":"Warner Bros.",
"WikipediaPage":"https://en.wikipedia.org/wiki/In_the_End"}

# 2 - Refactored print statements into single loop. 

for attribute in SongAttributesDict:
	print(attribute,":",SongAttributesDict[attribute])


############## 1 - Original variables ###################### 

# Title = "In the End"
# Artist = "Linkin Park"
# Album = "Hybrid Theory"
# Genre = "Nu metal - Rap Rock"
# DurationInSeconds = 216 
# DurationInMinutes = 3.6
# RecordedDate = 2000
# ReleaseDate = "October 9, 2001"
# Label = "Warner Bros." 
# WikipediaPage = "https://en.wikipedia.org/wiki/In_the_End"

############## 2 - Original print statements ###############

# print(Title)
# print(Artist)
# print(Album)
# print(Genre)
# print(DurationInSeconds)
# print(DurationInMinutes)
# print(RecordedDate)
# print(ReleaseDate)
# print(Label)
# print(WikipediaPage)


