# inclusion_py

This package provides an easy way to generate the inclusion flowchart generation for participant inclusion for medical and epidemiology analyses. It will reduce the possibility of erroneous reporting in epi research as often the inclusion conditions may vary as the research progresses. Manual flowchart generation is neither efficient or reliable. 

## How to use 
`sample_flowchart.ipynb` has a nice example and the specific format required. We expect the input to be a `Pandas` dataframe of with at least a subject id column called `PID`. All the other columns should contain bolean variables, whehter a particular subject has met the condition based on that criteria
```
sample_df.head()
pid	calibration	summary	duration
0	248	True	True	True
1	884	True	True	False
2	793	True	True	True
3	699	False	True	True
4	319	True	True	True
```

To generate the flowchart 
```python
from inclusion_py import *
my_order = ['calibration', 'duration', 'summary'] # optional. The default ordering will be used if not specified
gen_flowchart(sample_df, condition_order=my_order)
```

