---
title: textformattingusinghyperlinkadv1.md
original_path: WinForms_Docs/99_Uncategorized/textformattingusinghyperlinkadv1.md
created_at: 2025-08-05
---






#### Text Formatting Using HyperlinkAdv {#text-formatting-using-hyperlinkadv style="tab-stops: 0pt"}

**HyperlinkAdv** can be kept only inside the **ParagraphAdv** since the content property of **ParagraphAdv** is **Inline**. It allows you to display the formatted text using advanced features like **NavigationUrl** and **TargetType**. It simply differs by these properties when compared to **SpanAdv**.

Properties


  Property         Description                                                                 Type                  Data Type
  ---------------- --------------------------------------------------------------------------- --------------------- ---------------------
  Text             Contains the text information.                                              Dependency Property   String
  Baseline         Indicates whether the inline text is subscript or superscript.              Dependency Property   Baseline
  NavigateURL      Holds the URL to which the page navigates to.                               Dependency Property   String
  TargetType       Indicates whether to open the link in the same window or in a new window.   Dependency Property   HyperlinkTargetType
  FontFamily       Specifies the font family of the text.                                      Dependency Property   FontFamily
  FontSize         Specifies the size of the font.                                             Dependency Property   Double
  Foreground       Designates the font color.                                                  Dependency Property   Color
  HighlightColor   Designates the highlight color of the text.                                 Dependency Property   Color
  Strikethrough    Shows whether the text has SingleStrikeThrough or DoubleStrikeThrough.      Dependency Property   StrikeThrough
  FontWeight       Indicates the font weight of the text.                                      Dependency Property   FontWeight
  Underline        Indicates whether the text should be underlined.                            Dependency Property   Underline


More:





