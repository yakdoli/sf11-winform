---
title: builtinskinstyles.md
original_path: WinForms_Docs/02_Concepts/builtinskinstyles.md
created_at: 2025-08-05
---








  









### Built-in Skin Styles {#built-in-skin-styles style="tab-stops: 0pt"}

The Grid control has some predefined skins which can be controlled through a single property setting.

 

Some of the available skins are as follows:

[·      ]Office 2007 Blue

[·      ]Office 2007 Black

[·      ]Office 2007 Silver

[·      ]Vista

[·      ]Almond

[·      ]Blend

[·      ]Blueberry

[·      ]Marble

[·      ]Midnight

[·      ]Monochorome

[·      ]Olive

[·      ]Sandune

[·      ]Turquoise

[·      ]VS2010

 

Properties

[] 

 


+-------------+----------------------------------------------------------------------------------------+------------------+------------------------+--------------------------------------------------+
| Property    | Description                                                                            | Type of property | Value it accepts       | Any other dependencies/sub-properties associated |
+-------------+----------------------------------------------------------------------------------------+------------------+------------------------+--------------------------------------------------+
| AutoFormat  | Used to apply auto format by using Skins enumeration. Default value is Office2007Blue. | Enum             | Skins.Office2007Blue   | NA                                               |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Office2007Black  |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Office2007Silver |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Vista            |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Almond           |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Blend            |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Blueberry        |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Marble           |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Midnight         |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Monochrome       |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Olive            |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Sandune          |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.Turquoise        |                                                  |
|             |                                                                                        |                  |                        |                                                  |
|             |                                                                                        |                  | Skins.VS2010           |                                                  |
+-------------+----------------------------------------------------------------------------------------+------------------+------------------------+--------------------------------------------------+


 

Methods

 


  -------------------- ------------ ------------------- ----------------------------
  Method               Parameters   Return type         Descriptions
  AutoFormat (Skins)   Skins        IGridBuilder\<T\>   Used to set skins to grid.
  -------------------- ------------ ------------------- ----------------------------


More:







