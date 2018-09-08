#!/usr/bin/env python
import click
import codecs
import os
import json
import datetime
import pattern

from nlppln.utils import create_dirs, out_file_name


def parse(text, parsetree):
    tokens = []
    p = parsetree(text,
                  tokenize=True,     # Split punctuation marks from words?
                  tags=True,         # Parse part-of-speech tags? (NN, JJ, ...)
                  chunks=False,      # Parse chunks? (NP, VP, PNP, ...)
                  relations=False,   # Parse chunk relations? (-SBJ, -OBJ, ...)
                  lemmata=True,      # Parse lemmata? (ate => eat)
                  encoding='utf-8',  # Input string encoding.
                  tagset=None)       # Penn Treebank II (default) or UNIVERSAL.
    for sentence_id, sentence in enumerate(p):
        for word_id, word in enumerate(sentence):
            tokens.append({'id': word_id,
                           'word': word.string,
                           'lemma': word.lemma,
                           'sentence': sentence_id,
                           'pos': word.type})
    return tokens


@click.command()
@click.argument('in_file', type=click.File(encoding='utf-8'))
@click.option('--language', '-l', default='en',
              type=click.Choice(['en', 'es', 'de', 'fr', 'it', 'nl']))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def pattern_parse(in_file, language, out_dir):
    if language == 'en':
        from pattern.en import parsetree
    elif language == 'es':
        from pattern.es import parsetree
    elif language == 'de':
        from pattern.de import parsetree
    elif language == 'fr':
        from pattern.fr import parsetree
    elif language == 'it':
        from pattern.it import parsetree
    elif language == 'nl':
        from pattern.nl import parsetree

    tokens = parse(in_file.read(), parsetree)

    pattern_version = pattern.__version__
    header = {
                'format': 'SAF',
                'format-version': '0.1',
                'processed': [{
                    'module': "pattern.{}".format(language),
                    'module-version': pattern_version,
                    'started': datetime.date.today().strftime('%Y-%m-%d')
                }]
            }

    out_file = out_file_name(out_dir, in_file.name, 'json')
    create_dirs(out_file, is_file=True)
    with codecs.open(out_file, 'wb', encoding='utf-8') as f:
        json.dump({'header': header, 'tokens': tokens}, f, indent=4)


if __name__ == '__main__':
    pattern_parse()
