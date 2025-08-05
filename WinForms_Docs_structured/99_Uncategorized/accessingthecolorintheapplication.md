---
title: accessingthecolorintheapplication.md
original_path: WinForms_Docs/99_Uncategorized/accessingthecolorintheapplication.md
created_at: 2025-08-05
---






##### Accessing the Color in the Application {#accessing-the-color-in-the-application style="tab-stops: 0pt"}

You can also access the selected color in the application. This helps you customize the theme of the application or select a color for doodle application and so on.

 

The following code illustrates how to access the color in the application:

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                                                                                                 |
|                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                              |
| [colorPicker][ color_picker = [new] [colorPicker]();]                                         |
|                                                                                                                                                                                                                                                              |
| [SolidBrushColor ][color= color_picker.color as [SolidBrushColor;]][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

                    

 

[]{#related-topics}

