import spacy
from django.templatetags.static import static
from django.conf import settings
import glob
class Poem:
    def __init__(self) -> None:
        pass

    def speech_output(self, request):
        if request.method == "POST":
            data=request.POST.get('speech-output')
            # print('printing data')
            print(data)
            return data

    def merge_text_files(self):
        static_folder = settings.STATIC_ROOT
        files = static_folder + '/input/*.txt'
        read_files = glob.glob(files)
        print(read_files)
        with open(static_folder + "/merged/result.txt", "wb") as outfile:
            for f in read_files:
                with open(f, 'rb') as infile:
                    print(infile)
                    outfile.write(infile.read())

    def tokenize(self):
        nlp = spacy.load('en_core_web_sm')
        self.merge_text_files()
        file = settings.STATIC_ROOT + '/merged/result.txt'
        f = open(file, 'r')
        doc = nlp(f.read())
        for token in doc:
            print(token.text)

    