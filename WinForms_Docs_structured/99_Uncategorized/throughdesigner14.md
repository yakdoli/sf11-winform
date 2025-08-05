---
title: throughdesigner14.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner14.md
created_at: 2025-08-05
---






##### Through Designer {#through-designer style="tab-stops: 0pt"}

[] 

The Tabstrip can be customized to enhance the look and feel of the tab elements using Syncfusion Designer to add items, and ItemLook Editor to define custom ItemLooks that can be applied to different tabs.

[] 

Procedure for Designer

[] 

1.   Create a new Web application and drag the TabStrip control onto the page.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][cc1][:][TabStrip][ [ID][=\"TabStrip1\"] [runat][=\"server\"] [EnableCallbacks][=\"True\"] [AutoPostBack][=\"True\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [            ][\<][Items][\>]                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\<][cc1][:][TabStripItem][ [Text][=\"Support\"\>]]                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\<][cc1][:][TabStripItem][ [Text][=\"KnoweledgeBase\"\>]]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\</][cc1][:][TabStripItem][\>]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\<][cc1][:][TabStripItem][ [Text][=\"Forums\"\>]]                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\</][cc1][:][TabStripItem][\>]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\<][cc1][:][TabStripItem][ [Text][=\"Web from FAQs\"\>]]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\</][cc1][:][TabStripItem][\>]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\</][cc1][:][TabStripItem][\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\<][cc1][:][TabStripItem][ [Text][=\"Services\"\>]]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\<][cc1][:][TabStripItem][ [Text][=\"Consalting\"\>]]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\</][cc1][:][TabStripItem][\>]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\<][cc1][:][TabStripItem][ [Text][=\"Training\"\>]]                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                    ][\</][cc1][:][TabStripItem][\>]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                ][\</][cc1][:][TabStripItem][\>]                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [            ][\</][Items][\>]                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [        ][\</][cc1][:][TabStrip][\>]                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

99.  Right-click on the control and click the **Build** **Tabstrip** option to open **Syncfusion TabStrip Designer** dialog.

[] 

{border="0"}

**[]** 

Figure 290: Syncfusion Designer Window

[] 

100.   The Designer window allows you to add root and child tabs and define their state using the relative properties.

101.   To render styles for individual tab elements, click the **ItemLook Editor\...** button.

[] 

{border="0"}

Figure 291

[] 

102.   Then click either **OK** button to apply the style settings or **Cancel** button to cancel changes.

103.   Then in Designer dialog, click **Done** button to save the tabstrip items and its settings.

 

[]{#related-topics}

