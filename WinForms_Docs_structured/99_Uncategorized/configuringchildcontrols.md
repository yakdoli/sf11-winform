---
title: configuringchildcontrols.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\configuringchildcontrols.md
created_at: 2025-07-03
---






##### Configuring Child Controls {#configuring-child-controls style="tab-stops: 0pt"}

[] 

The Child controls can be aligned to various positions (North, South, East, West and Center) using the property given below.

[] 


  -------------------------- --------------------------------------------------------
  Child Control Property     Description
  Position on borderLayout   Gets / sets the border position for a Child component.
  -------------------------- --------------------------------------------------------


[] 


{border="0"} Note: This property is added as an extended property in the properties window of the Child control added to the BorderLayout.


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                       |
|                                                                                                                                                                                                                                            |
| [this][.borderLayout1.SetPosition([this].btnNorth, Syncfusion.Windows.Forms.Tools.[BorderPosition].North);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [Me][.borderLayout1.SetPosition([Me].btnNorth, Syncfusion.Windows.Forms.Tools.BorderPosition.North)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 658: Setting the position of button1 on BorderLayout to \"North\"

[] 

{border="0"}

[] 

Figure 659: Layout of all Button Controls using BorderLayout

[] 


{border="0"} Note:[ ]BorderLayout allows only one control to be aligned along a particular layout position, unlike the .NET framework support.


[] 

See Also

[] 

[Configuring BorderLayout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

