---
title: replace.md
original_path: WinForms_Docs/99_Uncategorized/replace.md
created_at: 2025-08-05
---








  









### Replace {#replace style="tab-stops: 0pt"}

 

**Replace** method provides support to replace text in the Word document. The following are the possible input parameters of the Replace method.

 

[·      ]**Pattern**: character pattern ( object of Regex class)

[·      ]**Replace**: replace string

[·      ]**Given**: string to be replaced

[·      ]**CaseSensitive**: defines if replace is case sensitive.

 

For example if case sensitive is set to false and you want to replace \"AA\" string, then in such case strings like \"aA\" and \"Aa\" also will be replaced.

 

[·      ]**WholeWord**: if set to true, string given must be the whole word (not the part of the word)

[·      ]**SaveFormatting**: if set to true, it will preserve the existing place holder formatting

 

The following are the variants of the Replace method.

 

[·      ]**Replace(Regex pattern, string replace)**: replaces of all occurrences of a character pattern specified by a regular expression with replace string

[·      ]**Replace(string given, string replace, bool caseSensitive, bool wholeWord)**: replaces all entries of given string with replace string, taking into consideration caseSensitive and wholeWord options

[·      ]**Replace(Regex pattern, TextSelection textSelection)**: replaces all entries of given regular expression with TextRangesHolder (TextSelection)

[·      ]**Replace(string given, TextSelection textSelection, bool caseSensitive, bool wholeWord)**: replaces all entries of given string with TextSelection, taking into consideration caseSensitive and wholeWord options

[·      ]**Replace(Regex pattern, TextBodyPart bodyPart)**: replaces all entries of given regular expression with TextBodyPart

[·      ]**Replace(string given, TextBodyPart bodyPart, bool caseSensitive, bool wholeWord)**: replaces all entries of given string with TextBodyPart, taking into consideration caseSensitive and wholeWord options

[·      ]**Replace(string given, IWordDocument replaceDoc, bool caseSensitive, bool wholeWord, bool saveFormatting)**: replaces all entries of given string with given word document, taking into consideration caseSensitive, wholeWord options and formatting option (to preserve the formatting of the existing place holder or the new document place holder)

[·      ]**Replace(string given, TextBodyPart bodyPart, bool caseSensitive, bool wholeWord, bool saveFormatting)**: replaces all entries of given string with given TextBodyPart, taking into consideration caseSensitive, wholeWord options and formatting option

