# MoodleXlator
Introduction
-------------
This application is used to convert a quiz specified in a specific format of
text file, to MOODLE XML format.

Currently tested in python 2.7. Will not work in python3 as prints have a
different syntax. You are welcome to port  it


Usage
------
  python moodleXmlGen.py -i <inputFileName> -o <outputFileName> 

   If -o  option is not used, the output will  be to console.

A global debug flag in dPrint.py is by default set to 0, 
if you set it to 1, it will output debug information.

Cannot document what the debug info actually means, but you can
Send  it to me along with input file, it will help me fix problem


Supported Question Types
-------------------------
1. Short Answer
2. True/False.
3. Multi Choice

Also Marks/Feedback for each of these question types can be specified.
By default the Marks is taken as 1.

Key Constructs
--------------
A parser looks of the following constructs. (Plz don’t use these as a part
of description of question/answer/choices. Dunno what will happen)`

1. <shortanswer>  </shortanswer> to identify questions that are short answer
type. Only these constructs must be present in the line.
2. <truefalse>  </truefalse>f or truefalse type of questions
3. <multichoice> </multichoice> type of question
4. <essay>/</essay> for essay answer question
4.  Q>> keyword  To identify question.
5. C>>  keyword tTo identify  choice
6. F>>  keyword To identify feedback
7. Marks>>  keyword for marks (IDeally should  have been M, but ....)
8. D>>  key work for description. The use case is suppose you want to
describe a scenario, and then asks questions related to the description,
this key word is used. See the attached sampleQpaper.txt for its usage.

Seem the attached "sampleQpaper.txt to understand how to write the  txt file
that specifies your questions/answers/choices


Issues
-----------
You can sepcify  regular expression as answers. But have never been able to
make it to work in Moodle server. It interprets the RE literaly. There 
are articles which describes how RE is supposed to work, but was unable
have a success with it
