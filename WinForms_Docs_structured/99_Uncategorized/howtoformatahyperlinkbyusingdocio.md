---
title: howtoformatahyperlinkbyusingdocio.md
original_path: WinForms_Docs/99_Uncategorized/howtoformatahyperlinkbyusingdocio.md
created_at: 2025-08-05
---








  









## How to format a Hyperlink by using DocIO? {#how-to-format-a-hyperlink-by-using-docio style="tab-stops: 0pt"}

 

Some details about the fields. Each field consists of the following.

 

[·      ]Field, which defines field properties (not formatting)

[·      ]FieldMark (FieldSeparator mark)

[·      ]Text of the Field (WTextTange)

[·      ]FieldMark (FieldEnd mark)

 

If you want to set formatting for the field text, you have to find **WTextRange(s)** between the field separator and field text to set the CharacterFormat for them.

 

The following code illustrates how to format the hyperlink text.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                                          |
| **[]**                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [doc.LastParagraph.AppendHyperlink([\"www.google.com\"], [\"google\"], [HyperlinkType].WebLink);] |
|                                                                                                                                                                                                          |
| [ [for] ([int] i = 0, cnt = doc.LastParagraph.Items.Count; i \< cnt; i++)]                                                 |
|                                                                                                                                                                                                          |
| [ {]                                                                                                                                                                 |
|                                                                                                                                                                                                          |
| [     [if] (doc.LastParagraph.Items\[i\] [is] [WTextRange])]                                          |
|                                                                                                                                                                                                          |
| [     {]                                                                                                                                                             |
|                                                                                                                                                                                                          |
| [         [WTextRange] text = doc.LastParagraph.Items\[i\] [as] [WTextRange];]                        |
|                                                                                                                                                                                                          |
| [         text.CharacterFormat.FontSize = 33f;]                                                                                                                      |
|                                                                                                                                                                                                          |
| [     }]                                                                                                                                                             |
|                                                                                                                                                                                                          |
| [ }]                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                           |
| [doc.LastParagraph.AppendHyperlink([\"www.google.com\"], [\"google\"], HyperlinkType.WebLink)]                                                                          |
|                                                                                                                                                                                                                                                           |
| [Dim][ i [As] [Integer] = 0, cnt [As] [Integer] = doc.LastParagraph.Items.Count] |
|                                                                                                                                                                                                                                                           |
| [While][ i \< cnt]                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [If][ [TypeOf] doc.LastParagraph.Items(i) [Is] WTextRange [Then]]                                     |
|                                                                                                                                                                                                                                                           |
| [     [Dim] text [As] WTextRange = [TryCast](doc.LastParagraph.Items(i), WTextRange)]                                                                  |
|                                                                                                                                                                                                                                                           |
| [     text.CharacterFormat.FontSize = 33.0F]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                           |
| [End][ [If]]                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [i += 1]                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                           |
| [End][ [While]]                                                                                                                                 |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note:  Following is the order in the paragraph.



1)  WField object

2)  Field separator

3)  Text to display

4)  Field end[]{#_How_to_format_1}


[]{#related-topics}

