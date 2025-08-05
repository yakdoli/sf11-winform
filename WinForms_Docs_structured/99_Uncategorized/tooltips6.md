---
title: tooltips6.md
original_path: WinForms_Docs/99_Uncategorized/tooltips6.md
created_at: 2025-08-05
---








  









## ToolTips {#tooltips style="tab-stops: 0pt"}

 

ToolTips will be shown during mouse over on the shape in Maps control. ToolTips can be shown through the AttributesItemSource of the ShapeFileLayer. AttributesItemSource is the IEnumerable collection. AttributesDataMapping will be mapped with AttributesItemSource, to show the ToolTip for  Maps Silverlight.

The following Code Snippet will demonstrate how to create the ToolTips for Maps Silverlight.

 

{border="0"}

Figure 23: ToolTips

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                       |
|                                                                                                                                                                                        |
| [using][ System;]                                                       |
|                                                                                                                                                                                        |
| [using][ System.Collections.Generic;]                                   |
|                                                                                                                                                                                        |
| [using][ System.Linq;]                                                  |
|                                                                                                                                                                                        |
| [using][ System.Text;]                                                  |
|                                                                                                                                                                                        |
| [namespace][ ToolTipDemo]                                               |
|                                                                                                                                                                                        |
| [{]                                                                                                                                   |
|                                                                                                                                                                                        |
| [   [public] [class] [MapToolTips]]                                 |
|                                                                                                                                                                                        |
| [    {]                                                                                                                               |
|                                                                                                                                                                                        |
| [       [public] MapToolTips()]                                                                                  |
|                                                                                                                                                                                        |
| [       { }]                                                                                                                          |
|                                                                                                                                                                                        |
| [       [public] [string] NAME { [get]; [set]; }] |
|                                                                                                                                                                                        |
| [    }]                                                                                                                               |
|                                                                                                                                                                                        |
| [}]                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                                                   |
|                                                                                                                                                                                                       |
| [using][ System;]                                                                                                |
|                                                                                                                                                                                                       |
| [using][ System.Collections.Generic;]                                                                            |
|                                                                                                                                                                                                       |
| [using][ System.Linq;]                                                                                           |
|                                                                                                                                                                                                       |
| [using][ System.Text;]                                                                                           |
|                                                                                                                                                                                                       |
| [using][ System.Collections.ObjectModel;]                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [namespace][ ToolTipDemo]                                                                                        |
|                                                                                                                                                                                                       |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                       |
| [    [class] [MapToolTip] : [ObservableCollection]\<[MapToolTips]\>] |
|                                                                                                                                                                                                       |
| [    {]                                                                                                                                                           |
|                                                                                                                                                                                                       |
| [        [public] MapToolTip()]                                                                                                              |
|                                                                                                                                                                                                       |
| [        {]                                                                                                                                                       |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Essex\"] });]                               |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Berkshire\"] });]                           |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Franklin\"] });]                            |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Middlesex\"] });]                           |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Worcester\"] });]                           |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Hampshire\"] });]                           |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Suffolk\"] });]                             |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Plymouth\"] });]                            |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Norfolk\"] });]                             |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Briscol\"] });]                             |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Branstable\"] });]                          |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Dukes\"] });]                               |
|                                                                                                                                                                                                       |
| [            Add([new] [MapToolTips] { NAME = [\"Nantucket\"] });]                           |
|                                                                                                                                                                                                       |
| [           ]                                                                                                                                                     |
|                                                                                                                                                                                                       |
| [        }]                                                                                                                                                       |
|                                                                                                                                                                                                       |
| [    }]                                                                                                                                                           |
|                                                                                                                                                                                                       |
| [}]                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

         

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                                   |
|                                                                                                                                                                                       |
| [            this][.shapeControl.AttributesDataMapping = [\"NAME;\"];]   |
|                                                                                                                                                                                       |
| [            [this].shapeControl.AttributesItemsSource = [new] [MapToolTip]();] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Notes:**

To define multiple AttributesDataMapping elements, the elements can be separated by the semi colon (;). AttributesItemSource elements value and the property of the class, which is to be binded with AttributesItemSource should be same. For enabling the ToolTips with this method, ShowAttributesToolTip property must be set as true.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]][ ]                                                                         |
|                                                                                                                                                                             |
| [            this][.shapeControl.ShowAttributesToolTip = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

