---
title: themes3.md
original_path: WinForms_Docs/02_Concepts/themes3.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Themes {#themes style="tab-stops: 0pt"}

Different themes can be applied to OlapGrid using Syncfusion.Shared.Wpf assembly, which contains the basic data structures for applying a theme.

The following code snippet describes about applying theme to Grid.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[XAML\]**                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
| [\<!---Shared WPF namespace should be included\--\>]                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                           |
| [xmlns] [:] [sfshared] [=\"clr-namespace:Syncfusion.Windows.Shared;assembly=Syncfusion.Shared.WPF\"]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
| [\<] [ResourceDictionary] [\>]\                                                                                                                                                                                                                                         |
| [    ] [\<!\--Skin Manager for application\--\>]\                                                                                                                                                                                                                                           |
| [    ] [\<] [ResourceDictionary.MergedDictionaries] [\>]\                                                                                                                                                                                       |
| [        ] [\<] [ResourceDictionary] [ Source] [=\"/syncfusion.Shared.WPF;component/SkinManager/SkinManager.xaml\" /\>]\                                                                                                    |
| [    ] [\</] [ResourceDictionary.MergedDictionaries] [\>]\                                                                                                                                                                                      |
| [\</] [ResourceDictionary] [\>]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
| [\<!\-- Applying theme to OlapGrid\--\>]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                           |
| [\<] [syncfusion] [:] [OlapGrid] [ Name] [=\"OlapGrid1\"] [ sfshared] [:] [SkinStorage.VisualStyle] [=\"Blend\" /\>] |
|                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

-Or-

+-----------------------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                                            |
|                                                                                                                                   |
|                                                                                                                                   |
|                                                                                                                                   |
| [// Shared WPF namespace]                                                                                   |
|                                                                                                                                   |
| [using] Syncfusion.Windows.Shared;                                                                           |
|                                                                                                                                   |
|                                                                                                                                   |
|                                                                                                                                   |
| [// For applying blend theme]                                                                               |
|                                                                                                                                   |
| [SkinStorage].SetVisualStyle([this].OlapGrid1, [\"Blend\"]); |
|                                                                                                                                   |
|                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------+
| \[VB\]                                                                     |
|                                                                            |
|                                                                            |
|                                                                            |
| [\' Shared WPF namespace]                            |
|                                                                            |
| [Imports] Syncfusion.Windows.Shared                   |
|                                                                            |
|                                                                            |
|                                                                            |
| [\' For applying blend theme]                        |
|                                                                            |
| SkinStorage.SetVisualStyle([Me].OlapGrid1, \"Blend\") |
|                                                                            |
|                                                                            |
+----------------------------------------------------------------------------+

[] 

[] 

{border="0"}

 

Figure 32: OlapGrid in Blue Theme

[] 

{border="0"}

Figure 33: OlapGrid in Silver Theme

[] 

{border="0"}

Figure 34: OlapGrid in Blend Theme

 

{border="0"}

Figure 35: OlapGrid in Office 2007 Theme

{border="0"}

Figure 35: Metro Theme

 

[]{#related-topics}

