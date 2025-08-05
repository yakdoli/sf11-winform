---
title: settingtitlebarbackgroundforchromelesswindow.md
original_path: WinForms_Docs/99_Uncategorized/settingtitlebarbackgroundforchromelesswindow.md
created_at: 2025-08-05
---






#### Setting Title Bar Background for ChromelessWindow {#setting-title-bar-background-for-chromelesswindow style="tab-stops: 0pt"}

ChromelessWindow enables the user to create custom TitleBars with custom backgrounds. **TitleBarBackground** property can be used to set the background for the TitleBar.

 

Here is the code snippet for setting the TitleBarBackground property.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\<][shared][:][ChromelessWindow][ x][:][Class][=\"TestChromeless.Window1\"] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [xmlns][=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"]                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [xmlns][:][x][=\"http://schemas.microsoft.com/winfx/2006/xaml\"]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [xmlns][:][shared][=\"clr-namespace:Syncfusion.Windows.Shared;assembly=Syncfusion.Shared.WPF\"]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Title][=\"ChromelessWindowTestSample\"][ [ Height][=\"300\"][ Width][=\"300\"][ shared][:][SkinStorage.VisualStyle][=\"Default\"]                 [TitleBarBackground][=\"Green\" \>]]                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [\</][ shared][:][ChromelessWindow][\>]                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                  |
| [SkinStorage][.SetVisualStyle([this], [\"Default\"]);]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                  |
| [this][.TitleBarBackground = [new] SolidColorBrush(([Color])[ColorConverter].ConvertFromString([\"Green\"]));] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The following screen shots illustrate the title bar background changes.

 

{border="0"}

Figure 132: Default TitleBarBackground

*[]* 

{border="0"}

Figure 133: TitleBarBackground = \"Green\"

 

[]{#p116} 

[]{#related-topics}

