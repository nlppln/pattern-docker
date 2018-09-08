#!/usr/bin/env cwl-runner
cwlVersion: v1.0
class: CommandLineTool
baseCommand: ["python", "/pattern_parse.py"]

doc: |
  Parse text using `pattern <https://www.clips.uantwerpen.be/pattern>`_.

  Does tokenization, lemmatization and part of speech tagging. The default language is English, but other languages can be specified (``--language [en|es|de|fr|it|nl]``).

  Output is `saf <https://github.com/vanatteveldt/saf>`_.

requirements:
  - class: DockerRequirement
    dockerPull: nlppln/pattern-docker

inputs:
  in_file:
    type: File
    inputBinding:
      position: 1
  language:
    type: string?
    default: en
    inputBinding:
      prefix: -l

outputs:
  saf:
    type: File
    outputBinding:
      glob: "*.json"
