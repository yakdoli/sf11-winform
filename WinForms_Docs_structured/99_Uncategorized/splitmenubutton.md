---
title: splitmenubutton.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\splitmenubutton.md
created_at: 2025-07-03
---






##### SplitMenuButton {#splitmenubutton style="tab-stops: 0pt"}

[] 

SplitMenuButton is similar to MenuButton. It is used to perform multiple operations. Events are raised, when main menubutton is clicked as well as when the sub item in the splitmenubutton is clicked. The following lines of code can be used to add a splitmenubutton control.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][ribbon][:][SplitMenuButton][ [Label][=\"Save As\"] [Icon][=\"/SampleImages/SaveAs32.png\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [   [\<][ribbon][:][ApplicationMenuGroup] [Header][=\"Header1\"] [IconBarEnabled][=\"True\"\>]]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [          [\<][ribbon][:][RibbonButton] [SizeForm] [=] [\"Small\"] [Label][=\"Item1\"]                                      ]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [          [SmallIcon][=\"SampleImages/Document32.png\"/\>]]                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [          [\<][ribbon][:][RibbonButton] [SizeForm] [=] [\"Small\"] [Label][=\"Item3\"] [SmallIcon][=\"SampleImages/Save32.png\"/\>]]                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [          [\<][ribbon][:][RibbonButton] [SizeForm] [=] [\"Small\"] [Label][=\"Item4\"] [SmallIcon][=\"SampleImages/Close32.png\"/\>]]                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [          [\<][ribbon][:][RibbonButton] [SizeForm] [=] [\"Small\"] [Label][=\"Item5\"]  [SmallIcon][=\"SampleImages/Print32.png\"/\>]]                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [          [\<][ribbon][:][RibbonButton] [SizeForm] [=] [\"Small\"] [Label][=\"Item6\"] [SmallIcon][=\"SampleImages/Open32.png\"/\>]]                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [   [\</][ribbon][:][ApplicationMenuGroup][\>]]                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][ribbon][:][SplitMenuButton][\>]                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 851: SplitMenuButton Added to the Ribbon Instance

 

[]{#p450} 

[]{#related-topics}

