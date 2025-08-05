---
title: textformattingusingspanadv1.md
original_path: WinForms_Docs/99_Uncategorized/textformattingusingspanadv1.md
created_at: 2025-08-05
---






#### Text Formatting Using SpanAdv {#text-formatting-using-spanadv style="tab-stops: 0pt"}

As **Inline** will be the content property of **ParagraphAdv**, **SpanAdv** can be added only inside the **ParagraphAdv**. Every **ParagraphAdv** can keep *n* number of inlines inside it. It allows you to display the formatted text using advanced features like font size, font family, strikethrough, and baseline.

Properties

  ---------------- ------------------------------------------------------------------------ ---------------------- ---------------
  Property         Description                                                              Type                   Data Type
  Text             Contains the text information.                                           Dependency Property    String
  Baseline         Indicates whether the inline's text is subscript or superscript.         Dependency Property    Baseline
  FontFamily       Specifies the font family of the text.                                   Dependency Property    FontFamily
  FontSize         Specifies the size of the font.                                          Dependency Property.   Double
  Foreground       Designates the font color.                                               Dependency Property    Color
  HighlightColor   Designates the highlight color of the text.                              Dependency Property    Color
  Strikethrough    Shows whether the text has SingleStrikeThrough or DoubleStrikeThrough.   Dependency Property    StrikeThrough
  FontWeight       Indicates the font weight of the text.                                   Dependency Property    FontWeight
  Underline        Indicates whether the text should be underlined.                         Dependency Property    Underline
  ---------------- ------------------------------------------------------------------------ ---------------------- ---------------

 

More:





