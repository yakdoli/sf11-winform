---
title: theicalcdatainterface.md
original_path: WinForms_Docs/03_Data_Binding/theicalcdatainterface.md
created_at: 2025-08-05
---






#### The ICalcData Interface {#the-icalcdata-interface style="tab-stops: 0pt"}

 

**ICalcData** has three methods and one event. This interface allows the **CalcEngine** class in Essential Calculate to communicate with arbitrary data sources that implement this interface.

 

[·      ]**GetValueRowCol**-Returns the data value of a specified row and column

[·      ]**SetValueRowCol**-Sets the data value of a specified row and column

[·      ]**WireParentObject**-A callback to the data object that occurs as the CalcEngine is being created. The purpose is to give the data object a chance to do any initialization steps it may need, such as subscribe to events to handle changes in data notifications.

[·      ]**ValueChanged**-An event that is raised whenever data changes. The ICalcData implementer raises this event when the data changes. The CalcEngine listens to this event and accordingly reacts to data changes. It is through this event that formulas are processed and dependencies are tracked by the CalcEngine.

[]{#p38} 

[]{#related-topics}

