---
title: usingbuilder68.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder68.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain how you can set the themes for the DatePicker control:

 

1.  [In the **view**, invoke the **DatePicker** helper with the control ID as the first argument and set the **AutoFormat()** with the desired theme as an argument.]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[ASPX\]]**                                                                                                                        |
|                                                                                                                                                                                |
| [\<%] [{Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                                |
| [                  \-\-\-\-\--]                                                                                                            |
|                                                                                                                                                                                |
| [                  .AutoFormat([MobSkins].Spinach)]                                                                |
|                                                                                                                                                                                |
| [                  \-\-\-\-\--]                                                                                                            |
|                                                                                                                                                                                |
| [                  .Render();]                                                                                                             |
|                                                                                                                                                                                |
| [}[%\>]]                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[View \[Razor\]]**                                                                                                                      |
|                                                                                                                                                                               |
| [@] [{ Html.MobSyncfusion().DatePicker([\"DatePicker\"])] |
|                                                                                                                                                                               |
| [                  \-\-\-\-\--]                                                                                                           |
|                                                                                                                                                                               |
| [                  .AutoFormat([MobSkins].Spinach)]                                                               |
|                                                                                                                                                                               |
| [                  \-\-\-\-\--]                                                                                                           |
|                                                                                                                                                                               |
| [                  .Render();]                                                                                                            |
|                                                                                                                                                                               |
| [}] []                                                                            |
|                                                                                                                                                                               |
| []                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

1.  [Build and run the application in an emulator. The output will be as follows:]

[            ] {border="0"} []

Figure 178 : Simple Mode with Spinach Theme

[] 

{border="0"} []

Figure 179: Android Mode with Spinach Theme

[]{#related-topics}

