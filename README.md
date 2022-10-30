# TestEditSQl_model_SPARC_dataset
SParC is built on the basis of the Spider dataset. Compared to other existing context-sensitive semantic analysis/text-to-SQL datasets, such as ATIS, it demonstrates:
-complex contextual dependencies 
-It has a great semantic diversity due to the complex coverage of SQL logic patterns in the Spider dataset.
-it requires generalization to new domains (keys, tokens, semantics) due to its cross-domain nature and invisible time for databases.

EditSQL tries to solve the context-dependent task of creating a text-to-SQL conversion query and includes interaction histories, as well as an encoding-decoding block of the utterance table in order to reliably understand the context of the user's utterance (or question). To do this, they use a BERT-based encoder that helps capture complex database structures and associate them with statements. Thus, with an arbitrary question, the model will surely correctly determine the database schema to which the question corresponds.

Model:
https://github.com/ryanzhumich/editsql

DataSet from model:
https://github.com/taoyds/sparc/blob/master/evaluation.py

https://github.com/taoyds/spider

Link to the article by the author Param Raval:
https://towardsdatascience.com/natural-language-to-sql-use-it-on-your-own-database-d4cd5784d081


Addition documentation and repository:
https://github.com/FerreroJeremy/ln2sql
https://github.com/dadashkarimi/seq2sql
https://github.com/xiaojunxu/SQLNet
http://www.ling.helsinki.fi/kit/2009s/clt231/NLTK/book/ch10-AnalyzingTheMeaningOfSentences.html#querying-a-database
