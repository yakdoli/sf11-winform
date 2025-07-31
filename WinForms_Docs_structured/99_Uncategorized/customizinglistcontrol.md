---
title: customizinglistcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\customizinglistcontrol.md
created_at: 2025-07-03
---






#### Customizing List control {#customizing-list-control style="tab-stops: 0pt"}

[] 

The appearance Grid List control can be customized by customizing the background color, image, header background color etc. The following properties can be used for customization:

[] 

[·      ]**TransparentBackground**--This property can be used to set a transparent background for grid cells. If its value is set to true, no background color is displayed for the grid cells. If its value is set to false, the background is filled with the chosen color. The value is set to False by default. Refer BackColor property for setting the required background color.

[] 

The following code example illustrates setting of a transparent background for grid cells.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                      |
|                                                                                                                                                                     |
| **[]**                                                                                                            |
|                                                                                                                                                                     |
| [this][.gridListControl1.TransparentBackground = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                               |
|                                                                                                                                                                  |
| []                                                                                                              |
|                                                                                                                                                                  |
| [Me][.gridListControl1.TransparentBackground = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][428][: Transparent Background set for Grid List Control]*

[] 

[·      ]**DisplayVertLines/DisplayHorzLines**--This property can be used to specify the display of vertical/horizontal lines on the grid. This property when set to true ensures display of vertical/horizontal grid lines.

 

The following code example illustrates the usage of the properties to display grid lines.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                            |
|                                                                                                                                                                           |
| **[]**                                                                                                                  |
|                                                                                                                                                                           |
| [this][.gridListControl1.Properties.DisplayHorzLines = [true];] |
|                                                                                                                                                                           |
| [this][.gridListControl1.Properties.DisplayVertLines = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                     |
|                                                                                                                                                                        |
| []                                                                                                                    |
|                                                                                                                                                                        |
| [Me][.gridListControl1.Properties.DisplayHorzLines = [True]] |
|                                                                                                                                                                        |
| [Me][.gridListControl1.Properties.DisplayVertLines = [True]] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][429][: Horizontal Lines displayed for Grid List Control]****[]***

***[]*** 

{border="0"}

***[]*** 

*[Figure ][430][: Vertical Lines displayed for Grid List Control]*

[] 

[·      ]**Buttons3D**-This property can be used to specify the appearance of row and column headers. This property when set to true, renders a three dimensional header providing the header a raised look.

 

The following code example illustrates the usage of the property to render a 3D header.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                     |
|                                                                                                                                                                    |
| **[]**                                                                                                           |
|                                                                                                                                                                    |
| [this][.gridListControl1.Properties.Buttons3D = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                              |
|                                                                                                                                                                 |
| []                                                                                                             |
|                                                                                                                                                                 |
| [Me][.gridListControl1.Properties.Buttons3D = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

*[Figure ][431][: Row and Column Headers with 3D Buttons Appearance]*

[] 

[·      ]**GridLineColor**-This property allows the user to specify a color for grid lines. Its value can be set to the required color.

 

The following code example illustrates the usage of this property to render blue grid lines.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| **[]**                                                                                                                             |
|                                                                                                                                                                                      |
| [this][.gridListControl1.Grid.Properties.GridLineColor = [Color].Blue;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                               |
|                                                                                                                                                                                   |
| [Me][.gridListControl1.Grid.Properties.GridLineColor = [Color].Blue] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

*[Figure ][432][: Grid Line Color set to \"Blue\"]*

[] 

[·      ]**BackColor**-This property allows the user to specify a background color for the Grid List control. It is mandatory to set the TransparentBackground to false to set the background color.

 

The following code example illustrates the usage of this property to render Beige background color.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                    |
|                                                                                                                                                                   |
| **[]**                                                                                                          |
|                                                                                                                                                                   |
| [this][.gridListControl1.BackColor = [Color.]Beige;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                             |
|                                                                                                                                                                |
| []                                                                                                            |
|                                                                                                                                                                |
| [Me][.gridListControl1.BackColor = [Color.]Beige] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

*[Figure ][433][: Grid List control with Back Color set to \"Beige\"]*

[] 

[·      ]**HeaderBackColor**-This property allows the user to specify the background color of headers.

 

The following code example illustrates the usage of this property to render a red background for the headers.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                        |
|                                                                                                                                                                       |
| **[]**                                                                                                              |
|                                                                                                                                                                       |
| [this][.gridListControl1.HeaderBackColor = [Color].Red;] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                 |
|                                                                                                                                                                    |
| []                                                                                                                |
|                                                                                                                                                                    |
| [Me][.gridListControl1.HeaderBackColor = [Color].Red] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**HeaderTextColor**-This property allows the user to specify the header text color.

 

The following code example illustrates the usage of this property to render a blue header text color.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| **[]**                                                                                                               |
|                                                                                                                                                                        |
| [this][.gridListControl1.HeaderTextColor = [Color].Blue;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                   |
|                                                                                                                                                                      |
| []                                                                                                                  |
|                                                                                                                                                                      |
| [Me][.gridListControl1.HeaderTextColor = [Color].Blue;] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**BackgroundImage**--This property allows the user to specify the background image used for the control.

 

The following code example illustrates the usage of this property to set the required image as background of the control.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                     |
| []                                                                                                                                                                |
|                                                                                                                                                                                                                     |
| [this][.gridListControl1.BackgroundImage = [Image].FromFile([\"Colud.jpg\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                             |
|                                                                                                                                                                                                                |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                |
| [Me][.gridListControl1.BackgroundImage =[ Image.FromFile]([\"Colud.jpg\"])] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

*[Figure ][434][: Grid List control with Background Image Set]*

 

[]{#p524} 

 

[]{#related-topics}

