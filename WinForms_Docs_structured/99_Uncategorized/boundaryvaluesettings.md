---
title: boundaryvaluesettings.md
original_path: WinForms_Docs/99_Uncategorized/boundaryvaluesettings.md
created_at: 2025-08-05
---






##### Boundary Value Settings {#boundary-value-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

The ProgressBarAdv during it\'s progressive operation indicates a minimum value and a maximum value for the process.

 

It provides the below properties to set the boundary values for the control and also the interval for the progression.

[] 


  ------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  ProgressBarAdv Property   Description
  Minimum                   Determines the lower bound of the range of the ProgressBarAdv.
  Maximum                   Determines the higher bound of the range of the ProgressBarAdv.
  Value                     The current value between the minimum and maximum values.
  Step                      Determines the amount to increment or decrement the value of the ProgressBarAdv when the Increment() or Decrement() method is called.
  ------------------------- ---------------------------------------------------------------------------------------------------------------------------------------


[] 

Create a ProgressBarAdv and set the below properties to see the changes.

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                              |
| []                                                                         |
|                                                                                                                              |
| [this][.progressBarAdv1.Maximum = 200;] |
|                                                                                                                              |
| [this][.progressBarAdv1.Minimum = 25;]  |
|                                                                                                                              |
| [this][.progressBarAdv1.Step = 50;]     |
|                                                                                                                              |
| [this][.progressBarAdv1.Value = 100;]   |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                        |
|                                                                                                                           |
| []                                                                      |
|                                                                                                                           |
| [Me][.progressBarAdv1.Maximum = 200] |
|                                                                                                                           |
| [Me][.progressBarAdv1.Minimum = 25]  |
|                                                                                                                           |
| [Me][.progressBarAdv1.Step = 50]     |
|                                                                                                                           |
| [Me][.progressBarAdv1.Value = 100]   |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

**[]** 

Figure 973: ProgressBarAdv with Boundary Values Set

**[]** 

The methods associated with the above properties are given below.

[] 


  ----------- ---------------------------------------------------------------
  Methods     Description
  Increment   Increments the Value property associated with the Step value.
  Decrement   Decrements the Value property associated with the Step value.
  ----------- ---------------------------------------------------------------


 

 

 

[]{#p717} 

[]{#related-topics}

