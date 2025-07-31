---
title: textbox2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textbox2.md
created_at: 2025-07-03
---






##### TextBox {#textbox style="tab-stops: 0pt"}

 

**WTextBox** class represents a text box in the Word document.

 

TextBox is a shape. DocIO text box (WTextBox) has two properties which are as follows.

 

[·      ]**TextBoxFormat** -- defines formatting of the text box (position, alignment, border colors, and so on)

[·      ]**TextBoxBody** -- defines the text for the text box

 

**TextBoxFormat** property returns the object of the WTextBoxFormat type. For more details, see [WTextBoxFormat]. TextBoxBody property returns the object of the WTextBody type.

 

You can use the **AppendTextBox** function of the WParagraph class to append a text box to a paragraph.

 

Class Hierarchy

 

ParagraphItem

            \|

            WTextBox

 

Public Constructor

 


  ----------------------------------- -----------------------------------------------------
  Name                                Description
  WTextBox.WTextBox (IWordDocument)   Initializes a new instance of the WTextBox class.  
  ----------------------------------- -----------------------------------------------------


 

Public Properties

 


  ---------------- -------------------------------------
  Name             Description
  ChildEntities    Gets the child entities.  
  EntityType       Gets the type of the entity.  
  OwnerParagraph   Gets owner paragraph.  
  TextBoxBody      Get or sets TextBody value.  
  TextBoxFormat    Gets or sets TextBoxFormat value.  
  ---------------- -------------------------------------


 

The following example illustrates how to use the WTextBox and TextBoxFormat classes.

