---
title: usingbuilder27.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder27.md
created_at: 2025-08-05
---






##### Using Builder {#using-builder style="tab-stops: 0pt"}

To enable symbol palette customization through Builder.

1.   In the **view**, [invoke the **Diagram** helper with ]the[ **control ID** as the first argument.][ ]

[] 

+-----------------------------------------------------------------------+
| **[View]**       |
|                                                                       |
|     <%{                                                               |
|                                                                       |
|           Html.Syncfusion().Diagram("SymbolPalette").SymbolPalette(   |
|                                                                       |
|             gr => gr.Background("white")                              |
|                                                                       |
|                     .BorderColor("black")                             |
|                                                                       |
|                     .ItemMouseOverBorderColor("red")                  |
|                                                                       |
|                     .SymbolPaletteGroupBackground("black")            |
|                                                                       |
|                     .SymbolPaletteGroupBorderColor("black")           |
|                                                                       |
|                     .SymbolPaletteGroupForeground("white")            |
|                                                                       |
|                     .SymbolPaletteGroupHoverBackground("orange")      |
|                                                                       |
|                     .SymbolPaletteGroupHoverBorderColor("orange")     |
|                                                                       |
|                     .SymbolPaletteGroupHoverForeground("white"))      |
|                                                                       |
|               .DiagramMode(DiagramMode.Canvas)                        |
|                                                                       |
|               .Render();                                              |
|                                                                       |
|       }                                                               |
|                                                                       |
|     %>                                                                |
|                                                                       |
| []               |
+-----------------------------------------------------------------------+

 

2.   Build and run the application.

 

[]{#related-topics}

