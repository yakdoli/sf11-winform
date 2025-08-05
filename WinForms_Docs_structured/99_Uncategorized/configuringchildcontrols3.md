---
title: configuringchildcontrols3.md
original_path: WinForms_Docs/99_Uncategorized/configuringchildcontrols3.md
created_at: 2025-08-05
---






##### Configuring Child Controls {#configuring-child-controls style="tab-stops: 0pt"}

[]{#p831} 

The following settings can be used to configure the Child controls of the GridLayout Manager.

[] 

ParticipateInLayout

[] 

To prevent a Child control from being laid out using the GridLayout Manager, the below given property can be used.

[] 


  ------------------------ -----------------------------------------------------------------------------------------------------------------
  Child Control Property   Description
  ParticipateInLayout      Specifies whether the Child control should participate in the GridLayout. The default value is set to \'True\'.
  ------------------------ -----------------------------------------------------------------------------------------------------------------


[] 

The methods associated with the above property are given below.

[] 


  ------------------------ -------------------------------------------------------------
  Methods                  Description
  GetParticipateInLayout   Indicates whether the component is in the layout list.
  SetParticipateInLayout   Adds or removes the specified control from the layout list.
  ------------------------ -------------------------------------------------------------


[] 

The following code can be used to add or remove the control from the GridLayout list programmatically.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.gridLayout1.SetParticipateInLayout([this].button1,[false]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [Me][.gridLayout1.SetParticipateInLayout([Me].button1,[False])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Configuring GridLayout]{.UGHyperlink}[, ]{.UGHyperlink}[Rearranging the Controls laid out by GridLayout]{.UGHyperlink}[, ]{.UGHyperlink}[[GridLayout - Configuring Child Controls]{.UGHyperlink}]()[]{.UGHyperlink}

[]{#related-topics}

