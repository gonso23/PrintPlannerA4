# PrintPlannerA4
Python3 script that places pages of a planner onto an A4 sheet.

You can choose between one-sided or double-sided printing, with 3 or 6 pages per side respectively.
   one-sided: printPlannerA4.py <input.pdf>
double-sided: printPlannerA4_2p.py <input.pdf>

output file name input_p1.pdf / input_p2.pdf

To install dependencies: pip install -r requirements.txt
 
Additionally, this script automatically adds a punch hole margin for each page, making it easy to design your planner refill.


# Formats

As Output A4 landscape is used 297x210mm
297mm/3 -> 99mm incl. the punch hole margin ~7mm

Input page format is required to be smaller than 99 x 210 mm to fit without scaling.
The page format incl punch hole margin is maximum 92 x 210 mm

Some refill formats I meassures, pls. check before usage.
Mini Organisers 	67mm x 105mm
Pocket Organisers 	81mm x 120mm 
Personal Organisers 95mm x 171mm
Slim Organisers 	95mm x 171mm
Compact Organisers 	95mm x 171mm

But you are not fixed to this numbers - I found out my planner has a perfect fit with 180 x 95 mm. And so I so set my print page format to 180 x 88 mm. The examples do use 171 x 88mm.

# Workflow
1 meassure your refill-format needs in mm. 
2 page format for printing refill-format height x refill-format width - 7 mm
3 set page size in our application (e.g. Word, Excel, Outlook, Writer...) 
  Note: standard planner settings will not work as punch hole margin is not respected there.
4 Print or export your pages in pdf
5 execute the script
6 print the output Note: 2 sided printing with flip on short side
7 cut, punch and use

# Participation
Comments are welcome, take the code and make it better.
Contributors and pull requests, just send a note.

# Example
python printPlannerA4.py Linien.pdf 
python printPlannerA4_2p.py karro.pdf


[example](karro_p2.pdf)