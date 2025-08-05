---
title: stepsinprocessingnonolapdata.md
original_path: WinForms_Docs/03_Data_Binding/stepsinprocessingnonolapdata.md
created_at: 2025-08-05
---








  









### Steps in processing Non-OLAP data {#steps-in-processing-non-olap-data style="tab-stops: 0pt"}

To process the Non-OLAP (Such as IEnumerable, IList, DataTable, DataView, etc.) data and provide the specified formatted input to the controls. For the Non-OLAP data no need to establish any connection.

To process the Non-OLAP data:

1.   Give the two inputs:

[·      ]Item Source

[·      ]OlapReport

2.   Provide an Item source. The source can be:

[·      ]IEnumerable Collection  and

[·      ]ITyped List

3.   Once the Item source was bounded, give the **OlapReport**.

4.   The given source will be formatted based on the given **OlapReport** and the result set will be passed to the controls.

5.   The output will be displayed in the controls.

 

[]{#related-topics}

