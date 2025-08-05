---
title: wizardcontrolevents.md
original_path: WinForms_Docs/99_Uncategorized/wizardcontrolevents.md
created_at: 2025-08-05
---






##### Wizard Control Events {#wizard-control-events style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

The events available for Wizard control and the methods which raises these events are listed in the below tables.

[] 


  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------
  Wizard Control Events                                                                                                                                                                                                                            Description
  [[Back]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_Programmatically)[]               This event is handled when the Back button is clicked or when PreviousPage method is called.
  [[Next]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_Programmatically)[]                  This event is handled when the Next button is clicked or when NextPage method is called.
  Cancel                                                                                                                                                                                                                                           This event is handled before the Cancel button is clicked.
  Finish                                                                                                                                                                                                                                           This event is handled before the Finish button is clicked.
  Help                                                                                                                                                                                                                                             This event is handled before the Help button is clicked.
  [[BannerControlLocationChanging]](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_Cancel)[]   Handled when banner panel controls are laid out.
  BeforePageSelect                                                                                                                                                                                                                                 Handled when the selected page is about to change.
  BeforeBack                                                                                                                                                                                                                                       Handled before the back button is clicked.
  BeforeFinish                                                                                                                                                                                                                                     Handled before the finish button is clicked.
  BeforeNext                                                                                                                                                                                                                                       Handled before the Next button is clicked.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ----------------------------------------------------------------------------------------------


[] 


  ------------------------ ----------------------------
  Wizard Control Methods   Description
  PreviousPage             Selects the previous page.
  NextPage                 Selects the next page.
  ------------------------ ----------------------------


 

 

 

 

###### []{#p1064}3.13.1.5.1.1    BannerControlLocationChanging Event {#bannercontrollocationchanging-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

This event is discussed in[ ][[How to Cancel the AutoLayout of the Banner panel controls]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_Cancel)[.]{.UGHyperlink}[]

 

 

 

 

[]{#related-topics}

