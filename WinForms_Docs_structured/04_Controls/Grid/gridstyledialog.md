---
title: gridstyledialog.md
original_path: WinForms_Docs/04_Controls/Grid/gridstyledialog.md
created_at: 2025-08-05
---








  









### Grid Style Dialog {#grid-style-dialog style="tab-stops: 0pt"}

The Grid Style Dialog is used to format the cells of the OlapGrid. Styling can be applied to the Column Header, Row Header, Summary cell, and value cell. The properties of the Header and Summary cells that can be formatted are as follows:

[·      ]Background Color

[·      ]Foreground Color

[·      ]Font Name

[·      ]Font Size

The properties of the Value cells that can be formatted are as follows:

[·      ]Font Name

[·      ]Font Style

[·      ]Font Color

[·      ]Font Size

[] 

{border="0"}

 

Figure 11: OlapGrid Style Dialog[]

 

The Grid line colour can also be changed by navigating to the Common tab and then selecting the Gridline color picker.

 

{border="0"}

 

Figure 12: Formatted OlapGrid[]

+----------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                           |
|                                                                                                                            |
| []                                                                                     |
|                                                                                                                            |
| [// To Display Style Dialog]                                             |
|                                                                                                                            |
| [this][.OlapGrid1.ShowStyleDialog();] |
|                                                                                                                            |
| []                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                        |
|                                                                                                                         |
| []                                                                                  |
|                                                                                                                         |
| [\' To Display Style Dialog][]    |
|                                                                                                                         |
| [Me][.OlapGrid1.ShowStyleDialog()] |
|                                                                                                                         |
| []                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

