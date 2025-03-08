# Chap01/demo_gensim.py
import sys
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer

if len(sys.argv) < 2:
    print("请提供一个文件名作为参数。")
    sys.exit(1)
fname = sys.argv[1]

with open(fname, 'r') as f:
    content = f.read()
    # 使用 sumy 进行文本摘要
    parser = PlaintextParser.from_string(content, Tokenizer("english"))
    summarizer = Summarizer()
    summary = summarizer(parser.document, 5)  # 摘要句子数量为 5
    for i, sentence in enumerate(summary):
        print("%d) %s" % (i + 1, sentence))