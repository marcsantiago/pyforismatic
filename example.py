# -*- coding: UTF-8 -*-

# Just importing Forsimatic class
from forismatic import Forismatic

# Initializing manager
f = Forismatic()

# Getting Quote object & printing quote and author

q = f.get_quote()
if q:
  print '{0}\t{1}\n'.format(q.quote, q.author)
