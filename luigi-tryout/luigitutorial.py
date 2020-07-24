import time
import os,sys
from pprint import pprint

import luigi

TMP_PATH = 'tmp'
TXT_FILE_PATH = os.path.join(TMP_PATH, 'helloworld.txt')
AAA_FILE_PATH = os.path.join(TMP_PATH, 'aaa.txt')

class Prepare(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget(AAA_FILE_PATH)

    def run(self):
        time.sleep(0)
        with self.output().open('w') as outfile:
            outfile.write('Hello World!\n')
        time.sleep(0)

# Task A - write hello world in text file
class HelloWorld(luigi.Task):
    def requires(self):
        return None

    def output(self):
        return luigi.LocalTarget(TXT_FILE_PATH)

    def run(self):
        time.sleep(0)
        pprint(self.output())
        with self.output().open('w') as outfile:
            outfile.write('Hello World!\n')
        time.sleep(0)


# Task B - pick the text from helloworld.txt, replace World with the input name
class NameSubstituter(luigi.Task):
    name = luigi.Parameter()

    def requires(self):

        return HelloWorld()

    def output(self):
        output_filename = TMP_PATH + '.name_' + self.name
        return luigi.LocalTarget(TMP_PATH + '/' + '.name_' + self.name)

    def run(self):
        time.sleep(0)
        with self.input().open() as infile, self.output().open('w') as outfile:
            text = infile.read()
            text = text.replace('World', self.name)
            outfile.write(text)
        time.sleep(0)


if __name__ == '__main__':
    luigi.run()