---
title: scrollsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\scrollsettings.md
created_at: 2025-07-03
---






##### Scroll Settings {#scroll-settings style="tab-stops: 0pt"}

[] 

Scroll buttons can be used to traverse through the elements, when there are more tab elements to be viewed. The **ScrollingEnabled** property should be set to true to enable the scroll feature.

[] 

The scroll buttons can be applied to the horizontal tabstrip when the width exceeds a certain value, by setting the **ScrollWidth** property. Hence whenever the value exceeds the given scroll width, left and right scroll buttons will appear automatically. Similarly for vertical tabstrip when the height exceeds the value given in the **ScrollHeight** property, the up and down scroll buttons appears for the vertically laid TabStrip.

[] 


  ----------------------- -----------------------------------------------------------------------------------------------
  Property                Description
  ScrollDownImage         Specifies the image to be used for down scroll button.
  ScrollDownImageHover    Specifies the image to be used for down scroll button on mouse hover.
  ScrollDownLook          Specifies the class name of the css definitions to apply to the down scroll.
  ScrollHeight            Specifies the scroll height.
  ScrollingEnabled        Gets/set boolean value, whether to enable scroll feature for pop ups. Default value is false.
  ScrollLeftImage         Specifies the image to be used for left scroll button.
  ScrollLeftImageHover    Specifies the image to be used for left scroll button on mouse hover.
  ScrollRightImage        Specifies the image to be used for right scroll button.
  ScrollRightImageHover   Specifies the image to be used for right scroll button on mouse hover.
  ScrollUpImage           Specifies the image to be used for up scroll button.
  ScrollUpImageHover      Specifies the image to be used for up scroll button on mouse hover.
  ScrollUpLook            Specifies styles for up scroll region.
  ScrollWidth             Specifies the scroll width.
  ----------------------- -----------------------------------------------------------------------------------------------


[] 

[TabStrip also allows you to specify styles for the up and down scroll regions. This can be done by setting the **ScrollUpLook** and **ScrollDownLook** properties.]

[] 

{border="0"}

**[]** 

Figure 295: TabStrip with Scroll buttons

[]{#related-topics}

