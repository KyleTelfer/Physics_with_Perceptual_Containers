## 1. Facility Workflow Skeleton Notation ##

*1.1 - Facility Name*
*1.2 - Facility General Concept Description *

## 2. Facility Components or Units ##

Each unit has a number and a name

## 3. Types of connections ##

Each unit connection type notated by number within parathesis between matching open and close dash pairs.  A dash open and a dash close.  A dash open or a double dash close.  A placeholder type will be by default 3..

## 4. Component or unit connections ##

Each unit connection notated by matching open and closing dashes.  To signal modular entry or exit points the modular input would signal with a dash followed by a question mark.  To end the current modular entry point close with a dash followed by a question mark.  No workflow can have a modular entry that is linked as an exit to a point before the entry.  This would need to have the earlier point notated within a workflow that has a linear flow and natural endpoint.  Said notation of workflow would bloat but that bloat is needed to consider degredation while all workflow must have a begginning and end. Each use of a modular input would link to a specific notation of what is being considered within the workflow thus act as a branch not a loop.
To signal exit from workflow a connection of dash question mark dash will exit workflow. Workflow notation has a max limit of unit combinations configurable while respecting limits set within any computational limits.
 
### Example Facility ###

1.1 Waste Facility
1.2 A community waste management Concept

2.1 Intake 
2.2 Submerged Shredder
2.3 Waste transport (light density - not processed by current unit2)
2.4 Waste transport (heavy density - processed by current unit2)
2.5 Liquid density medium management
2.6 Packing and shipping

3.1 Centripetal Seperation
3.2 Auger
3.3 Conveyor
3.4 Magnetic
3.5 Vaccuum
3.. Not defined as of yet, placeholder for future thought

*Workflow notation example*
2.1 -?
-? (3..) - 2.2 -? 
-? (3..) - 2.3 - (3..) - 2.6 -?-
-? (3..) - 2.4 - (3..) - 2.2 -?
-? (3..) - 2.4 - (3..) - 2.6 -?-
-? (3..) - 2.6 -?
-? (3..) - 2.6 -?-



