# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#This is from an article in Wikipedia
paragraph = "European higher education took place for hundreds of years in\
Christian cathedral schools or monastic schools (scholae monasticae), in \
which monks and nuns taught classes; evidence of these immediate forerunners \
of the later university at many places dates back to the 6th century.[12] The \
earliest universities were developed under the aegis of the Latin Church by \
papal bull as studia generalia and perhaps from cathedral schools. It is \
possible, however, that the development of cathedral schools into \
universities was quite rare, with the University of Paris being an exception.\
[13] Later they were also founded by Kings (University of Naples Federico II\
, Charles University in Prague, Jagiellonian University in Kraków) or \
municipal administrations (University of Cologne, University of Erfurt). \
In the early medieval period, most new universities were founded from \
pre-existing schools, usually when these schools were deemed to have become \
primarily sites of higher education. Many historians state that universities \
and cathedral schools were a continuation of the interest in learning promoted\
 by monasteries.[14] The first universities in Europe with a form of \
 corporate/guild structure were the University of Bologna (1088), the \
 University of Paris (c.1150, later associated with the Sorbonne), and the \
 University of Oxford (1167). The University of Bologna began as a law school \
 teaching the ius gentium or Roman law of peoples which was in demand across \
 Europe for those defending the right of incipient nations against empire and \
 church. Bologna's special claim to Alma Mater Studiorum[clarification \
 needed] is based on its autonomy, its awarding of degrees, and other \
 structural arrangements, making it the oldest continuously operating \
 institution[9] independent of kings, emperors or any kind of direct \
 religious authority.[15][16]"
paragraph = paragraph.lower()

i = 0
countuni = 0
countunis = 0

for i in range(len(paragraph)):
    if paragraph[i:i+10] == "university":
        countuni += 1
    elif paragraph[i:i+12] == "universities":
        countunis += 1
    i += 1

print("The number of university words counted is %s" % (countuni))
print("The number of universities words counted is %s" % (countunis))
