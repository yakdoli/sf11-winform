---
title: find1.md
original_path: WinForms_Docs/99_Uncategorized/find1.md
created_at: 2025-08-05
---








  









### Find {#find style="tab-stops: 0pt"}

 

Essential DocIO provides various methods to improve the flexibility of the Find feature in the Word document.

 

**Find Method**

 

Find method is used to find an entry with a specified text of regular expression in the Word document.

 

Following are the possible input parameters of the Find method.

 

[·      ]given string to find.

[·      ]**caseSensitive**: defines if replace is case sensitive. For example, if case sensitive is set to false, and you want to find \"AA\" string, then in such case strings like \"aA\" and \"Aa\" also will be returned (will fit the search conditions).

[·      ]**wholeWord**: if set to true, string given must be the whole word (not part of the word).

 

The following are the variants of the Find method.

 

[·      ]**TextSelection Find(string given, bool caseSensitive, bool wholeWord)** - finds and returns an entry of specified string along with formatting, taking into consideration case-sensitive and whole word options.

[·      ]**TextSelection Find(Regex pattern)** - finds and returns entry of specified regular expression along with formatting.

[·      ]**TextSelection\[\] FindAll(Regex pattern)** - finds and returns all entries of specified regular expression along with formatting.

[·      ]**TextSelection\[\] FindAll(string given, bool caseSensitive, bool wholeWord)** - finds and returns all entries of specified string along with formatting, taking into consideration case-sensitive and whole word options.

 

The following example illustrates how to use the Find method.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                               |
| [doc.Open( \"sample.doc\" );]                                                                                                                                                                             |
|                                                                                                                                                                                                                                               |
| [TextSelection][ rangesHolder1 = doc.Find( [\"The PlaceHolder1\"], [false], [false] );] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                          |
| [doc.Open([\"sample.doc\"])]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                          |
| [Dim][ rangesHolder1 [As] TextSelection = doc.Find([\"The PlaceHolder1\"], [False], [False])] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**FindNext Method**

 

You can find a particular string from a paragraph region or table by using the **FindNext** method. The following code illustrates this.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [//To find and replace particular table]                                                                                                                               |
|                                                                                                                                                                                                                          |
| [IWTable table = doc.Sections\[0\].Tables\[0\];]                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [TextSelection selc = doc.FindNext(table [as] TextBodyItem, [\"textAA\"], [false], [false]);] |
|                                                                                                                                                                                                                          |
| [WTextRange range = selc.GetAsOneRange();]                                                                                                                                           |
|                                                                                                                                                                                                                          |
| [range.Text = [\"TextReplaced\"];]                                                                                                                           |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [//or To find and replace from particular paragraph]                                                                                                                   |
|                                                                                                                                                                                                                          |
| [IWTable table1 = doc.Sections\[0\].Tables\[0\];]                                                                                                                                    |
|                                                                                                                                                                                                                          |
| [IWParagraph par = table1.Rows\[1\].Cells\[0\].Paragraphs\[0\];]                                                                                                                     |
|                                                                                                                                                                                                                          |
| [TextSelection sel1 = doc.FindNext(par [as] TextBodyItem, [\"ref AA\"], [false], [false]);]   |
|                                                                                                                                                                                                                          |
| [WTextRange range1 = sel1.GetAsOneRange();]                                                                                                                                          |
|                                                                                                                                                                                                                          |
| [range1.Text = [\"New Text\"];]                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                |
| [\'To find and replace particular table]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                |
| [Dim][ table [As] IWTable = doc.Sections(0).Tables(0)]                                                                                               |
|                                                                                                                                                                                                                                                                |
| [Dim][ selc [As] TextSelection = doc.FindNext(TryCast(table, TextBodyItem), \"textAA\", [False], [False])] |
|                                                                                                                                                                                                                                                                |
| [Dim][ range [As] WTextRange = selc.GetAsOneRange()]                                                                                                 |
|                                                                                                                                                                                                                                                                |
| [range.Text = \"TextReplaced\"]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [\'or To find and replace from particular paragraph]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                |
| [Dim][ table1 [As] IWTable = doc.Sections(0).Tables(0)]                                                                                              |
|                                                                                                                                                                                                                                                                |
| [Dim][ par [As] IWParagraph = table1.Rows(1).Cells(0).Paragraphs(0)]                                                                                 |
|                                                                                                                                                                                                                                                                |
| [Dim][ sel1 [As] TextSelection = doc.FindNext(TryCast(par, TextBodyItem), \"ref AA\", [False], [False])]   |
|                                                                                                                                                                                                                                                                |
| [Dim][ range1 [As] WTextRange = sel1.GetAsOneRange()]                                                                                                |
|                                                                                                                                                                                                                                                                |
| [range1.Text = \"New Text\"]                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Find with SingleLine mode**

**[]** 

**FindSingleLine** method is used to find an entry in a document with a specified text of regular expression, including the newline or carriage return. This works in the same way as the SingleLine mode of .NET Regex. Note that the Find method will find the text only in a single paragraph without any newlines or carriage return considerations.

 


  ------------------------------------------ -----------------------------------------------------------------
  Name                                       Description
  FindSingleLine(Regex)                      Finds the first entry of specified pattern in single-line mode.
  FindSingleLine(String, Boolean, Boolean)   Finds the first entry of given text in single-line mode.
  ------------------------------------------ -----------------------------------------------------------------


 

It is also possible to find the string with SingleLine mode from a particular region by using the **FindNextSingleLine** method of the WordDocument class.

 


  ------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------
  Name                                                         Description
  FindNextSingleLine(TextBodyItem, Regex)                      Finds the next text which fit the specified pattern starting from start TextBodyItem using single-line mode.
  FindNextSingleLine(TextBodyItem, String, Boolean, Boolean)   Finds the next given text starting from specified. TextBodyItem using single-line mode.
  ------------------------------------------------------------ --------------------------------------------------------------------------------------------------------------


 

The following example illustrates how to find a string in the SingleLine mode.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                                      |
| []                                                                                                                 |
|                                                                                                                                                                      |
| [WordDocument][ doc = new [WordDocument](\"Sample.doc\");] |
|                                                                                                                                                                      |
| [string search = \"\\\\\[start\\\\\](.\*)\\\\\[end\\\\\]\";]                                                                     |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [// The singleline option should cause \\r\\n to be included in .\*]                                               |
|                                                                                                                                                                      |
| [Regex expr = new Regex(search, RegexOptions.Singleline);]                                                                       |
|                                                                                                                                                                      |
| [     ]                                                                                                                          |
|                                                                                                                                                                      |
| [WTable table = doc.Sections\[0\].Tables\[0\] as WTable;]                                                                        |
|                                                                                                                                                                      |
| [TextSelection\[\] sel = doc.[FindNextSingleLine](table as TextBodyItem, expr);]                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                    |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
| [Dim][ doc As New [WordDocument](\"Sample.doc\")]                                           |
|                                                                                                                                                                                                       |
| [Dim][ search As String = \"\\\[start\\\](.\*)\\\[end\\\]\"]                                                     |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [\' The singleline option should cause \\r\\n to be included in .\*]                                                                                |
|                                                                                                                                                                                                       |
| [Dim][ expr As New [Regex](search, RegexOptions.Singleline)]                                |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [Dim][ tab As WTable = TryCast(doc.Sections(0).Tables(0), WTable)]                                               |
|                                                                                                                                                                                                       |
| [Dim][ sel As TextSelection() = doc.[FindNextSingleLine](TryCast(tab, TextBodyItem), expr)] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

