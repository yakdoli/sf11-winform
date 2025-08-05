---
title: wordconverter1.md
original_path: WinForms_Docs/99_Uncategorized/wordconverter1.md
created_at: 2025-08-05
---






##### Word Converter {#word-converter style="tab-stops: 0pt"}

[] 

Export to Word is one of the most common functionalities that are required in the .NET world. The Essential Grid Control has in-built support for Word Export. Users can download the data from the Grouping Grid control into a Word document for offline verification and/or computation. This can be achieved by making use of the GroupingGridWordConverter class. This section will walk you through the conversion of the contents of the grid to a word file as well as discuss the various converter options.

 

GroupingGridWordConverter class derives from GridWordConverterBase. It contains a number of methods that helps in exporting different components of the grouping grid. You can be able to export NestedTables as well.

 

The following table lists the properties offered by Grouping Grid Word Converter. By setting these properties, you could be able to choose the elements you need to export.

[] 


  ------------ ------------------------------------------
  Property     Description
  ShowHeader   Specifies if header should be displayed.
  ShowFooter   Indicates if footer should be displayed.
  ------------ ------------------------------------------


[] 

Method

 

Grouping Grid Word Converter control provides a method called GroupingGridToWord. This is the method that does the conversion of grouping grid contents to a word file. It accepts two parameters: grouping grid to be converted and filename of the destination word document.

 

Syntax

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [GroupingGridWordConverter][ converter = [new] [GroupingGridWordConverter]();] |
|                                                                                                                                                                                                                                                     |
| [converter.GroupingGridToWord([\"Grid.doc\"], [this].gridGroupingControl1);]                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| [Dim][ converter [As] GroupingGridWordConverter = [New] GroupingGridWordConverter()] |
|                                                                                                                                                                                                                                                     |
| [converter.GroupingGridToWord([\"Grid.doc\"], [Me].gridGroupingControl1)]                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Events

 

DrawHeader and DrawFooter are the events offered by the Grouping Grid Word Converter that aids in adding as well as customizing the header and footer in the destination word document.

 

Sample Output

 

Below images depicts the conversion of grid content to a word file.

[] 

{border="0"}

[] 

*[Figure ][377][: Grid to be Exported]*

**[]** 

{border="0"}

**[]** 

*[Figure ][378][: Grid Exported to a Word File]*

[] 


{border="0"}Note: For more details, refer the following browser sample:

 

\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Grouping.Windows\\Samples\\2.0\\Export\\Word Converter Demo


 

[]{#p471} 

 

[]{#related-topics}