[·      ]**Replace(string given, TextSelection textSelection, bool caseSensitive, bool wholeWord, bool saveFormatting)**: replaces all entries of given string with TextSelection, taking into consideration caseSensitive, wholeWord options and formatting option

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| **[Example 1:]**                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [//This sample replace specified regular expression with Picture]                                                                                                       |
|                                                                                                                                                                                                                           |
| [TextBodyPart][ textBodyPart = [new] [TextBodyPart]( doc );]                               |
|                                                                                                                                                                                                                           |
| [Image][ image = [Image].FromFile( ImagesPath + [\"Image.gif\"] );]                      |
|                                                                                                                                                                                                                           |
| [WPicture][ pict = [new] [WPicture]( doc );]                                               |
|                                                                                                                                                                                                                           |
| [pict.LoadImage( image );]                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [WParagraph][ para = [new] [WParagraph]( doc );]                                           |
|                                                                                                                                                                                                                           |
| [para.Items.Add( pict );]                                                                                                                                                             |
|                                                                                                                                                                                                                           |
| [textBodyPart.BodyItems.Insert( 0, para );]                                                                                                                                           |
|                                                                                                                                                                                                                           |
| [doc.Replace( [new] Regex( [\"A\"] ), textBodyPart );]                                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| **[Example 2:]**                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                |
|                                                                                                                                                                                                                           |
| [WordDocument][ docSource1 = [new] [WordDocument]();]                                      |
|                                                                                                                                                                                                                           |
| [docSource1.Open( DocumentsPath + FINDSOURCE1 );]                                                                                                                                     |
|                                                                                                                                                                                                                           |
| [WordDocument][ docSource2 = [new] [WordDocument]();]                                      |
|                                                                                                                                                                                                                           |
| [docSource2.Open( DocumentsPath + FINDSOURCE2 );]                                                                                                                                     |
|                                                                                                                                                                                                                           |
| [WordDocument][ docTemplate = [new] [WordDocument]();]                                     |
|                                                                                                                                                                                                                           |
| [docTemplate.Open( DocumentsPath + FINDTEMPLATE );]                                                                                                                                   |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [//Finds and returns entry of specified regular expression along with formatting]                                                                                       |
|                                                                                                                                                                                                                           |
| [TextSelection][ rangesHolder1 = docSource1.Find( [\"The PlaceHolder1 was replaced by ]]                      |
|                                                                                                                                                                                                                           |
| [this][ sample Text.[\", false, false );]]                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [//Create new TextSelection object, with text and it\'s formatting specified by ]                                                                                       |
|                                                                                                                                                                                                                           |
| [//character range.In current sample character range is a paragraph\'s range of ]                                                                                       |
|                                                                                                                                                                                                                           |
| [//symbols from 1 to 4 position.]                                                                                                                                       |
|                                                                                                                                                                                                                           |
| [TextSelection][ rangesHolder2 = [new] [TextSelection]( docSource2.LastParagraph, 1, 4 );] |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [docTemplate.Replace( [new] Regex( [\"PlaceHolder1\"] ), rangesHolder1 );]                                                                |
|                                                                                                                                                                                                                           |
| [docTemplate.Replace( [new] Regex( [\"PlaceHolder2\"] ), rangesHolder2 );]                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| **[Example 1:]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| [\'This sample replace specified regular expression with Picture]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ textBodyPart [As] TextBodyPart = [New] TextBodyPart(doc)]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ image [As] Image = Image.FromFile(ImagesPath & [\"Image.gif\"])]                                                                                                          |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ pict [As] WPicture = [New] WPicture(doc)]                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                   |
| [pict.LoadImage(image)]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ para [As] WParagraph = [New] WParagraph(doc)]                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [para.Items.Add(pict)]                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [textBodyPart.BodyItems.Insert(0, para)]                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                   |
| [doc.Replace([New] Regex([\"A\"]), textBodyPart)]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| **[Example 2:]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ docSource1 [As] WordDocument = [New] WordDocument()]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [docSource1.Open(DocumentsPath + FINDSOURCE1)]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ docSource2 [As] WordDocument = [New] WordDocument()]                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                   |
| [docSource2.Open(DocumentsPath + FINDSOURCE2)]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ docTemplate [As] WordDocument = [New] WordDocument()]                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                   |
| [docTemplate.Open(DocumentsPath + FINDTEMPLATE)]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| [\'Finds and returns entry of specified regular expression along with formatting]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ rangesHolder1 [As] TextSelection = docSource1.Find([\"The PlaceHolder1 was replaced by this sample Text.\"], [False], [False])] |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| [\'Create new TextSelection object, with text and it\'s formatting specified by ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [\'character range.In current sample character range is a paragraph\'s range of ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [\'symbols from 1 to 4 position.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                   |
| [Dim][ rangesHolder2 [As] TextSelection = [New] TextSelection(docSource2.LastParagraph, 1, 4)]                                                                                     |
|                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                   |
| [docTemplate.Replace([New] Regex([\"PlaceHolder1\"]), rangesHolder1)]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                   |
| [docTemplate.Replace([New] Regex([\"PlaceHolder2\"]), rangesHolder2)]                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

If you want to replace the first occurrence of a particular text alone, which appears more than once, set **doc.ReplaceFirst** property to **True**.

 

+---------------------------------------------------------------------------------------+
| **[\[C#\]]**                        |
|                                                                                       |
| []                                  |
|                                                                                       |
| [doc.ReplaceFirst = [true];] |
+---------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------+
| **\[VB.NET\]**                                                                        |
|                                                                                       |
|                                                                                       |
|                                                                                       |
| [doc.ReplaceFirst = [true];] |
+---------------------------------------------------------------------------------------+

 

**Replace with SingleLine Mode**

 

It is also possible to replace the string with .NET Regex **SingleLine** mode by using the **ReplaceSingleLine** method of DocIO. This enables the user to find the specified text of regular expression including the newline or carriage return, and replaces it with the given text.

 

The following table lists the overloads of this method.

 


  ------------------------------------------------------------ ------------------------------------------------------------------------------------
  Name                                                         Description
  ReplaceSingleLine(Regex, TextBodyPart)                       Replaces the pattern with specified replacement in single-line mode.
  ReplaceSingleLine(Regex, TextSelection)                      Replaces the given pattern with replacement in single-line mode.
  ReplaceSingleLine(Regex, String)                             Replaces all entries with specified pattern with replace text in single-line mode.
  ReplaceSingleLine(String, TextBodyPart, Boolean, Boolean)    Replaces the given text with specified replacement in single-line mode.
  ReplaceSingleLine(String, TextSelection, Boolean, Boolean)   Replaces the given text with replacement in single-line mode.
  ReplaceSingleLine(String, String, Boolean, Boolean)          Replaces all entries of given text with replace text in single-line mode.
  ------------------------------------------------------------ ------------------------------------------------------------------------------------


 

The following code snippet illustrates the SingleLine mode replacement.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                                      |
| []                                                                                                                 |
|                                                                                                                                                                      |
| [WordDocument][ doc = new [WordDocument](\"sample.doc\");] |
|                                                                                                                                                                      |
| [string search = \"\\\\\|(.\|\\r\\n\|\\r\|\\n)\*?\\\\\|\";]                                                                      |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [// The singleline option should cause \\r\\n to be included in .\*]                                               |
|                                                                                                                                                                      |
| [Regex expr = new Regex(search, RegexOptions.Singleline);]                                                                       |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [doc.[ReplaceSingleLine](expr, \"test\");]                                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                        |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
|                                                                                                                                                                                           |
| [Dim][ doc As New [WordDocument](\"sample.doc\")]                               |
|                                                                                                                                                                                           |
| [Dim][ search As String = \"\\\|(.\|\" & vbCr & vbLf & \"\|\" & vbCr & \"\|\" & vbLf & \")\*?\\\|\"] |
|                                                                                                                                                                                           |
| []                                                                                                                                      |
|                                                                                                                                                                                           |
| [\' The singleline option should cause \\r\\n to be included in .\*]                                                                    |
|                                                                                                                                                                                           |
| [Dim][ expr As New Regex(search, RegexOptions.Singleline)]                                           |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [doc.[ReplaceSingleLine](expr, \"test\")]                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

