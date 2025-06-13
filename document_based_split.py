from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = '''from langchain_text_splitters import RecursiveCharacterTextSplitter
The most intuitive strategy is to split documents based on their length. This simple yet effective approach ensures that each chunk doesn't exceed a specified size limit. Key benefits of length-based splitting:

Straightforward implementation
Consistent chunk sizes
Easily adaptable to different model requirements
Types of length-based splitting:

Token-based: Splits text based on the number of tokens, which is useful when working with language models.
Character-based: Splits text based on the number of characters, which can be more consistent across different types of text.


text_splitter = RecursiveCharacterTextSplitter(chunk_size = 100, chunk_overlap = 0)

result = text_splitter.split_text(text)
print (len(result))

print (result[1:5])


'''

splitter = RecursiveCharacterTextSplitter.from_language(language= Language.PYTHON, chunk_size = 300, chunk_overlap =0)

result = splitter.split_text(text)

print (result[-1])