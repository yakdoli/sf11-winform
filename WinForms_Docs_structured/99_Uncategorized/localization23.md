---
title: localization23.md
original_path: WinForms_Docs/99_Uncategorized/localization23.md
created_at: 2025-08-05
---








  





### Localization {#localization style="tab-stops: 0pt"}

Localization is a key feature that targets its global usage. OlapDataManager can be set to the specific locale and the BI controls will render the localized string based on the culture set on the OlapDataManager.

OLAP Base allows overriding default format strings of OlapCube with the culture based format string. This can be done by setting "OverrideDefaultFormatStrings" property to true.

Use Case Scenarios

Localization helps the user to create an application that targets several cultures.[]

Properties

Table 7: Properties Table


  ------------------------------ ------------------------------------------------------------------------------------------------------- ------ ------------- -----------------
  Property                       Description                                                                                             Type   Data Type     Reference links
  Culture                        Gets or sets the current culture of the OlapDataManager                                                 CLR    CultureInfo   
  OverrideDefaultFormatStrings   Gets or sets a value indicating whether  to override default OlapCube\'s FormatStrings of Value cells   CLR    bool           
  ------------------------------ ------------------------------------------------------------------------------------------------------- ------ ------------- -----------------


[] 

Adding Localization to an Application

The culture can be set through OlapDataManager by using following code:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**[]                                                                                                      |
|                                                                                                                                                                                             |
| [var][ olapDataManager = [new] [OlapDataManager]();]      |
|                                                                                                                                                                                             |
| [olapDataManager.Culture = [new] System.Globalization.[CultureInfo]([\"fr-Fr\"]);] |
|                                                                                                                                                                                             |
| [olapDataManager.OverrideDefaultFormatStrings = [true];][]                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**** 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**[]                                                                                                     |
|                                                                                                                                                                                            |
| [Dim][ olapDataManager = [New ][OlapDataManager]()]      |
|                                                                                                                                                                                            |
| [olapDataManager.Culture = [New] System.Globalization.[CultureInfo]([\"fr-Fr\"])] |
|                                                                                                                                                                                            |
| [olapDataManager.OverrideDefaultFormatStrings = [True]][]                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

