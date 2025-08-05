---
title: tooltips7.md
original_path: WinForms_Docs/99_Uncategorized/tooltips7.md
created_at: 2025-08-05
---








  









## ToolTips {#tooltips style="tab-stops: 0pt"}

ToolTips will be shown when during mouse over on the shape in Maps control. ToolTips can be shown through the AttributesItemSource of the ShapeFileLayer. AttributesItemSource is the IEnumerable collection. AttributesDataMapping will be mapped with AttributesItemSource to show the ToolTip for the Maps WPF.

The following code snippet will demonstrate how to create the ToolTips for the Maps WPF.

{border="0"}

Figure 26: ToolTips

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][ ]**                                                                   |
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

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][ ]**                                                                                               |
|                                                                                                                                                                                                                    |
| [using][ System;]                                                                                   |
|                                                                                                                                                                                                                    |
| [using][ System.Collections.Generic;]                                                               |
|                                                                                                                                                                                                                    |
| [using][ System.Linq;]                                                                              |
|                                                                                                                                                                                                                    |
| [using][ System.Text;]                                                                              |
|                                                                                                                                                                                                                    |
| [using][ System.Collections.ObjectModel;]                                                           |
|                                                                                                                                                                                                                    |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                    |
| [namespace][ ToolTipDemo]                                                                           |
|                                                                                                                                                                                                                    |
| [{]                                                                                                                                                               |
|                                                                                                                                                                                                                    |
| [    [class] [MapToolTip] : [ObservableCollection]\<[MapToolTips]\>] |
|                                                                                                                                                                                                                    |
| [    {]                                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [        [public] MapToolTip()]                                                                                                              |
|                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                       |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Essex\"] });]                               |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Berkshire\"] });]                           |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Franklin\"] });]                            |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Middlesex\"] });]                           |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Worcester\"] });]                           |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Hampshire\"] });]                           |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Suffolk\"] });]                             |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Plymouth\"] });]                            |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Norfolk\"] });]                             |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Briscol\"] });]                             |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Branstable\"] });]                          |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Dukes\"] });]                               |
|                                                                                                                                                                                                                    |
| [            Add([new] [MapToolTips] { NAME = [\"Nantucket\"] });]                           |
|                                                                                                                                                                                                                    |
| [           ]                                                                                                                                                     |
|                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                       |
|                                                                                                                                                                                                                    |
| [    }]                                                                                                                                                           |
|                                                                                                                                                                                                                    |
| [}]                                                                                                                                                               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

         

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][ ]**                                                                                          |
|                                                                                                                                                                                                               |
| [            this][.shapeControl.AttributesDataMapping = [\"NAME;\"];] |
|                                                                                                                                                                                                               |
| [            [this].shapeControl.AttributesItemsSource = [new] [MapToolTip]();]            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Note:

To define multiple AttributesDataMapping elements, the elements can be separated by a semi- colon. AttributesItemSource elements value and the property of the class which is to be binded with AttributesItemSource should be the same. To enable the ToolTips with this method ShowAttributesToolTip property must be set as true.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][ ]**                                                                                  |
|                                                                                                                                                                                                       |
| [            this][.shapeControl.ShowAttributesToolTip = [true];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Alternative way to Show the ToolTip

Load a shape file from the location. If a .dbf file with same name is available in the same location ToolTip will be displayed automatically If a shape file is loaded with Uri property, add a .dbf file with the same name of the shape file in the same location, and change its property "Copy to Directory" as Always Copy. Then the ToolTip for the corresponding shape file will be displayed automatically.

 

 

[]{#related-topics}

