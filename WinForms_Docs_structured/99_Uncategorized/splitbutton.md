---
title: splitbutton.md
original_path: WinForms_Docs/99_Uncategorized/splitbutton.md
created_at: 2025-08-05
---






##### SplitButton {#splitbutton style="tab-stops: 0pt"}

[] 

Split Button in the Ribbon instance enables to display a menu when the split button is clicked. This also enables to perform multiple operations by using a button. The Split Button contains a drop arrow, when clicked on it; the menu related to the button is displayed.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][ribbon][:][SplitButton][ [Label][=\" Split1 \"] [Command][=\"sample:SampleCommands.CustomCommand\"] [SizeForm][=\"Small\"]  [HitTestArea][=\"ImageOnly\"]   [SmallIcon][=\"SampleImages/TextHighlight.png\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [\<][ribbon][:][SplitButton][ [Label][=\" Split2 \"] [Command][=\"sample:SampleCommands.CustomCommand\"] [SizeForm][=\"Small\"] [SmallIcon][=\"SampleImages/TextHighlight.png\"] [/\>]]                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                             |
|                                                                                                                            |
| []                                                                     |
|                                                                                                                            |
| [SplitButton splitbutton = [new] SplitButton();]  |
|                                                                                                                            |
| [splitbutton.Label = [\"Split 1\"];]            |
|                                                                                                                            |
| []                                                                     |
|                                                                                                                            |
| [SplitButton splitbutton 1= [new] SplitButton();] |
|                                                                                                                            |
| [splitbutton1.Label = [\"Split 2\"];]           |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 850: SplitButton

 

**In SplitButton, which is more preferable, RibbonButton or RibbonMenuItem?**

[] 

In SplitButton, RibbonButton is more preferable since it has \"Toggle\" and \"IsChecked\" options. RibbonMenuItem is more applicable for Application Menus.

 

[]{#p449} 

[]{#related-topics}

