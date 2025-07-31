---
title: lengthandheightsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\lengthandheightsettings.md
created_at: 2025-07-03
---






##### Length and Height Settings {#length-and-height-settings style="tab-stops: 0pt"}

[] 

The[ ]properties that define the dimensions for the CommandBar are given below. During design time, the control\'s size can be changed by editing these property values.

[] 


  --------------------- -------------------------------------------------------------------------------------------------------
  CommandBar Property   Description
  MaxLength             Gets / sets the maximum linear dimension of the CommandBar.
  MinLength             Gets / sets the minimum linear dimension of the CommandBar.
  OccupyFullRow         Indicates whether the CommandBar should occupy the entire row when docked.
  MinHeight             Gets / sets the ideal lateral dimension of the CommandBar.
  IntegralHeight        Gets / sets the incremental step by which the CommandBar\'s lateral dimension increases when wrapped.
  --------------------- -------------------------------------------------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                         |
|                                                                                                                                                        |
| []                                                                                                   |
|                                                                                                                                                        |
| [this][.commandBar1.MaxLength = 201;]                             |
|                                                                                                                                                        |
| [this][.commandBar1.MinLength = 51;]                              |
|                                                                                                                                                        |
| [this][.commandBar1.OccupyFullRow = [true];] |
|                                                                                                                                                        |
| [this][.commandBar1.MinHeight = 27;]                              |
|                                                                                                                                                        |
| [this][.commandBar1.IntegralHeight = 2;]                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                  |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [Me][.commandBar1.MaxLength = 201]                             |
|                                                                                                                                                     |
| [Me][.commandBar1.MinLength = 51]                              |
|                                                                                                                                                     |
| [Me][.commandBar1.OccupyFullRow = [True]] |
|                                                                                                                                                     |
| [Me][.commandBar1.MinHeight = 27]                              |
|                                                                                                                                                     |
| [Me][.commandBar1.IntegralHeight = 2]                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 30: CommandBar with OccupyFullRow property set to \"True\"

[] 

The method associated with the above properties is given below.

[] 


  ------------------------- -----------------------------------------------------------------------------
  Method                    Description
  CalcCommandBarMaxLength   Calculates the CommandBar\'s maximum length for the specified client width.
  ------------------------- -----------------------------------------------------------------------------


[] 

See Also

[] 

[Interactive Features]{.UGHyperlink}[, ]{.UGHyperlink}[Themes And Visual Styles]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

