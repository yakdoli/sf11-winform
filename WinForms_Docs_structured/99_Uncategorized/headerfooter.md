---
title: headerfooter.md
original_path: WinForms_Docs/99_Uncategorized/headerfooter.md
created_at: 2025-08-05
---








  









### Header/Footer {#headerfooter style="tab-stops: 0pt"}

**[]** 

Often, there is a need to include some information about your document at the top (the header), or the bottom (the footer) of each printed sheet. Spreadsheets often need several pages to print. It is important to put the right information on the header or footer, so you can tell which pages go together.

 

MS Excel provides an option to insert headers and footers, through the below handy dialog box from the **View** menu, to make this process as easy as possible.

 

{border="0"}

Figure 84: Page Setup Dialog Box to insert Headers and Footers

[] 

{border="0"}

Figure 85: Header Dialog Box**[]**

[] 

Inserting Headers and Footers in XlsIO

 

You can insert headers and footers through XlsIO, with the properties in the **IPageSetup**. Headers and footers can also be inserted to a Chart Worksheet.

 

The string that the header/footer takes, is a script that you can use to format the header. Please refer to the following link for more information on formatting strings: [[http://support.microsoft.com/smarterror/default.aspx?spid=global&query=213618.]{.UGHyperlink}](http://support.microsoft.com/smarterror/default.aspx?spid=global&query=213618.)

[] 


+-----------------------------------+-----------------------------------------------------+
| Codes to Format Text              | Description                                         |
+===================================+=====================================================+
| &L                                | Left-aligns the characters that follow.             |
+-----------------------------------+-----------------------------------------------------+
| &C                                | Centers the characters that follow.                 |
+-----------------------------------+-----------------------------------------------------+
| &R                                | Right-aligns the characters that follow.            |
+-----------------------------------+-----------------------------------------------------+
| &E                                | Turns double-underline printing on or off.          |
+-----------------------------------+-----------------------------------------------------+
| &X                                | Turns superscript printing on or off.               |
+-----------------------------------+-----------------------------------------------------+
| &Y                                | Turns subscript printing on or off.                 |
+-----------------------------------+-----------------------------------------------------+
| &B                                | Turns bold printing on or off.                      |
+-----------------------------------+-----------------------------------------------------+
| &I                                | Turns italic printing on or off.                    |
+-----------------------------------+-----------------------------------------------------+
| &U                                | Turns underline printing on or off.                 |
+-----------------------------------+-----------------------------------------------------+
| &S                                | Turns strikethrough printing on or off.             |
+-----------------------------------+-----------------------------------------------------+
| &\"fontname\"                     | Prints the characters that follow in the specified  |
|                                   |                                                     |
|                                   | font. Be sure to include the quotation marks around |
|                                   |                                                     |
|                                   | the font name.                                      |
+-----------------------------------+-----------------------------------------------------+
| &nn                               | Prints the characters that follow in the specified  |
|                                   |                                                     |
|                                   | font size. Use a two-digit number to specify a size |
|                                   |                                                     |
|                                   | in points.                                          |
+-----------------------------------+-----------------------------------------------------+


[] 


  ------------------------------- -----------------------------------------------------------
  Codes to Insert Specific Data   Description
  &D                              Prints the current date.
  &T                              Prints the current time.
  &F                              Prints the name of the document.
  &A                              Prints the name of the workbook tab (the \"sheet name\").
  &P                              Prints the page number.
  &P+number                       Prints the page number plus number.
  &P-number                       Prints the page number minus number.
  &&                              Prints a single ampersand.
  &N                              Prints the total number of pages in the document.
  ------------------------------- -----------------------------------------------------------


 

Following code example illustrates how to insert images in the header.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                           |
|                                                                                                                                                                                            |
| []                                                                                                                                       |
|                                                                                                                                                                                            |
| [// Insert image in right header.]                                                                                                       |
|                                                                                                                                                                                            |
| [Image][ img = [Image].FromFile([@\"logo.jpg\"]);] |
|                                                                                                                                                                                            |
| []                                                                                                                                                     |
|                                                                                                                                                                                            |
| [// Right Header Image.]                                                                                                                 |
|                                                                                                                                                                                            |
| [sheet.PageSetup.RightHeaderImage = img;]                                                                                                              |
|                                                                                                                                                                                            |
| [sheet.PageSetup.RightHeader = [\"&G\"];]                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                          |
| **[]**                                                                                                                                               |
|                                                                                                                                                                                          |
| [\' Insert image in right header.]                                                                                                     |
|                                                                                                                                                                                          |
| [Dim][ img [As] Image = Image.FromFile([\"logo.jpg\"])] |
|                                                                                                                                                                                          |
| []                                                                                                                                                   |
|                                                                                                                                                                                          |
| [\' Right Header Image.]                                                                                                               |
|                                                                                                                                                                                          |
| [sheet.PageSetup.RightHeaderImage = img]                                                                                                             |
|                                                                                                                                                                                          |
| [sheet.PageSetup.RightHeader = [\"&G\"]]                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: XlsIO does not provide any option to get the page count. You can only insert the page count by using the format string, as illustrated in the following code snippet.


[] 

+-------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                      |
|                                                                                                       |
| []                                                  |
|                                                                                                       |
| [// Setting the page number in the Center Header.]  |
|                                                                                                       |
| [sheet.PageSetup.CenterHeader = [\"&P\"];] |
+-------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                 |
|                                                                                                      |
| **[]**                                                           |
|                                                                                                      |
| [\' Setting the page number in the Center Header.] |
|                                                                                                      |
| [sheet.PageSetup.CenterHeader = [\"&P\"]] |
+------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

