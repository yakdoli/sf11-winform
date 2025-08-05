---
title: buttonwithmenuitems.md
original_path: WinForms_Docs/99_Uncategorized/buttonwithmenuitems.md
created_at: 2025-08-05
---






##### Button with menu items {#button-with-menu-items style="tab-stops: 0pt"}

The button can be rendered with sub-menu items. The following code snippets will help you to do so.

 


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[ASPX\]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\<][syncfusion][:][ButtonAdv][ [ID][=\"Button1\"] [ImageUrl][=\"Img/Save16.png\"] [runat][=\"server\"] [CustomClass][=\"buttonback\" ][Text][=\"Save the text\"] [DisplayType][=\"ImageBeforeText\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [  \<][Items][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [     \<][syncfusion][:][ButtonAdvItem][ [Text][=\"SaveAs\"] [ImageUrl][=\"Img/Save16.png\"] [/\>]]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [     [\<][syncfusion][:][ButtonAdvItem] [Text][=\"Open\"] [ImageUrl][=\"Img/Open.png\"] [/\>]]                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [  [\</][Items][\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [\</][syncfusion][:][ButtonAdv][\>][]                                                                                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                              |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [        [ButtonAdv] ButtonAdvance = [new] [ButtonAdv]();]       |
|                                                                                                                                                                           |
| [        ButtonAdvance.ID = [\"Button2\"];]                                                                   |
|                                                                                                                                                                           |
| [        ButtonAdvance.ImageUrl = [\"Img/Save16.png\"];]                                                      |
|                                                                                                                                                                           |
| [        ButtonAdvance.CustomClass = [\"buttonback\"];]                                                       |
|                                                                                                                                                                           |
| [        ButtonAdvance.DisplayType = Syncfusion.Web.UI.WebControls.Shared.[DisplayType].ImageBeforeText;]     |
|                                                                                                                                                                           |
| [        ButtonAdvance.Text = [\"Save\"];]                                                                    |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [        [ButtonAdvItem] ButtonItem = [new] [ButtonAdvItem]();]  |
|                                                                                                                                                                           |
| [        ButtonItem.Text = [\"Save As\"];]                                                                    |
|                                                                                                                                                                           |
| [        ButtonItem.ImageUrl = [\"Img/Save16.png\"];]                                                         |
|                                                                                                                                                                           |
| [        ButtonAdvance.Items.Add(ButtonItem);]                                                                                        |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [        [ButtonAdvItem] ButtonItem1 = [new] [ButtonAdvItem]();] |
|                                                                                                                                                                           |
| [        ButtonItem1.Text = [\"Open\"];]                                                                      |
|                                                                                                                                                                           |
| [        ButtonItem1.ImageUrl = [\"Img/Open.png\"];]                                                          |
|                                                                                                                                                                           |
| [        ButtonAdvance.Items.Add(ButtonItem1);]                                                                                       |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [        form1.Controls.Add(ButtonAdvance);][]                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

 

 


+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[VB\]]                                                                                                                                |
|                                                                                                                                                                             |
| [Dim][ ButtonAdvance [As] [New] ButtonAdv]   |
|                                                                                                                                                                             |
| [Dim][ ButtonItem [As] [New] ButtonAdvItem]  |
|                                                                                                                                                                             |
| [Dim][ ButtonItem1 [As] [New] ButtonAdvItem] |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [ButtonAdvance.ID = [\"Button2\"]]                                                                              |
|                                                                                                                                                                             |
| [ButtonAdvance.ImageUrl = [\"Img/Save16.png\"]]                                                                 |
|                                                                                                                                                                             |
| [ButtonAdvance.CustomClass = [\"buttonback\"]]                                                                  |
|                                                                                                                                                                             |
| [ButtonAdvance.Text = [\"Save\"]]                                                                               |
|                                                                                                                                                                             |
| [ButtonAdvance.DisplayType = Syncfusion.Web.UI.WebControls.Shared.DisplayType.ImageBeforeText]                                          |
|                                                                                                                                                                             |
| []                                                                                                                                      |
|                                                                                                                                                                             |
| [ButtonItem.Text = [\"Save As\"]]                                                                               |
|                                                                                                                                                                             |
| [ButtonItem.ImageUrl = [\"Img/Save16.png\"]]                                                                    |
|                                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                                             |
| [ButtonItem1.Text = [\"Open\"]]                                                                                 |
|                                                                                                                                                                             |
| [ButtonItem1.ImageUrl = [\"Img/Open.png\"]]                                                                     |
|                                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                                             |
| [ButtonAdvance.Items.Add(ButtonItem)]                                                                                                   |
|                                                                                                                                                                             |
| [ButtonAdvance.Items.Add(ButtonItem1)]                                                                                                  |
|                                                                                                                                                                             |
| [Me][.Controls.Add(ButtonAdvance)][]               |
|                                                                                                                                                                             |
| []                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

Build and run the application to see the following output generated.

 

{border="0"}

Figure 159: Button with sub-menu items

 

[]{#related-topics}

