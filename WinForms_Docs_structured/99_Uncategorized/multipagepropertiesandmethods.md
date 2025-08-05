---
title: multipagepropertiesandmethods.md
original_path: WinForms_Docs/99_Uncategorized/multipagepropertiesandmethods.md
created_at: 2025-08-05
---






##### MultiPage Properties and Methods {#multipage-properties-and-methods style="tab-stops: 0pt"}

[] 

The MultiPage acts as a container for **PageView** objects. The page view can contain any ASP.NET controls.

[] 

MultiPage Server Side Properties

[] 


  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------
  Property                 Description
  SelectedIndex            Specifies the page index to be selected on pageload.
  Controls                 Specifies the collection of controls contained within MultiPage control. Instances of page view can be added dynamically to MultiPage using this property.
  RenderSelectedPageOnly   When this property is set to true, SelectedIndex page alone will be visible. By default it is set to false.
  ------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

MultiPage Server Side Methods

[] 


  ------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------
  Method             Description
  GoFirst()          Displays the first pageview object in MultiPage control collection.
  GoNext()           Displays the next pageview object in MultiPage control collection.
  GoNext(bool)       Gets/sets a boolean value. When the value is true, if it\'s in the endmost page, it moves to the first page.
  GoPrevious()       Displays the previous pageview object in MultiPage Control collection.
  GoPrevious(bool)   This overloaded method takes a boolean value. When the value is set to true, it moves to the last page if there are no more pages at the beginning.
  GoLast()           Displays the last pageview object in MultiPage control collection.
  ------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------


[] 

MultiPage Client Side Methods

[] 


  ------------------ ------------------------------------------------------------------------
  Method             Description
  GetIndex()         Returns the index of the current page.
  GoFirst()          Displays the first page.
  GoLast()           Displays the last page.
  GoNext()           Displays the next page.
  GoNext(true)       If it\'s in the endmost page, it moves to the first page.
  GoPrevious()       Displays the previous page.
  GoPrevious(true)   It moves to the last page if there are no more pages at the beginning.
  PageCount()        Specifies the number of pages present in MultiPage.
  SetIndex(int)      Specifies to display the page with index provided.
  ------------------ ------------------------------------------------------------------------


[]{#p427} 

[]{#related-topics}