*[]* 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                                                       |
|                                                                                                                                                                                |
| [IWordDocument][ doc = [new] [WordDocument]();] |
|                                                                                                                                                                                |
| [IWSection][ section = doc.AddSection();]                                                 |
|                                                                                                                                                                                |
| [IWParagraph][ paragraph = section.AddParagraph();]                                       |
|                                                                                                                                                                                |
| [section.PageSetup.DifferentFirstPage = [true];]                                                                      |
|                                                                                                                                                                                |
| [section.PageSetup.DifferentOddAndEvenPages = [true];]                                                                |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [// Main doc text boxes]                                                                                                     |
|                                                                                                                                                                                |
| [paragraph.AppendText([\"Testing textboxes\"]);]                                                                    |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [// 1st text box]                                                                                                            |
|                                                                                                                                                                                |
| [IWTextBox][ mainTextbox = paragraph.AppendTextBox(150, 110);]                            |
|                                                                                                                                                                                |
| [mainTextbox.TextBoxBody.AddParagraph().AppendText([\"Textbox text 1\"]);]                                          |
|                                                                                                                                                                                |
| [mainTextbox.TextBoxFormat.FillColor = System.Drawing.[Color].Blue;]                                                  |
|                                                                                                                                                                                |
| [mainTextbox.TextBoxFormat.LineDashing = [LineDashing].LongDashDotDotGEL;]                                            |
|                                                                                                                                                                                |
| [mainTextbox.TextBoxFormat.LineWidth = 4.0f;]                                                                                              |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [// 2nd text box]                                                                                                            |
|                                                                                                                                                                                |
| [IWTextBox][ mainTextbox1 = paragraph.AppendTextBox(150, 100);]                           |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxFormat.VerticalPosition = 500;]                                                                                       |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxBody.AddParagraph().AppendText([\"Another textbox\"]);]                                        |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxFormat.FillColor = System.Drawing.[Color].Yellow;]                                               |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxFormat.LineDashing = [LineDashing].DashGEL;]                                                     |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxFormat.LineWidth = 3.75f;]                                                                                            |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxFormat.TextWrappingStyle = [TextWrappingStyle].Through;]                                         |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxFormat.TextWrappingType = [TextWrappingType].Both;]                                              |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxFormat.HorizontalAlignment = [ShapeHorizontalAlignment].Center;]                                 |
|                                                                                                                                                                                |
| [mainTextbox1.TextBoxFormat.VerticalAlignment = [ShapeVerticalAlignment].Bottom;]                                     |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [// Header/footer text boxes]                                                                                                |
|                                                                                                                                                                                |
| [paragraph = [new] [WParagraph](doc);]                                                           |
|                                                                                                                                                                                |
| [paragraph.AppendText([\"Hello textboxes\"]);]                                                                      |
|                                                                                                                                                                                |
| [IWTextBox][ textbox = paragraph.AppendTextBox(20, 50);]                                  |
|                                                                                                                                                                                |
| [textbox.TextBoxBody.AddParagraph().AppendText([\"Header textbox\"]);]                                              |
|                                                                                                                                                                                |
| [textbox.TextBoxFormat.FillColor = System.Drawing.[Color].Blue;]                                                      |
|                                                                                                                                                                                |
| [textbox.TextBoxFormat.LineDashing = [LineDashing].LongDashDotDotGEL;]                                                |
|                                                                                                                                                                                |
| [textbox.TextBoxFormat.LineWidth = 4.0f;]                                                                                                  |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [IWTextBox][ textbox1 = paragraph.AppendTextBox(250, 50);]                                |
|                                                                                                                                                                                |
| [textbox1.TextBoxBody.AddParagraph().AppendText([\"Header textbox 2\"]);]                                           |
|                                                                                                                                                                                |
| [textbox1.TextBoxFormat.FillColor = System.Drawing.[Color].Tomato;]                                                   |
|                                                                                                                                                                                |
| [textbox1.TextBoxFormat.VerticalPosition = 250;]                                                                                           |
|                                                                                                                                                                                |
| [textbox1.TextBoxFormat.LineStyle = [TextBoxLineStyle].Triple;]                                                       |
|                                                                                                                                                                                |
| [textbox1.TextBoxFormat.LineDashing = [LineDashing].LongDashGEL;]                                                     |
|                                                                                                                                                                                |
| [textbox1.TextBoxFormat.LineWidth = 6.0f;]                                                                                                 |
|                                                                                                                                                                                |
| [textbox1.TextBoxFormat.NoLine = [true];]                                                                             |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph);]                                                                        |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [paragraph = [new] [WParagraph](doc);]                                                           |
|                                                                                                                                                                                |
| [paragraph.AppendText([\"Hello footer textbox\"]);]                                                                 |
|                                                                                                                                                                                |
| [IWTextBox][ textbox2 = paragraph.AppendTextBox(120, 100);]                               |
|                                                                                                                                                                                |
| [textbox2.TextBoxFormat.VerticalPosition = 5;]                                                                                             |
|                                                                                                                                                                                |
| [textbox2.TextBoxBody.AddParagraph().AppendText([\"Footer textbox\"]);]                                             |
|                                                                                                                                                                                |
| [textbox2.TextBoxFormat.FillColor = System.Drawing.[Color].Yellow;]                                                   |
|                                                                                                                                                                                |
| [textbox2.TextBoxFormat.LineDashing = [LineDashing].DashGEL;]                                                         |
|                                                                                                                                                                                |
| [textbox2.TextBoxFormat.LineWidth = 3.75f;]                                                                                                |
|                                                                                                                                                                                |
| [textbox2.TextBoxFormat.TextWrappingStyle = [TextWrappingStyle].Square;]                                              |
|                                                                                                                                                                                |
| [textbox2.TextBoxFormat.HorizontalAlignment = [ShapeHorizontalAlignment].Left;]                                       |
|                                                                                                                                                                                |
| [textbox2.TextBoxFormat.VerticalAlignment = [ShapeVerticalAlignment].Bottom;]                                         |
|                                                                                                                                                                                |
| [section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph);]                                                                        |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [doc.Save([\"TextBoxes.doc\"]);]                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                                             |
|                                                                                                                                                                                      |
| [Dim][ doc [As] IWordDocument = [New] WordDocument()] |
|                                                                                                                                                                                      |
| [Dim][ section [As] IWSection = doc.AddSection()]                          |
|                                                                                                                                                                                      |
| [Dim][ paragraph [As] IWParagraph = section.AddParagraph()]                |
|                                                                                                                                                                                      |
| [section.PageSetup.DifferentFirstPage = [True]]                                                                             |
|                                                                                                                                                                                      |
| [section.PageSetup.DifferentOddAndEvenPages = [True]]                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                  |
|                                                                                                                                                                                      |
| [\' Main doc text boxes]                                                                                                           |
|                                                                                                                                                                                      |
| [paragraph.AppendText([\"Testing textboxes\"])]                                                                           |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [\' 1st text box]                                                                                                                  |
|                                                                                                                                                                                      |
| [Dim][ mainTextbox [As] IWTextBox = paragraph.AppendTextBox(150, 110)]     |
|                                                                                                                                                                                      |
| [mainTextbox.TextBoxBody.AddParagraph().AppendText([\"Textbox text 1\"])]                                                 |
|                                                                                                                                                                                      |
| [mainTextbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue]                                                                                |
|                                                                                                                                                                                      |
| [mainTextbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL]                                                                          |
|                                                                                                                                                                                      |
| [mainTextbox.TextBoxFormat.LineWidth = 4.0f]                                                                                                     |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [\' 2nd text box]                                                                                                                  |
|                                                                                                                                                                                      |
| [Dim][ mainTextbox1 [As] IWTextBox = paragraph.AppendTextBox(150, 100)]    |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxFormat.VerticalPosition = 500]                                                                                              |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxBody.AddParagraph().AppendText([\"Another textbox\"])]                                               |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxFormat.FillColor = System.Drawing.Color.Yellow]                                                                             |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxFormat.LineDashing = LineDashing.DashGEL]                                                                                   |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxFormat.LineWidth = 3.75f]                                                                                                   |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Through]                                                                       |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxFormat.TextWrappingType = TextWrappingType.Both]                                                                            |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxFormat.HorizontalAlignment = ShapeHorizontalAlignment.Center]                                                               |
|                                                                                                                                                                                      |
| [mainTextbox1.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom]                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [\' Header/footer text boxes]                                                                                                      |
|                                                                                                                                                                                      |
| [paragraph = [New] WParagraph(doc)]                                                                                         |
|                                                                                                                                                                                      |
| [paragraph.AppendText([\"Hello textboxes\"])]                                                                             |
|                                                                                                                                                                                      |
| [Dim][ textbox [As] IWTextBox = paragraph.AppendTextBox(20, 50)]           |
|                                                                                                                                                                                      |
| [textbox.TextBoxBody.AddParagraph().AppendText([\"Header textbox\"])]                                                     |
|                                                                                                                                                                                      |
| [textbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue]                                                                                    |
|                                                                                                                                                                                      |
| [textbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL]                                                                              |
|                                                                                                                                                                                      |
| [textbox.TextBoxFormat.LineWidth = 4.0f]                                                                                                         |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [Dim][ textbox1 [As] IWTextBox = paragraph.AppendTextBox(250, 50)]         |
|                                                                                                                                                                                      |
| [textbox1.TextBoxBody.AddParagraph().AppendText([\"Header textbox 2\"])]                                                  |
|                                                                                                                                                                                      |
| [textbox1.TextBoxFormat.FillColor = System.Drawing.Color.Tomato]                                                                                 |
|                                                                                                                                                                                      |
| [textbox1.TextBoxFormat.VerticalPosition = 250]                                                                                                  |
|                                                                                                                                                                                      |
| [textbox1.TextBoxFormat.LineStyle = TextBoxLineStyle.Triple]                                                                                     |
|                                                                                                                                                                                      |
| [textbox1.TextBoxFormat.LineDashing = LineDashing.LongDashGEL]                                                                                   |
|                                                                                                                                                                                      |
| [textbox1.TextBoxFormat.LineWidth = 6.0f]                                                                                                        |
|                                                                                                                                                                                      |
| [textbox1.TextBoxFormat.NoLine = [True]]                                                                                    |
|                                                                                                                                                                                      |
| []                                                                                                                                  |
|                                                                                                                                                                                      |
| [section.HeadersFooters.FirstPageHeader.Paragraphs.Add(paragraph)]                                                                               |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [paragraph = [New] WParagraph(doc)]                                                                                         |
|                                                                                                                                                                                      |
| [paragraph.AppendText([\"Hello footer textbox\"])]                                                                        |
|                                                                                                                                                                                      |
| [Dim][ textbox2 [As] IWTextBox = paragraph.AppendTextBox(120, 100)]        |
|                                                                                                                                                                                      |
| [textbox2.TextBoxFormat.VerticalPosition = 5]                                                                                                    |
|                                                                                                                                                                                      |
| [textbox2.TextBoxBody.AddParagraph().AppendText([\"Footer textbox\"])]                                                    |
|                                                                                                                                                                                      |
| [textbox2.TextBoxFormat.FillColor = System.Drawing.Color.Yellow]                                                                                 |
|                                                                                                                                                                                      |
| [textbox2.TextBoxFormat.LineDashing = LineDashing.DashGEL]                                                                                       |
|                                                                                                                                                                                      |
| [textbox2.TextBoxFormat.LineWidth = 3.75f]                                                                                                       |
|                                                                                                                                                                                      |
| [textbox2.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Square]                                                                            |
|                                                                                                                                                                                      |
| [textbox2.TextBoxFormat.HorizontalAlignment = ShapeHorizontalAlignment.Left]                                                                     |
|                                                                                                                                                                                      |
| [textbox2.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom]                                                                       |
|                                                                                                                                                                                      |
| [section.HeadersFooters.FirstPageFooter.Paragraphs.Add(paragraph)]                                                                               |
|                                                                                                                                                                                      |
| []                                                                                                                                               |
|                                                                                                                                                                                      |
| [doc.Save([\"TextBoxes.doc\"])]                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

