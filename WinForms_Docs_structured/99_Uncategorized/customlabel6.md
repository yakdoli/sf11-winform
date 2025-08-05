---
title: customlabel6.md
original_path: WinForms_Docs/99_Uncategorized/customlabel6.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Custom Label {#custom-label style="tab-stops: 0pt"}

 

This feature allows you to customize the label for the slider.

  -------------- --------------------------------------------- -------------------------- -------------------------- ----------------
  Name           Description                                   Type of property           Value it accepts           Dependency
  Custom Label   Used to customize the label.                  Action\<TickLabelAdder\>   Action\<TickLabelAdder\>   NA
  ShowLabel      Used to display the label for the tick mark   Bool                       True/false                 EnableTickMark
  -------------- --------------------------------------------- -------------------------- -------------------------- ----------------

 

Custom Label Sub-Properties

  ------------- -------------------------------------------------- ------------------ ------------------- ------------
  Name          Description                                        Type of property   Value it accepts    Dependency
  Text          Used to set the custom text for specific value.    String             Any String          NA
  Value         The Value used to set the custom text.             Int                0 to int MaxValue   NA
  ToolTipText   Used to set the ToolTip text for specific values   String             Any String          NA
  ------------- -------------------------------------------------- ------------------ ------------------- ------------

 

The following steps explain how to set the Custom Label for slider control through the builder:**

1.   In **View**, invoke the slider helper with the control ID as an argument followed by the **CustomLabel** method which contains the methods(**Text, Value and ToolTipText**)  to customize the slider label.

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                            |
| [\<%] [=] [Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                                                                            |
| [         .Value(20)]                                                                                                                                                                  |
|                                                                                                                                                                                                                            |
| [                 **.CustomLabel(lable =\>**]                                                                                                                                          |
|                                                                                                                                                                                                                            |
| **[                 {]**                                                                                                                                                               |
|                                                                                                                                                                                                                            |
| **[                     lable.Add().Text([\"0\"]).Value(0);]**                                                                                                 |
|                                                                                                                                                                                                                            |
| **[                     lable.Add().Text([\"II\"]).Value(20);]**                                                                                               |
|                                                                                                                                                                                                                            |
| **[                     lable.Add().Text([\"IV\"]).Value(40);]**                                                                                               |
|                                                                                                                                                                                                                            |
| **[                     lable.Add().Text([\"VI\"]).Value(60);]**                                                                                               |
|                                                                                                                                                                                                                            |
| **[                     lable.Add().Text([\"VIII\"]).Value(80);]**                                                                                             |
|                                                                                                                                                                                                                            |
| **[                     lable.Add().Text([\"X\"]).Value(100);]**                                                                                               |
|                                                                                                                                                                                                                            |
| **[                 })]**                                                                                                                                                              |
|                                                                                                                                                                                                                            |
| [                 .EnableTickMark([true])]                                                                                                                        |
|                                                                                                                                                                                                                            |
| [                 **.ShowLabel([true])**]                                                                                                                         |
|                                                                                                                                                                                                                            |
| [    [%\>]]                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                             |
|                                                                                                                                                                        |
| **[\[Razor\]]**                                                                                                                    |
|                                                                                                                                                                        |
| [\@{] [ Html.MobSyncfusion().Slider([\"slider\"])] |
|                                                                                                                                                                        |
| [.Value(20)]                                                                                                                       |
|                                                                                                                                                                        |
| [                 **.CustomLabel(lable =\>**]                                                                                      |
|                                                                                                                                                                        |
| **[                 {]**                                                                                                           |
|                                                                                                                                                                        |
| **[                     lable.Add().Text([\"0\"]).Value(0);]**                                             |
|                                                                                                                                                                        |
| **[                     lable.Add().Text([\"II\"]).Value(20);]**                                           |
|                                                                                                                                                                        |
| **[                     lable.Add().Text([\"IV\"]).Value(40);]**                                           |
|                                                                                                                                                                        |
| **[                     lable.Add().Text([\"VI\"]).Value(60);]**                                           |
|                                                                                                                                                                        |
| **[                     lable.Add().Text([\"VIII\"]).Value(80);]**                                         |
|                                                                                                                                                                        |
| **[                     lable.Add().Text([\"X\"]).Value(100);]**                                           |
|                                                                                                                                                                        |
| **[                 })]**                                                                                                          |
|                                                                                                                                                                        |
| [                 .EnableTickMark([true])]                                                                    |
|                                                                                                                                                                        |
| [                 **.ShowLabel([true])**]                                                                     |
|                                                                                                                                                                        |
| [    .Render();]                                                                                                                   |
|                                                                                                                                                                        |
| [    [}]]                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application in the emulator.

*[[ [] ]]{.underline}*  

[ {border="0"} ] []

*[[ [] ]]{.underline}*  

[]{#related-topics}

