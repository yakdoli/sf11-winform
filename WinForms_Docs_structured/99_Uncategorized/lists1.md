---
title: lists1.md
original_path: WinForms_Docs/99_Uncategorized/lists1.md
created_at: 2025-08-05
---






#### Lists {#lists style="tab-stops: 0pt"}

 

Lists in the Essential PDF are used to list out the items in a collection in some order to provide readability. There are two kinds of lists. They are:

 

[·      ]**Ordered list**, which is represented by the PdfOrderedList class

[·      ]**Unordered list**, which is represented by the PdfUnorderedList class

[] 

Base class for the preceding classes is the **PdfList** class, which contains an item collection represented by the **PdfListItemCollection** class. The items from the collection are represented by the **PdfListItem** class.

 

**Ordered List**

 

**PdfOrderedList** class represents an ordered list.

 

**Initialize Lists**

 

You can create new instances of the PdfOrderedList class by using the following constructors.

 

[·      ]**PdfOrderedList()**: Creates list with default settings

[·      ]**PdfOrderedList(PdfListItemCollection items)**: Creates list with the specified collection of items

[·      ]**PdfOrderedList(PdfOrderedMarker marker)**: Creates list with the specified marker

[·      ]**PdfOrderedList(PdfListItemCollection items, PdfOrderedMarker marker)**: Creates list with the specified items collection and marker

[·      ]**PdfOrderedList(string text)**: creates list from the specified text. It splits text by using the \"\\n\" symbol and creates a collection of items.

[·      ]**PdfOrderedList(string text, PdfOrderedMarker marker)**: Creates list from the specified text and with specified marker. It splits text by using the \"\\n\" symbol and creates a collection of items.

 

List Marker

 

Ordered list has ordered markers that are represented by the **PdfOrderedMarker** class. To create a new instance of the ordered marker, use the following constructors.

[] 

[·      ]**PdfOrderedMarker(PdfNumberStyle style, PdfFont font)**: Creates marker by using the PdfNumberStyle and specified font

[·      ]**PdfOrderedMarker (PdfNumberStyle style, string finalizer, PdfFont font)**: Creates marker with number style, font, finalizer, and the specified symbol that follows after number.  Default value for finalizer is \'.\'.

[·      ]**PdfOrderedMarker (PdfNumberStyle style, string delimiter, string finalizer, PdfFont font)**: Creates marker with the number style, font, finalizer, delimiter, and the specified symbol located between numbers. It is used when the **MarkerHierarchy** property of the PdfOrderedList class is set ***True***. Default value for delimiter is \'.\'.

 

Default list marker has **Number** style.

 

Features

 

Also, PdfOrderedList enables you to use numbering hierarchy, which means if you have an ordered list and one of its item has an ordered sublist, marker of it will contain the number of its parent item. This number is split by the delimiter.

 

To use numbering hierarchy, just set the **MarkerHierarchy** property of the PdfOrderedList class to ***True***. Default value is ***False***.

 

Unordered List

 

**PdfUnorderedList** class represents an unordered list.

 

Initialize Lists

 

You can create a new instance of the PdfUnorderedList class by using the following constructors.

 

[·      ]**PdfUnorderedList()**: Creates list with default settings

[·      ]**PdfUnorderedList(PdfListItemCollection items)**: Creates list with the specified collection of items

[·      ]**PdfUnorderedList(PdfUnorderedMarker marker)**: Creates list with the specified marker

[·      ]**PdfUnorderedList(PdfListItemCollection items, PdfUnorderedMarker marker)**: Creates list with the specified items collection and marker

[·      ]**PdfUnorderedList (string text)**: Creates list from the specified text. It splits the text by using the \"\\n\" symbol and creates a collection of items.

[·      ]**PdfUnorderedList (string text, PdfUnorderedMarker marker)**: Creates list from the specified text and with the specified marker. It splits text by using the \"\\n\" symbol and creates a collection of items.

 

List Marker

 

Unordered list has an unordered marker that is represented by the **PdfUnorderedMarker** class. Unordered marker has the marker style represented by the **PdfUnorderedMarkerStyle** class. The following marker styles are supported.

 

[·      ]None

[·      ]Disk

[·      ]Square

[·      ]Asterisk

[·      ]Circle

[·      ]CustomString

[·      ]CustomImage

[·      ]CustomTemplate

 

Default list marker has **Disk** style.

To use the **CustomString**, **CustomImage** or **CustomTemplate** style, you must set the **Text**, **Image** or **Template** property of the PdfUnorderedMarker class respectively.

 

Drawing Lists

 

There are a lot of **Draw** overloads that enable you to draw lists on a series of pages or on a PdfGraphics page.

 

Events

 

Each list raises the following four events:

 

[·      ]**BeginPageLayout** event is raised when the list starts layouting on page

[·      ]**EndPageLayout** event is raised when the list completes layouting on the page

[·      ]**BeginItemLayout** event is raised when the item starts layouting

[·      ]**EndItemLayout** event is raised when the item completes layouting

[] 


{border="0"}Note: You should add the Syncfusion.Pdf.List namespace to work with lists.


 

 

[]{#related-topics}

