# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Nicolas Hernandez 2017
# 
#
# SET in the __init__, uncomment the test to perform and set the verbosity  (0 None 1 global 2 verbose) 
# 
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import pyrata.re
import pyrata.semantic_analysis

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class TestPyrata(object):

  testCounter = 0
  testSuccess = 0


# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Main test method
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  def test (self, description = '', method = '', lexicons = {}, pattern = '', data = [], expected = [], verbosity = 0, 
    action = '', annotation= {}, group = [0], iob = False, **kwargs):
    ''' 
    general method for testing 
    '''

    if verbosity >0:
      print ('================================================')
#      print ('________________________________________________')
#      print ('------------------------------------------------')
#      print ('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
#      print ('- -  - - - - - - - - - - - - - - - - - - - - - -')



    if method == 'search':
      result = pyrata.re.search(pattern, data, lexicons=lexicons, verbosity = verbosity)
      if result != None:
        result = result.group()
    elif method == 'findall':
      result = pyrata.re.findall(pattern, data, lexicons=lexicons, verbosity = verbosity)
    elif method == 'finditer':
      result = pyrata.re.finditer(pattern, data, lexicons=lexicons, verbosity = verbosity) 
    elif method == 'annotate':
      result = pyrata.re.annotate (pattern, annotation, data, group, action, iob, verbosity = verbosity, **kwargs)

    else:
      raise Exception('wrong method to test')
    #print('Result:',l.lexer.finalresult,'; start:',l.lexer.groupstartindex,'; end:',l.lexer.groupendindex)
    #if debug:
    if verbosity >0:
      print ()
      print ('Test:\t', description)
      print ('Method:\t', method) 
      if action != '': print ('Action:\t', action) 
      if lexicons != {}: print ('Lexicons:\t', lexicons)       
      print ('Pattern:\t', pattern)
      if group != [0]:       print ('Group:\t', group)
      if annotation != {}:       print ('Annotation:\t', annotation)
      print ('Data:\t\t', data)
      print ('Expected:\t', expected)
      print ('Recognized:\t', result) 
    if result == expected:
      if verbosity >0:
        print ('Result:\tSUCCESS')
      self.testSuccess += 1
    else:
      if verbosity >0:
        print ('Result:\tFAIL') 
        #exit()
    self.testCounter +=1

    if verbosity >0:
      print ()
    
  # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
  # Test cases definitions
  # by default (if not specified) 
  # * a step is an atomic constraint wi eq operator
  # * the pattern is at least present once
  # * data is made of one or several elements
  # """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


  def test_search_step_in_data(self, verbosity):
    description = 'test_search_step_in_data'
    method = 'search'
    lexicons = {}
    pattern = 'pos="JJ"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [{'pos': 'JJ', 'raw': 'fast'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_step_in_data(self, verbosity):
    description = 'test_findall_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="JJ"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'JJ', 'raw': 'fast'}], [{'pos': 'JJ', 'raw': 'easy'}], [{'pos': 'JJ', 'raw': 'funny'}], [{'pos': 'JJ', 'raw': 'regular'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_finditer_step_in_data(self, verbosity):
    description = 'test_finditer_step_in_data'
    method = 'finditer'
    lexicons = {}
    pattern = 'pos="JJ"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    matcheslist = pyrata.semantic_analysis.MatchesList()  
    matcheslist.append(pyrata.semantic_analysis.Match (start=2, end=3, value=[{'pos': 'JJ', 'raw': 'fast'}]))
    matcheslist.append(pyrata.semantic_analysis.Match (start=3, end=4, value=[{'pos': 'JJ', 'raw': 'easy'}]))
    matcheslist.append(pyrata.semantic_analysis.Match (start=5, end=6, value=[{'pos': 'JJ', 'raw': 'funny'}]))
    matcheslist.append(pyrata.semantic_analysis.Match (start=8, end=9, value=[{'pos': 'JJ', 'raw': 'regular'}]))
    expected = matcheslist
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_search_step_absent_in_data(self, verbosity):
    description = 'test_search_step_absent_in_data'
    method = 'search'
    lexicons = {}
    pattern = 'foo="bar"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_step_absent_in_data(self, verbosity):
    description = 'test_findall_step_absent_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'foo="bar"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_search_class_step_in_data(self, verbosity):
    description = 'test_search_class_step_in_data'
    method = 'search'
    lexicons = {}
    pattern = '[pos="VB" | pos="VBZ"]'
    #data = [{'raw':'The', 'lem':'the', 'pos':'DT'}, {'raw':'big', 'lem':'big', 'pos':'JJ'}, {'raw':'fat', 'lem':'fat', 'pos':'JJ'}, {'raw':'giant', 'lem':'giant', 'pos':'JJ'}, {'raw':'cars', 'lem':'car', 'pos':'NN'}, {'raw':'are', 'lem':'be', 'pos':'VB'}, {'raw':'amazing', 'lem':'amaze', 'pos':'JJ'}]     
    #expected = [ {'raw':'are', 'lem':'be', 'pos':'VB'}]
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, 
      {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, 
      {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, 
      {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [{'pos': 'VBZ', 'raw': 'is'}]   
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_search_rich_class_step_in_data(self, verbosity):
    description = 'test_search_rich_class_step_in_data'
    method = 'search'
    lexicons = {}
    pattern = '[(pos="VB" | pos="VBZ") & !raw="is"]'
    #data = [{'raw':'The', 'lem':'the', 'pos':'DT'}, {'raw':'big', 'lem':'big', 'pos':'JJ'}, {'raw':'fat', 'lem':'fat', 'pos':'JJ'}, {'raw':'giant', 'lem':'giant', 'pos':'JJ'}, {'raw':'cars', 'lem':'car', 'pos':'NN'}, {'raw':'are', 'lem':'be', 'pos':'VB'}, {'raw':'amazing', 'lem':'amaze', 'pos':'JJ'}]     
    #expected = [ {'raw':'are', 'lem':'be', 'pos':'VB'}]
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, 
      {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, 
      {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, 
      {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [{'pos': 'VBZ', 'raw': 'is'}]   

  def test_findall_regex_step_in_data(self, verbosity):
    description = 'test_findall_regex_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos~"NN.*"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'NNS', 'raw': 'expressions'}], [{'pos': 'NNP', 'raw': 'Pyrata'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_lexicon_step_in_data(self, verbosity):
    description = 'test_findall_lexicon_step_in_data'
    method = 'findall'
    lexicons = {'positiveLexicon':['easy', 'funny']}
    pattern = 'raw@"positiveLexicon"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[ {'pos': 'JJ', 'raw': 'easy'}], [{'pos': 'JJ', 'raw': 'funny'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)   

  def test_findall_undefined_lexicon_step_in_data(self, verbosity):
    description = 'test_findall_undefined_lexicon_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'raw@"positiveLexicon"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)      

  def test_findall_multiple_lexicon_step_in_data(self, verbosity):
    description = 'test_findall_multiple_lexicon_step_in_data'
    method = 'findall'
    lexicons = {'positiveLexicon':['easy', 'funny'], 'negativeLexicon':['fast', 'regular']}
    pattern = '[raw@"positiveLexicon" | raw@"negativeLexicon"]'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[ {'pos': 'JJ', 'raw': 'fast'}], [ {'pos': 'JJ', 'raw': 'easy'}], [{'pos': 'JJ', 'raw': 'funny'}],[ {'pos': 'JJ', 'raw': 'regular'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)  


  def test_search_optional_step_in_data(self, verbosity):
    # echo 1 | perl -ne '$s = "abcbdb"; if ($s =~ /b?/) {print "matched>$1<\n";} else {print "unmatched\n"}'
    # echo 1 | perl -ne '$s = "abcbdb"; if ($s =~ /e?/) {print "matched>$1<\n";} else {print "unmatched\n"}'
    # both return matche but wo any character
    description = 'test_search_optional_step_in_data'
    method = 'search'
    lexicons = {}
    pattern = 'pos="JJ"?'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [{'raw': 'fast', 'pos': 'JJ'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_optional_step_in_data(self, verbosity):
    # echo 1 | perl -ne '$s = "abcbdb"; if ($s =~ /b?/) {print "matched>$1<\n";} else {print "unmatched\n"}'
    # echo 1 | perl -ne '$s = "abcbdb"; if ($s =~ /e?/) {print "matched>$1<\n";} else {print "unmatched\n"}'
    # both return matche but wo any character
    description = 'test_findall_optional_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="JJ"?'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'JJ', 'raw': 'fast'}], [{'pos': 'JJ', 'raw': 'easy'}], [{'pos': 'JJ', 'raw': 'funny'}], [{'pos': 'JJ', 'raw': 'regular'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_step_step_in_data(self, verbosity):
    description = 'test_findall_step_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="JJ" pos="NNS"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[ {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_optional_step_step_in_data(self, verbosity):
    description = 'test_findall_optional_step_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="JJ"? pos~"NN.*"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[ {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}], [{'raw': 'Pyrata', 'pos': 'NNP'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_any_step_step_in_data(self, verbosity):
    description = 'test_findall_any_step_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="JJ"* pos~"NN.*"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[ {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}], [{'raw': 'Pyrata', 'pos': 'NNP'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_at_least_one_step_step_in_data(self, verbosity):
    description = 'test_findall_at_least_one_step_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="JJ"+ pos~"NN.*"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[ {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_any_step_step_nbar_in_data(self, verbosity):
    # https://gist.github.com/alexbowe/879414
    # echo 0 | perl -ne '$s = "abccd"; if ($s =~ /([bc]c)/) {print "$1\n"}'
    # bc
    description = 'test_findall_any_step_step_nbar_in_data'
    method = 'findall'
    lexicons = {}
    pattern = '[pos~"NN.*" | pos="JJ"]* pos~"NN.*"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    #data = [ {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}],[{'pos': 'NNP', 'raw': 'Pyrata'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)    

  def test_findall_at_least_one_step_step_nbar_in_data(self, verbosity):
    # https://gist.github.com/alexbowe/879414
    # echo 0 | perl -ne '$s = "abccd"; if ($s =~ /([bc]c)/) {print "$1\n"}'
    # bc
    description = 'test_findall_at_least_one_step_step_nbar_in_data'
    method = 'findall'
    lexicons = {}
    pattern = '[pos~"NN.*" | pos="JJ"]+ pos~"NN.*"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    #data = [ {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)   

  def test_findall_step_step_partially_matched_in_data_ending(self, verbosity):
    description = 'test_findall_step_step_partially_matched_in_data_ending'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="NNS" pos="JJ"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_optional_step_step_partially_matched_in_data_ending(self, verbosity):
    description = 'test_findall_optional_step_step_partially_matched_in_data_ending'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="NNS"? pos="JJ"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'JJ', 'raw': 'fast'}], [{'pos': 'JJ', 'raw': 'easy'}], [{'pos': 'JJ', 'raw': 'funny'}], [{'pos': 'JJ', 'raw': 'regular'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_any_step_step_partially_matched_in_data_ending(self, verbosity):
    description = 'test_findall_any_step_step_partially_matched_in_data_ending'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="NNS"? pos="JJ"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'JJ', 'raw': 'fast'}], [{'pos': 'JJ', 'raw': 'easy'}], [{'pos': 'JJ', 'raw': 'funny'}], [{'pos': 'JJ', 'raw': 'regular'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_at_least_one_step_step_partially_matched_in_data_ending(self, verbosity):
    description = 'test_findall_at_least_one_step_step_partially_matched_in_data_ending'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="NNS"+ pos="JJ"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)


  def test_findall_step_at_least_one_not_step_step_in_data(self, verbosity):
    description = 'test_findall_step_at_least_one_not_step_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="VB" !pos="NNS"+ pos="NNS"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_step_present_optional_step_step_in_data(self, verbosity):
    description = 'test_findall_step_present_optional_step_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="VB" pos="JJ"? pos="NNS"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_step_absent_optional_step_step_in_data(self, verbosity):
    description = 'test_findall_step_absent_optional_step_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="IN" pos="JJ"? pos="NNP"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)


  def test_findall_step_optional_step_in_data(self, verbosity):
    #echo 0 |  perl -ne '$s="abbbcb"; if ($s =~/(bc?)/) {print "$1\n"}' gives b
    description = 'test_findall_step_optional_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="JJ" pos~"NN.*"?'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'raw': 'fast', 'pos': 'JJ'}], [{'raw': 'easy', 'pos': 'JJ'}], [{'raw': 'funny', 'pos': 'JJ'}], [{'raw': 'regular', 'pos': 'JJ'}, {'raw': 'expressions', 'pos': 'NNS'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_step_any_step_in_data(self, verbosity):
    description = 'test_findall_step_any_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="JJ" pos~"NN.*"*'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'raw': 'fast', 'pos': 'JJ'}], [{'raw': 'easy', 'pos': 'JJ'}], [{'raw': 'funny', 'pos': 'JJ'}], [{'raw': 'regular', 'pos': 'JJ'}, {'raw': 'expressions', 'pos': 'NNS'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)

  def test_findall_step_optinal_step_optional_step_step_in_data(self, verbosity):
    #echo 0 |  perl -ne '$s="abbbcb"; if ($s =~/(bc?)/) {print "$1\n"}' gives b
    description = 'test_findall_step_optinal_step_optional_step_step_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos="VBZ" pos="JJ"? pos="JJ"? pos="CC"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'}, {'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[ {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)
  
  def test_search_any_class_step_error_step_in_data(self, verbosity):
    description = 'test_search_any_class_step_error_step_in_data'
    method = 'search'
    lexicons = {}
    pattern = '[pos~"NN.*" | pos="JJ"]* blabla pos~"NN.*"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)    

  def test_findall_step_any_not_step1_step1_in_data(self, verbosity):
    # https://gist.github.com/alexbowe/879414
    description = 'test_findall_step_any_not_step1_step1_in_data'
    method = 'findall'
    lexicons = {}
    pattern = 'pos~"VB." [!raw="to"]* raw="to"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [[{'raw': 'is', 'pos': 'VBZ'}, {'raw': 'fast', 'pos': 'JJ'}, {'raw': 'easy', 'pos': 'JJ'}, {'raw': 'and', 'pos': 'CC'}, {'raw': 'funny', 'pos': 'JJ'}, {'raw': 'to', 'pos': 'TO'}]]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)    

  def test_pattern_starting_with_the_first_token_of_data_present_as_expected_in_data(self, verbosity):
    # ^ matches the start of data before the first token in a data.
    # $ matches the end of data ~after the last token of data.
    # test_pattern_starting_with_the_first_token_of_data_present_as_expected_in_data
    # test_pattern_ending_with_the_last_token_of_data_present_as_expected_in_data
    # test_pattern_starting_with_the_first_token_of_data_and_ending_with_the_last_token_of_data_present_as_expected_in_data   
    # test_pattern_starting_with_the_first_token_of_data_not_present_as_expected_in_data
    # test_pattern_ending_with_the_last_token_of_data_not_present_as_expected_in_data
    # test_pattern_starting_with_the_first_token_of_data_and_ending_with_the_last_token_of_data_not_present_as_expected_in_data  
    description = 'test_pattern_starting_with_the_first_token_of_data_present_as_expected_in_data'
    method = 'search'
    lexicons = {}
    pattern = '^raw="It" raw="is"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)  

  def test_pattern_ending_with_the_last_token_of_data_present_as_expected_in_data(self, verbosity):
    description = 'test_pattern_ending_with_the_last_token_of_data_present_as_expected_in_data'
    method = 'search'
    lexicons = {}
    pattern = 'raw="with" raw="Pyrata"$'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [{'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)  

  def test_pattern_starting_with_the_first_token_of_data_and_ending_with_the_last_token_of_data_present_as_expected_in_data(self, verbosity):

    description = 'test_pattern_starting_with_the_first_token_of_data_and_ending_with_the_last_token_of_data_present_as_expected_in_data'
    method = 'search'
    lexicons = {}
    pattern = '^raw="with" raw="Pyrata"$'
    data = [{'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = [{'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity)  


  def test_pattern_starting_with_the_first_token_of_data_not_present_as_expected_in_data(self, verbosity):
    description = 'test_pattern_starting_with_the_first_token_of_data_not_present_as_expected_in_data'
    method = 'search'
    lexicons = {}
    pattern = '^raw="is" raw="fast"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)  


  def test_pattern_starting_with_the_first_token_of_data_not_present_as_expected_in_data(self, verbosity):
    description = 'test_pattern_starting_with_the_first_token_of_data_present_as_expected_in_data'
    method = 'search'
    lexicons = {}
    pattern = '^raw="is" raw="fast"'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)  

  def test_pattern_ending_with_the_last_token_of_data_not_present_as_expected_in_data(self, verbosity):
    description = 'test_pattern_ending_with_the_last_token_of_data_not_present_as_expected_in_data'
    method = 'search'
    lexicons = {}
    pattern = 'raw="is" raw="fast"$'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)  

  def test_pattern_starting_with_the_first_token_of_data_and_ending_with_the_last_token_of_data_not_present_as_expected_in_data(self, verbosity):
    description = 'test_pattern_starting_with_the_first_token_of_data_and_ending_with_the_last_token_of_data_not_present_as_expected_in_data'
    method = 'search'
    lexicons = {}
    pattern = '^raw="is" raw="fast"$'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    expected = None
    self.test(description, method, lexicons, pattern, data, expected, verbosity)  


  def test_search_groups_in_data(self, verbosity):
    if verbosity >0:
      print ('================================================')
    description = 'test_search_groups_in_data'
    method = 'search'
    lexicons = {}
    pattern = 'raw="It" (raw="is") (( pos="JJ"* (pos="JJ" raw="and") (pos="JJ") )) (raw="to")'
    #pattern = 'raw="It" (raw="is" |fa="ke") (( pos="JJ"* (pos="JJ" raw="and"|fa="ke") (pos="JJ"|fa="ke") |fa="ke")|fa="ke") (raw="to"|fa="ke")'
    #pattern = 'raw="It" (raw="is"|fa="ke") (( pos="JJ"* (pos="JJ" raw="and") (pos="JJ") )|fa="ke") (raw="to"|fa="ke")'
    #pattern = 'raw="It" (raw="is"|fa="ke") (( pos="JJ"* (pos="JJ" raw="and") (pos="JJ") )) (raw="to"|fa="ke")'
    #pattern = 'raw="A" (raw="B") (( raw="C"* (raw="C" raw="D") (raw="E") )) (raw="F")'

    #pattern = '(raw="is") (( pos="JJ"* (pos="JJ" raw="and") (pos="JJ") )) (raw="to")'
    data = [{'pos': 'PRP', 'raw': 'It'}, {'pos': 'VBZ', 'raw': 'is'}, {'pos': 'JJ', 'raw': 'fast'}, {'pos': 'JJ', 'raw': 'easy'}, {'pos': 'CC', 'raw': 'and'}, {'pos': 'JJ', 'raw': 'funny'}, {'pos': 'TO', 'raw': 'to'}, {'pos': 'VB', 'raw': 'write'}, {'pos': 'JJ', 'raw': 'regular'}, {'pos': 'NNS', 'raw': 'expressions'}, {'pos': 'IN', 'raw': 'with'},{'pos': 'NNP', 'raw': 'Pyrata'}]
    #data = [{'raw': 'A'}, {'raw': 'B'}, {'raw': 'C'}, {'raw': 'C'}, {'raw': 'D'}, {'raw': 'E'}, {'raw': 'F'}, {'raw': 'G'}, {'raw': 'H'}, {'raw': 'I'}, {'raw': 'J'},{'raw': 'K'}]

    expected = [[[{'pos': 'PRP', 'raw': 'It'}, {'raw': 'is', 'pos': 'VBZ'}, {'raw': 'fast', 'pos': 'JJ'}, {'raw': 'easy', 'pos': 'JJ'}, {'raw': 'and', 'pos': 'CC'}, {'raw': 'funny', 'pos': 'JJ'}, {'raw': 'to', 'pos': 'TO'}], 0, 7], [[{'raw': 'is', 'pos': 'VBZ'}], 1, 2], [[{'raw': 'fast', 'pos': 'JJ'}, {'raw': 'easy', 'pos': 'JJ'}, {'raw': 'and', 'pos': 'CC'}, {'raw': 'funny', 'pos': 'JJ'}], 2, 6], [[{'raw': 'fast', 'pos': 'JJ'}, {'raw': 'easy', 'pos': 'JJ'}, {'raw': 'and', 'pos': 'CC'}, {'raw': 'funny', 'pos': 'JJ'}], 2, 6], [[{'raw': 'easy', 'pos': 'JJ'}, {'raw': 'and', 'pos': 'CC'}], 3, 5], [[{'raw': 'funny', 'pos': 'JJ'}], 5, 6], [[{'raw': 'to', 'pos': 'TO'}], 6, 7]]
    #self.test(description, method, lexicons, pattern, data, expected, verbosity)  
    result = pyrata.re.search(pattern, data, lexicons=lexicons, verbosity = verbosity)
    print ('Debug: result=',result)
    result = result.groups

    #print ('Debug: type(result)=',result)
    if verbosity >0:
      print ()
      print ('Test:\t', description)
      print ('Method:\t', method) 
      print ('Lexicons:\t', lexicons)       
      print ('Pattern:\t', pattern)
      print ('Data:\t\t', data)
      print ('Expected groups:\t', expected)
      print ('Recognized groups:\t', result) 
    if result == expected:
      if verbosity >0:
        print ('Result:\tSUCCESS')
      self.testSuccess += 1
    else:
      if verbosity >0:
        print ('Result:\tFAIL')
    self.testCounter +=1

    if verbosity >0:
      print ()




  def test_annotate_default_action_sub_default_group_default_iob_annotation_dict_in_data(self, verbosity):
    if verbosity >0:
      print ('================================================')
    description = 'test_annotate_default_action_sub_default_group_default_iob_annotation_dict_in_data'
    method = 'annotate'
    pattern = 'pos~"NN.?"'
    annotation = {'raw':'smurf', 'pos':'NN' },
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [{'pos': 'IN', 'raw': 'Over'}, {'pos': 'DT', 'raw': 'a'}, {'pos': 'NN', 'raw': 'smurf'}, {'pos': 'IN', 'raw': 'of'}, {'pos': 'NN', 'raw': 'smurf'}, {'pos': ',', 'raw': ','}, {'pos': 'NN', 'raw': 'smurf'}, {'pos': 'NN', 'raw': 'smurf'}, {'pos': 'VBD', 'raw': 'told'}, {'pos': 'PRP$', 'raw': 'his'}, {'pos': 'NN', 'raw': 'smurf'}]
    result = pyrata.re.annotate(pattern, annotation, data, verbosity = verbosity)
    if verbosity >0:
      print ()
      print ('Test:\t', description)
      print ('Method:\t', method)
      print ('Action:\t', 'default (i.e. sub)')
      print ('Pattern:\t', pattern)
      print ('Group:\t', 'default (i.e. [0])')      
      print ('Annotation:\t', annotation) 
      print ('IOB:\t', 'default (i.e. False)')
      print ('Data:\t\t', data)
      print ('Expected:\t', expected)
      print ('Result:\t\t', result) 
    if result == expected:
      if verbosity >0:
        print ('Result:\tSUCCESS')
      self.testSuccess += 1
    else:
      if verbosity >0:
        print ('Result:\tFAIL')
    self.testCounter +=1

    if verbosity >0:
      print ()

    gold = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT', 'chunk':'B-NP'}, 
      {'raw':'cup', 'pos':'NN', 'chunk':'I-NP'},
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN', 'chunk':'B-NP'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP', 'chunk':'B-NP'}, 
      {'raw':'Stone', 'pos':'NNP', 'chunk':'I-NP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$', 'chunk':'B-NP'}, 
      {'raw':'story', 'pos':'NN', 'chunk':'I-NP'} ]


  def test_annotate_default_action_sub_default_group_default_iob_annotation_dict_not_in_data(self, verbosity):
    description = 'test_annotate_default_action_sub_default_group_default_iob_annotation_dict_not_in_data'
    method = 'annotate'
    action = 'sub'
    pattern = 'pos="JJ"'
    lexicons = {}
    annotation = {'raw':'smurf', 'pos':'NN' }
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'}, 
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, {'raw':'story', 'pos':'NN'} ]
    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation)


  def test_annotate_default_action_sub_default_group_default_iob_annotation_empty_in_data(self, verbosity):
    description = 'test_annotate_default_action_sub_default_group_default_iob_annotation_empty_in_data'
    method = 'annotate'
    action = 'sub'
    pattern = 'pos~"NN.?"'
    lexicons = {}
    annotation = []
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'of', 'pos':'IN'},
      {'raw':',', 'pos':','},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation)



  def test_annotate_default_action_sub_default_group_default_iob_annotation_dict_pattern_sequence_to_annotation_step_in_data(self, verbosity):
    description = 'test_annotate_default_action_sub_default_group_default_iob_annotation_dict_pattern_sequence_to_annotation_step_in_data'
    method = 'annotate'
    action = 'sub'
    pattern = 'pos~"(DT|PRP\$)" pos~"NN.?"'
    lexicons = {}
    annotation = {'raw':'smurf', 'pos':'NN' }
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, {'raw':'story', 'pos':'NN'} ]
    expected = [{'raw': 'Over', 'pos': 'IN'}, 
      {'raw': 'smurf', 'pos': 'NN'}, 
      {'raw': 'of', 'pos': 'IN'}, 
      {'raw': 'coffee', 'pos': 'NN'}, 
      {'raw': ',', 'pos': ','}, 
      {'raw': 'Mr.', 'pos': 'NNP'}, {'raw': 'Stone', 'pos': 'NNP'}, 
      {'raw': 'told', 'pos': 'VBD'}, 
      {'raw': 'smurf', 'pos': 'NN'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation)  #def test (self, description = '', method = '', lexicons = {}, pattern = '', data = [], expected = [], verbosity = 0, action = '', annotation= {}, group = [0], iob = False, **kwargs):


  def test_annotate_default_action_sub_group_one_default_iob_annotation_dict_pattern_in_data (self, verbosity):
    description = 'test_annotate_default_action_sub_group_one_default_iob_annotation_dict_pattern_in_data'
    method = 'annotate'
    action = 'sub'
    pattern = 'pos~"(DT|PRP\$)" (pos~"NN.?")'
    group = [1]
    lexicons = {}
    annotation = {'raw':'smurf', 'pos':'NN' }
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [{'raw': 'Over', 'pos': 'IN'}, {'raw': 'a', 'pos': 'DT'}, {'raw': 'smurf', 'pos': 'NN'}, {'raw': 'of', 'pos': 'IN'}, {'raw': 'coffee', 'pos': 'NN'}, {'raw': ',', 'pos': ','}, {'raw': 'Mr.', 'pos': 'NNP'}, {'raw': 'Stone', 'pos': 'NNP'}, {'raw': 'told', 'pos': 'VBD'}, {'raw': 'his', 'pos': 'PRP$'}, {'raw': 'smurf', 'pos': 'NN'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation, group)  
    #def test (self, description = '', method = '', lexicons = {}, pattern = '', data = [], expected = [], verbosity = 0, action = '', annotation= {}, group = [0], iob = False, **kwargs):



  def test_annotate_default_action_update_default_group_default_iob_annotation_dict_pattern_in_data(self, verbosity):
    description = 'test_annotate_default_action_update_default_group_default_iob_annotation_dict_pattern_in_data'
    method = 'annotate'
    action = 'update'
    pattern = 'pos~"(DT|PRP\$|NNP)"? pos~"NN.?"'
    lexicons = {}
    annotation = {'raw':'smurf', 'pos':'NN', 'chunk':'NP'}
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [{'pos': 'IN', 'raw': 'Over'}, {'chunk': 'NP', 'pos': 'NN', 'raw': 'smurf'}, {'chunk': 'NP', 'pos': 'NN', 'raw': 'smurf'}, {'pos': 'IN', 'raw': 'of'}, {'chunk': 'NP', 'pos': 'NN', 'raw': 'smurf'}, {'pos': ',', 'raw': ','}, {'chunk': 'NP', 'pos': 'NN', 'raw': 'smurf'}, {'chunk': 'NP', 'pos': 'NN', 'raw': 'smurf'}, {'pos': 'VBD', 'raw': 'told'}, {'chunk': 'NP', 'pos': 'NN', 'raw': 'smurf'}, {'chunk': 'NP', 'pos': 'NN', 'raw': 'smurf'}]
    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation)  #def test (self, description = '', method = '', lexicons = {}, pattern = '', data = [], expected = [], verbosity = 0, action = '', annotation= {}, group = [0], iob = False, **kwargs):

  def test_annotate_default_action_extend_default_group_default_iob_annotation_dict_pattern_in_data(self, verbosity):
    description = 'test_annotate_default_action_extend_default_group_default_iob_annotation_dict_pattern_in_data'
    method = 'annotate'
    action = 'extend'
    pattern = 'pos~"(DT|PRP\$|NNP)"? pos~"NN.?"'
    lexicons = {}
    annotation = {'raw':'smurf', 'pos':'NN', 'chunk':'NP'}
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' , 'chunk':'NP'}, 
      {'raw':'cup', 'pos':'NN' , 'chunk':'NP'},
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN', 'chunk':'NP'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP', 'chunk':'NP'}, 
      {'raw':'Stone', 'pos':'NNP', 'chunk':'NP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$', 'chunk':'NP'}, 
      {'raw':'story', 'pos':'NN', 'chunk':'NP'} ]

    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation)  #def test (self, description = '', method = '', lexicons = {}, pattern = '', data = [], expected = [], verbosity = 0, action = '', annotation= {}, group = [0], iob = False, **kwargs):


  def test_annotate_default_action_extend_default_group_default_iob_annotation_sequence_of_dict_for_single_token_match_in_data(self, verbosity):
    description = 'test_annotate_default_action_extend_default_group_default_iob_annotation_sequence_of_dict_for_single_token_match_in_data'
    method = 'annotate'
    action = 'extend'
    pattern = 'pos~"(DT|PRP\$|NNP)"? pos~"NN.?"'
    lexicons = {}
    annotation = {'chunk':'NP'}
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' , 'chunk':'NP'}, 
      {'raw':'cup', 'pos':'NN' , 'chunk':'NP'},
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN', 'chunk':'NP'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP', 'chunk':'NP'}, 
      {'raw':'Stone', 'pos':'NNP', 'chunk':'NP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$', 'chunk':'NP'}, 
      {'raw':'story', 'pos':'NN', 'chunk':'NP'} ]
    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation)  #def test (self, description = '', method = '', lexicons = {}, pattern = '', data = [], expected = [], verbosity = 0, action = '', annotation= {}, group = [0], iob = False, **kwargs):


  def test_annotate_default_action_extend_default_group_default_iob_annotation_sequence_of_dict_for_single_token_match_in_data(self, verbosity):
    description = 'test_annotate_default_action_extend_default_group_default_iob_annotation_sequence_of_dict_for_single_token_match_in_data'
    method = 'annotate'
    action = 'extend'
    pattern = 'pos~"NN.?"'
    lexicons = {}
    annotation = [{'raw':'smurf1'}, {'raw':'smurf2'} ]
    group = [0]
    iob = True
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation, group, iob)  




  def test_annotate_default_action_extend_default_group_iob_True_annotation_sequence_by_one_dict_in_data(self, verbosity):
    description = 'test_annotate_default_action_extend_default_group_iob_True_annotation_sequence_by_one_dict_in_data'
    method = 'annotate'
    action = 'extend'
    pattern = 'pos~"(DT|PRP\$|NNP)"? pos~"NN.?"'
    lexicons = {}
    annotation = {'chunk':'NP'}
    group = [0]
    iob = True
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' , 'chunk':'B-NP'}, 
      {'raw':'cup', 'pos':'NN' , 'chunk':'I-NP'},
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN', 'chunk':'B-NP'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP', 'chunk':'B-NP'}, 
      {'raw':'Stone', 'pos':'NNP', 'chunk':'I-NP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$', 'chunk':'B-NP'}, 
      {'raw':'story', 'pos':'NN', 'chunk':'I-NP'} ]
    self.test(description, method, lexicons, pattern, data, expected, verbosity, action, annotation, group, iob)  
    #def test (self, description = '', method = '', lexicons = {}, pattern = '', data = [], expected = [], verbosity = 0, action = '', annotation= {}, group = [0], iob = False, **kwargs):



  def test_search_alternative_groups_in_data(self, verbosity):
    if verbosity >0:
      print ('================================================')
    description = 'test_search_alternative_groups_in_data'
    method = 'search'
    group = [1]
    lexicons = {}
    pattern = '(raw="a" raw="cup" raw="of" raw="coffee")'
    pattern = '(raw="a" raw="cup" raw="of" raw="coffee" | raw="a" raw="tea" )' # Error: syntactic parsing error - unexpected token type="NAME" with value="raw" at position 54. Search an error before this point.
    pattern = '((raw="a" raw="cup" raw="of" raw="coffee") | (raw="a" raw="tea" ))'

    pattern = '((raw="of" raw="coffee") | (raw="of" raw="tea" ))'
    pattern = '(raw="of" raw="coffee" | raw="of" raw="tea" )'
    pattern = '(pos="IN") (raw="a" raw="tea" | raw="a" raw="cup" raw="of" raw="coffee" | raw="an" raw="orange" raw="juice" ) !pos=";"'

    #pattern = '((raw="a" raw="cup" raw="of" raw="coffee")*| (raw="a" raw="tea" ))+'

    #pattern = '(raw="is") (( pos="JJ"* (pos="JJ" raw="and") (pos="JJ") )) (raw="to")'
    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [[{'pos': 'DT', 'raw': 'a'}, {'pos': 'NN', 'raw': 'cup'}, {'pos': 'IN', 'raw': 'of'}, {'pos': 'NN', 'raw': 'coffee'}], 1, 5]
        #self.test(description, method, lexicons, pattern, data, expected, verbosity)  
    expected = [[{'pos': 'DT', 'raw': 'a'}, {'pos': 'NN', 'raw': 'cup'}, {'pos': 'IN', 'raw': 'of'}, {'pos': 'NN', 'raw': 'coffee'}], 1, 5]

    result = pyrata.re.search(pattern, data, lexicons=lexicons, verbosity = verbosity)
    if result != None: result = result.groups[2] #group(2)

    #print ('Debug: type(result)=',result)
    if verbosity >0:
      print ()
      print ('Test:\t', description)
      print ('Method:\t', method) 
      print ('Lexicons:\t', lexicons)       
      print ('Pattern:\t', pattern)
      print ('Data:\t\t', data)
      print ('Expected groups:\t', expected)
      print ('Recognized groups:\t', result) 
    if result == expected:
      if verbosity >0:
        print ('Result:\tSUCCESS')
      self.testSuccess += 1
    else:
      if verbosity >0:
        print ('Result:\tFAIL')
    self.testCounter +=1

    if verbosity >0:
      print ()


  def test_search_alternative_groups_wi_unmatched_quantifiers_in_data(self, verbosity):
    if verbosity >0:
      print ('================================================')
    description = 'test_search_alternative_groups_wi_unmatched_quantifiers_in_data'
    method = 'search'
    group = [1]
    lexicons = {}
    pattern = '(pos="IN") (raw="a" raw="tea" | raw="a" raw="cup" raw="of"? raw="coffee" | raw="an" raw="orange"* raw="juice" )+ !pos=";"'

    data = [ {'raw':'Over', 'pos':'IN'},
      {'raw':'a', 'pos':'DT' }, 
      {'raw':'cup', 'pos':'NN' },
      {'raw':'of', 'pos':'IN'},
      {'raw':'coffee', 'pos':'NN'},
      {'raw':',', 'pos':','},
      {'raw':'Mr.', 'pos':'NNP'}, 
      {'raw':'Stone', 'pos':'NNP'},
      {'raw':'told', 'pos':'VBD'},
      {'raw':'his', 'pos':'PRP$'}, 
      {'raw':'story', 'pos':'NN'} ]
    expected = [[{'pos': 'DT', 'raw': 'a'}, {'pos': 'NN', 'raw': 'cup'}, {'pos': 'IN', 'raw': 'of'}, {'pos': 'NN', 'raw': 'coffee'}], 1, 5]

    result = pyrata.re.search(pattern, data, lexicons=lexicons, verbosity = verbosity)
    if result != None: result = result.groups[2] #group(2)

    #print ('Debug: type(result)=',result)
    if verbosity >0:
      print ()
      print ('Test:\t', description)
      print ('Method:\t', method) 
      print ('Lexicons:\t', lexicons)       
      print ('Pattern:\t', pattern)
      print ('Data:\t\t', data)
      print ('Expected groups:\t', expected)
      print ('Recognized groups:\t', result) 
    if result == expected:
      if verbosity >0:
        print ('Result:\tSUCCESS')
      self.testSuccess += 1
    else:
      if verbosity >0:
        print ('Result:\tFAIL')
    self.testCounter +=1

    if verbosity >0:
      print ()

  def test_search_groups_wi_matched_quantifiers_in_data(self, verbosity):
    if verbosity >0:
      print ('================================================')
    description = 'test_search_groups_wi_matched_quantifiers_in_data'
    method = 'search'
    group = [1]
    lexicons = {}
    #pattern = '(pos="VB" pos="DT"? pos="JJ"* pos="NN" pos="."|pos="FAKE")+' # Debug: p[0]=[[[None, 'pos="VB" '], ['?', 'pos="DT"'], ['*', 'pos="JJ"'], [None, 'pos="NN" '], [None, 'pos="."']], [[None, 'pos="FAKE"']]]

    pattern = '(pos="VB" pos="DT"? pos="JJ"* pos="NN" pos=".")+' # Debug: p[0]=['(pos="VB" pos="DT"? pos="JJ"* pos="NN" pos=".")']


    # Choose Life. Choose a job. Choose a career. Choose a family. Choose a fucking big television, choose washing machines, cars, compact disc players and electrical tin openers. Choose good health, low cholesterol, and dental insurance. 
    data = [ {'raw':'Choose', 'pos':'VB'},
      {'raw':'Life', 'pos':'NN' }, 
      {'raw':'.', 'pos':'.' },
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'job', 'pos':'NN'},
      {'raw':'.', 'pos':'.'}, 
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'career', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'},
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'family', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'},
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'fucking', 'pos':'JJ'}, 
      {'raw':'big', 'pos':'JJ'},             
      {'raw':'television', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'}  
      ]
    expected = [ {'raw':'Choose', 'pos':'VB'},
      {'raw':'Life', 'pos':'NN' }, 
      {'raw':'.', 'pos':'.' },
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'job', 'pos':'NN'},
      {'raw':'.', 'pos':'.'}, 
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'career', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'},
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'family', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'},
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'fucking', 'pos':'JJ'}, 
      {'raw':'big', 'pos':'JJ'},             
      {'raw':'television', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'}  
      ]
    result = pyrata.re.search(pattern, data, lexicons=lexicons, verbosity = verbosity)
    if result != None: result = result.group(0) #group(2)

    #print ('Debug: type(result)=',result)
    if verbosity >0:
      print ()
      print ('Test:\t', description)
      print ('Method:\t', method) 
      print ('Lexicons:\t', lexicons)       
      print ('Pattern:\t', pattern)
      print ('Data:\t\t', data)
      print ('Expected groups:\t', expected)
      print ('Recognized groups:\t', result) 
    if result == expected:
      if verbosity >0:
        print ('Result:\tSUCCESS')
      self.testSuccess += 1
    else:
      if verbosity >0:
        print ('Result:\tFAIL')
    self.testCounter +=1

    if verbosity >0:
      print ()


  def test_search_alternatives_groups_wi_matched_quantifiers_in_data(self, verbosity):
    if verbosity >0:
      print ('================================================')
    description = 'test_search_alternatives_groups_wi_matched_quantifiers_in_data'
    method = 'search'
    group = [1]
    lexicons = {}
    pattern = '(pos="VB" pos="DT"? pos="JJ"* pos="NN" pos="."|pos="FAKE")+' # Debug: p[0]=[[[None, 'pos="VB" '], ['?', 'pos="DT"'], ['*', 'pos="JJ"'], [None, 'pos="NN" '], [None, 'pos="."']], [[None, 'pos="FAKE"']]]



    # Choose Life. Choose a job. Choose a career. Choose a family. Choose a fucking big television, choose washing machines, cars, compact disc players and electrical tin openers. Choose good health, low cholesterol, and dental insurance. 
    data = [ {'raw':'Choose', 'pos':'VB'},
      {'raw':'Life', 'pos':'NN' }, 
      {'raw':'.', 'pos':'.' },
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'job', 'pos':'NN'},
      {'raw':'.', 'pos':'.'}, 
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'career', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'},
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'family', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'},
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'fucking', 'pos':'JJ'}, 
      {'raw':'big', 'pos':'JJ'},             
      {'raw':'television', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'}  
      ]
    expected = [ {'raw':'Choose', 'pos':'VB'},
      {'raw':'Life', 'pos':'NN' }, 
      {'raw':'.', 'pos':'.' },
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'job', 'pos':'NN'},
      {'raw':'.', 'pos':'.'}, 
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'career', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'},
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'family', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'},
      {'raw':'Choose', 'pos':'VB'},
      {'raw':'a', 'pos':'DT'},
      {'raw':'fucking', 'pos':'JJ'}, 
      {'raw':'big', 'pos':'JJ'},             
      {'raw':'television', 'pos':'NN'}, 
      {'raw':'.', 'pos':'.'}  
      ]
    result = pyrata.re.search(pattern, data, lexicons=lexicons, verbosity = verbosity)
    if result != None: result = result.group(0) #group(2)

    #print ('Debug: type(result)=',result)
    if verbosity >0:
      print ()
      print ('Test:\t', description)
      print ('Method:\t', method) 
      print ('Lexicons:\t', lexicons)       
      print ('Pattern:\t', pattern)
      print ('Data:\t\t', data)
      print ('Expected groups:\t', expected)
      print ('Recognized groups:\t', result) 
    if result == expected:
      if verbosity >0:
        print ('Result:\tSUCCESS')
      self.testSuccess += 1
    else:
      if verbosity >0:
        print ('Result:\tFAIL')
    self.testCounter +=1

    if verbosity >0:
      print ()

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Declare here all the tests you want to run
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

  def __init__(self):

    myverbosity = 2
    self.test_search_step_in_data(myverbosity)
    self.test_findall_step_in_data(myverbosity)
    self.test_finditer_step_in_data(myverbosity)

    self.test_search_step_absent_in_data(myverbosity)
    self.test_findall_step_absent_in_data(myverbosity)

    self.test_search_class_step_in_data(myverbosity)
    self.test_search_rich_class_step_in_data(myverbosity)

    self.test_findall_regex_step_in_data(myverbosity)
    self.test_findall_lexicon_step_in_data(myverbosity)
    self.test_findall_undefined_lexicon_step_in_data(myverbosity)

    self.test_findall_multiple_lexicon_step_in_data(myverbosity)

    self.test_search_optional_step_in_data(myverbosity)
    self.test_findall_optional_step_in_data(myverbosity)
    
    self.test_findall_step_step_in_data(myverbosity)

    self.test_findall_optional_step_step_in_data(myverbosity)
    self.test_findall_any_step_step_in_data(myverbosity)
    self.test_findall_at_least_one_step_step_in_data(myverbosity)

    self.test_findall_any_step_step_nbar_in_data(myverbosity)
    self.test_findall_at_least_one_step_step_nbar_in_data(myverbosity)

    self.test_findall_step_step_partially_matched_in_data_ending(myverbosity)
    self.test_findall_optional_step_step_partially_matched_in_data_ending(myverbosity)
    self.test_findall_any_step_step_partially_matched_in_data_ending(myverbosity)
    self.test_findall_at_least_one_step_step_partially_matched_in_data_ending(myverbosity)

    self.test_findall_step_at_least_one_not_step_step_in_data(myverbosity)
    self.test_findall_step_present_optional_step_step_in_data(myverbosity)
    self.test_findall_step_absent_optional_step_step_in_data(myverbosity)

    self.test_findall_step_optional_step_in_data(myverbosity)
    self.test_findall_step_any_step_in_data(myverbosity)
    self.test_findall_step_optinal_step_optional_step_step_in_data(myverbosity)

    self.test_findall_step_any_not_step1_step1_in_data(myverbosity)

    self.test_pattern_starting_with_the_first_token_of_data_present_as_expected_in_data(myverbosity)
    self.test_pattern_ending_with_the_last_token_of_data_present_as_expected_in_data(myverbosity)
    self.test_pattern_starting_with_the_first_token_of_data_and_ending_with_the_last_token_of_data_present_as_expected_in_data(myverbosity)
    self.test_pattern_starting_with_the_first_token_of_data_not_present_as_expected_in_data(myverbosity)
    self.test_pattern_ending_with_the_last_token_of_data_not_present_as_expected_in_data(myverbosity)
    self.test_pattern_starting_with_the_first_token_of_data_and_ending_with_the_last_token_of_data_not_present_as_expected_in_data(myverbosity)


    self.test_search_groups_in_data(myverbosity)

    self.test_annotate_default_action_sub_default_group_default_iob_annotation_dict_in_data(myverbosity)
    self.test_annotate_default_action_sub_default_group_default_iob_annotation_dict_not_in_data(myverbosity)
    self.test_annotate_default_action_sub_default_group_default_iob_annotation_dict_pattern_sequence_to_annotation_step_in_data(myverbosity)
    self.test_annotate_default_action_sub_group_one_default_iob_annotation_dict_pattern_in_data(myverbosity)
    self.test_annotate_default_action_sub_default_group_default_iob_annotation_empty_in_data(myverbosity)


    self.test_annotate_default_action_update_default_group_default_iob_annotation_dict_pattern_in_data(myverbosity)
    self.test_annotate_default_action_extend_default_group_default_iob_annotation_dict_pattern_in_data(myverbosity)
    self.test_annotate_default_action_extend_default_group_default_iob_annotation_sequence_of_dict_for_single_token_match_in_data(myverbosity)
    self.test_annotate_default_action_extend_default_group_iob_True_annotation_sequence_by_one_dict_in_data(myverbosity)


    self.test_search_alternative_groups_in_data(myverbosity)
    self.test_search_alternatives_groups_wi_matched_quantifiers_in_data(myverbosity)
    self.test_search_groups_wi_matched_quantifiers_in_data(myverbosity)


    

    #self.test_search_any_class_step_error_step_in_data(myverbosity)



    
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Run all the tests
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == '__main__':

  tests = TestPyrata()
  
  accuracy=tests.testSuccess/float(tests.testCounter)
  print ("PyRATA - testCounter=",tests.testCounter,'; testSuccess=',tests.testSuccess,'; accuracy=',accuracy)