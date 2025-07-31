---
title: configuringcardlayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\configuringcardlayout.md
created_at: 2025-07-03
---






##### Configuring CardLayout     {#configuring-cardlayout style="tab-stops: 0pt"}

[] 

The configuration settings for the CardLayout have been discussed in this topic.

[] 

Card Names

[] 

By default, when a new Child control is added, the CardLayout will render a unique card name for it. This name can be modified by using the property given below.

[] 


  --------------------- ---------------------------------
  CardLayout Property   Description
  CardName              Specifies the name of the card.
  --------------------- ---------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [this][.cardLayout1.SetCardName([this].label1, [\"Card1\"]);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                           |
| [Me][.cardLayout1.SetCardName([Me].label1, [\"Card1\"])] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 661: Setting the Card Name

[] 

The methods associated with the above property are given below.

[] 


  ---------------------- ----------------------------------------------------------------------------------
  Method                 Description
  GetCardName            Returns the card name of a Child component.
  GetCardNames           Returns an array containing the card names as strings.
  GetComponentFromName   Returns an associated control given a card name.
  GetNewCardName         Generates a new unique name for the card that could be added to this CardLayout.
  SetCardName            Sets the card name for a Child component.
  ---------------------- ----------------------------------------------------------------------------------


[] 


{border="0"} Note: This property is added as an extended property in the properties window of the Child control added to the CardLayout.


[] 

Card Index

[] 

The index of the previous and next cards can be determined using the below given properties.

[] 


  ----------------------- ---------------------------------------------------------------------------------------------------
  CardLayout Properties   Description
  NextCardIndex           Returns the index of the next card that will be shown when the Next() method gets called.
  PreviousCardIndex       Returns the index of the previous card that will be shown when the Previous() method gets called.
  ----------------------- ---------------------------------------------------------------------------------------------------


[] 

Aspect Ratio

[] 

The aspect ratio can be set using the property given below.

 


  --------------------- -------------------------------------------------------------------------------------------
  CardLayout Property   Description
  MaintainAspectRatio   Indicates if the aspect ratio is to be maintained. The default value is set to \'False\'.
  --------------------- -------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                                |
|                                                                                                                                                                                                    |
| [this][.cardLayout1.SetMaintainAspectRatio([this].label1, [true]);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                               |
| []                                                                                                                                          |
|                                                                                                                                                                                               |
| [Me][.cardLayout1.SetMaintainAspectRatio([Me].label1, [True])] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The methods associated with the above property are given below.

[] 


  ------------------------ ----------------------------------------------------------------------------------------
  Method                   Description
  GetMaintainAspectRatio   Returns the value for maintaining aspect ratio based on the control\'s preferred size.
  SetMaintainAspectRatio   Sets the value for maintaining aspect ratio based on the control\'s preferred size.
  ------------------------ ----------------------------------------------------------------------------------------


[] 

See Also

[] 

[Card Layout - Configuring Child Controls]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

