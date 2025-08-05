---
title: marginsettings.md
original_path: WinForms_Docs/99_Uncategorized/marginsettings.md
created_at: 2025-08-05
---






##### Margin Settings {#margin-settings style="tab-stops: 0pt"}

[] 

The margin settings that are common to all the Layout Managers are discussed below.

 

The layout bounds will also be adjusted to include some margin space along the borders according to the values specified in the properties given below. The default values of these properties are set to \'Zero\'.

[] 


  -------------------------- --------------------------------------------------------------------------------------
  LayoutManager Properties   Description
  TopMargin                  Gets / sets the top margin between the client rectangle and the layout rectangle.
  HorzNearMargin             Gets / sets the left margin between the client rectangle and the layout rectangle.
  HorzFarMargin              Gets / sets the right margin between the client rectangle and the layout rectangle.
  BottonMargin               Gets / sets the bottom margin between the client rectangle and the layout rectangle.
  -------------------------- --------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [this][.borderLayout1.TopMargin = 20;]      |
|                                                                                                                                  |
| [this][.borderLayout1.HorzFarMargin = 20;]  |
|                                                                                                                                  |
| [this][.borderLayout1.HorzNearMargin = 20;] |
|                                                                                                                                  |
| [this][.borderLayout1.BottomMargin = 20;]   |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [Me][.borderLayout1.TopMargin = 20]      |
|                                                                                                                               |
| [Me][.borderLayout1.HorzFarMargin = 20]  |
|                                                                                                                               |
| [Me][.borderLayout1.HorzNearMargin = 20] |
|                                                                                                                               |
| [Me][.borderLayout1.BottomMargin = 20]   |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 654: Margins set for Layout Manager (BorderLayout)

[] 

**[]** 

See Also

[] 

[Configuring BorderLayout]{.UGHyperlink}[, ]{.UGHyperlink}[Configuring FlowLayout]{.UGHyperlink}[, ]{.UGHyperlink}[Configuring GridLayout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

