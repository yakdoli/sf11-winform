---
title: keyboardnavigation2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\keyboardnavigation2.md
created_at: 2025-07-03
---






#### Keyboard Navigation {#keyboard-navigation style="tab-stops: 0pt"}

[] 

Gauge Silverlight now comes with keyboard navigation support. The keys can be used to change the pointer value in the Linear Gauge.

[] 

Default Keys

[] 

By default, the following keys on the keyboard can be used to change the pointer value:

[] 

[·      ]**UP ARROW** and **PAGE UP** keys can be used to increase the pointer value of a gauge.

[·      ]**DOWN ARROW** and **PAGE DOWN** keys can be used to decrease the value.

[·      ]**RIGHT ARROW** and **LEFT ARROW** keys increase and decrease the pointer value.

[·      ]**HOME** and **END** keys are used to set the value to Minimum and Maximum.

[·      ]**TAB** key selects the pointer to navigate.

[] 


{border="0"}Note:


***[]*** 


By default, when the pointer gets focus, its border color changes to black. This can be modified by using PointerSelectionBrush property.

Custom keys can be added to increase and decrease the pointer value by using the IncrementKey and DecrementKey properties.


[] 

The following screen shots illustrate the effect of default keys on gauge pointers:

 

1.   Initial Linear Gauge

[] 

{border="0"}

[] 

Figure 102: Linear Gauge

[] 

2.   Focus is shifted to Linear Gauge Pointer.

[] 

{border="0"}

[] 

Figure 103: Linear Gauge Pointer Focused

[] 

3.   Focus is removed from the Linear Gauge Pointer.

[] 

{border="0"}

 

Figure 104: Linear Gauge Pointer Focus Lost

[] 

4.   Linear Gauge Pointer value is increased.

[] 

{border="0"}

[] 

Figure 105: Increase in Linear Gauge Pointer Value

[] 

5.   Linear Gauge Pointer value is decreased.

[] 

{border="0"}

 

Figure 106: Decrease in Linear Gauge Pointer Value

[] 

6.   HOME key is pressed.

[] 

{border="0"}

[] 

Figure 107: Linear Gauge Pointer returns to the Start

[] 

7.   END key is pressed.

[] 

{border="0"}

[] 

Figure 108: Linear Gauge Pointer returns to the End

 

[]{#p96} 

 

More:









