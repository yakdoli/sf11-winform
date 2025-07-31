---
title: scrollsettings1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollsettings1.md
created_at: 2025-07-03
---






##### Scroll Settings {#scroll-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

This section discusses about the Scrolling Properties available for the TabControlAdv.

 

ScrollButton

 

TabControlAdv has the ability to add scrollbuttons on the TabPanel when the number of Tab items increase. These scrollbuttons allow the user to navigate through the tabpages in the front and back. For this, the ShowScroll property of the TabControl must be set.

 


  ------------------------ ---------------------------------------------
  TabControlAdv Property   Description
  ShowScroll               Specifies whether to show the scrollbutton.
  ------------------------ ---------------------------------------------


            

[• ]By default, scrollbuttons are set to 2D, 3D and Workbook tabstyles.

 

{border="0"}

 

Figure 1075: Scroll buttons displayed for the TabControlAdv**[]**

 

[• ]For all other styles, scrollbuttons are set to normal button-look.

 

{border="0"}

 

Figure 1076: Scroll buttons with Normal Button-Look**[]**

 

[• ]ScrollButtons can have a VS .NET - TabbedMDI scrollbutton-look, when the VSLikeScrollButton property is set to true.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| **[]**                                                                                                       |
|                                                                                                                                                                |
| [this][.tabControlAdv1.ShowScroll = [true];]         |
|                                                                                                                                                                |
| [this][.tabControlAdv1.VSLikeScrollButton = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| **[]**                                                                                                    |
|                                                                                                                                                             |
| [Me][.tabControlAdv1.ShowScroll = [True]]         |
|                                                                                                                                                             |
| [Me][.tabControlAdv1.VSLikeScrollButton = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

ScrollBars

 

ScrollBars can be set for the tabpages for which the AutoScroll property has to be set to true. The AutoScrollMinSize is set to a value, which if exceeded, enables the tabcontroladv to automatically add a scrollbar to the tabpage. Setting AutoScrollMargin, allows to maintain a minimum distance between the end margin of any control that is placed and the margin of the tabpage.

 

ScrollIncrement property is used to specify whether to scroll through tabs or pages.

 


  --------------------- ---------------------------------------------------------------------------------------------------------------
  TabPageAdv Property   Description
  AutoScroll            Specifies to add a scrollbar to the tabpage. Default value is False.
  AutoScrollMargin      Specifies the distance to be maintained between any control that is placed inside the page and the tabmargin.
  AutoScrollMinSize     Specifies the size of the tabpage, which if exceeded, would  enable scrollbars to be added.
  --------------------- ---------------------------------------------------------------------------------------------------------------


 

 

{border="0"}

Figure 1077: TabPage with ScrollBars and AutoScrollMargin Set**[]**

 

 Note:***[ ]***The TabControlAdv.BringSelectedTabToView() method is used to bring the selected tab to view, if scrolled out of view.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                     |
|                                                                                                                                                                                                              |
| [this][.tabPageAdv1.AutoScroll = [true];]                                                          |
|                                                                                                                                                                                                              |
| [this][.tabPageAdv1.AutoScrollMargin = [new] System.Drawing.[Size](20, 20);]  |
|                                                                                                                                                                                                              |
| [this][.tabPageAdv1.AutoScrollMinSize = [new] System.Drawing.[Size](50, 50);] |
|                                                                                                                                                                                                              |
| [this][.tabControlAdv1.ScrollIncrement = Syncfusion.Windows.Forms.Tools.[ScrollIncrement].Page;]   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [Private][ [Me].tabPageAdv1.AutoScroll = [True]]                                                        |
|                                                                                                                                                                                                                                        |
| [Private][ [Me].tabPageAdv1.AutoScrollMargin = [New] System.Drawing.Size(20, 20)]                       |
|                                                                                                                                                                                                                                        |
| [Private][ [Me].tabPageAdv1.AutoScrollMinSize = [New] System.Drawing.Size(50, 50)]                      |
|                                                                                                                                                                                                                                        |
| [Private][ [Me].tabControlAdv1.ScrollIncrement = Syncfusion.Windows.Forms.Tools.[ScrollIncrement].Page] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

[[[]]]{.underline} 

 

 

[]{#related-topics}

