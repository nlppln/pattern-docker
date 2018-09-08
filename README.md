# pattern-docker

Docker container and [CWL specification](http://www.commonwl.org/) to parse text using [pattern](https://www.clips.uantwerpen.be/pattern). This Docker container is used in [nlppln](https://github.com/nlppln/nlppln/), and is required, because pattern is not compatible with Python 3, and nlppln is.

To be able to use pattern in nlppln, do:

```python
from nlppln import WorkflowGenerator

with WorkflowGenerator() as wf:

	txt_file = wf.add_input(txt_file='File')
	language = wf.add_input(language='string')

	# add more workflow inputs
	# add data processing steps

	saf = wf.pattern(in_file=txt_file, language=language)

	# add more processing tools
	# add workflow outputs
	# save workflow to file
```

The input is a text file, the output is [saf](https://github.com/vanatteveldt/saf) (json).
