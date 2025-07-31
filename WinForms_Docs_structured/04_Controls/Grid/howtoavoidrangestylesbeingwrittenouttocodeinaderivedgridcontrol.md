---
title: howtoavoidrangestylesbeingwrittenouttocodeinaderivedgridcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtoavoidrangestylesbeingwrittenouttocodeinaderivedgridcontrol.md
created_at: 2025-07-03
---








  









### How to Avoid RangeStyles being Written out to Code in a Derived GridControl {#how-to-avoid-rangestyles-being-written-out-to-code-in-a-derived-gridcontrol style="tab-stops: 0pt"}

[] 

When a derived grid is dropped onto a form at design-time, the styles that are changed in the derived grid\'s constructor will be written out as code in the form. This serialization to code can be avoided by overriding the respective properties and by setting it to the DesignerSerializationVisibility.Hidden.

 

As an example the RangeStyles being serialized to code can be avoided by overriding the RangeStyles and setting it to the DesignerSerializationVisibility.Hidden.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [\[Browsable(][false][), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)\]]                                          |
|                                                                                                                                                                                                                                                                                                   |
| [public new][ GridRangeStyleCollection RangeStyles]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [{]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                   |
| [    ][get]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                   |
| [   {]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [       ][return][ ][base][.RangeStyles;] |
|                                                                                                                                                                                                                                                                                                   |
| [   }]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [   ][set]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                   |
| [   {]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [      ][base][.RangeStyles = value;]                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [   }]                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [}]                                                                                                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [\<Browsable(][False][), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)\> ]                       |
|                                                                                                                                                                                                                                                                                 |
| [Public Shadows Property][ RangeStyles() ][As][ GridRangeStyleCollection] |
|                                                                                                                                                                                                                                                                                 |
| [    Get]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| [           Return][ ][MyBase][.RangeStyles]                              |
|                                                                                                                                                                                                                                                                                 |
| [   ][ End Get]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [    ][Set]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [         ][MyBase][.RangeStyles = Value]                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [    ][End Set]                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| [End Property]                                                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p547} 

 

[]{#related-topics}

