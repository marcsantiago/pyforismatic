# -*- coding: UTF-8 -*-

import arrow
import requests


class Quote(object):
  """
  Quote object, forming from given data
  """

  def __init__(self, data):
    self.__quote = data['quoteText']
    self.__author = data['quoteAuthor']
    self.__sender_name = data['senderName']
    self.__sender_link = data['senderLink']
    self.__datetime = arrow.now()

  @property
  def quote(self):
    return self.__quote

  @property
  def author(self):
    return self.__author

  @property
  def sender_name(self):
    return self.__sender_name

  @property
  def sender_link(self):
    return self.__sender_link

  @property
  def __recieved_datetime(self):
    return self.__datetime


class Forismatic(object):
  """
  Manager for getting quotes using Forismatic API (default = 1.0)
  Supports POST & GET methods, russian & english quotes

  """

  def __init__(self, api_url='http://api.forismatic.com/api/1.0/'):
    self.api_url = api_url


  def get_quote(self, lang='en', key=None):
    '''
    Method for retrieve quote

    '''

    str_key = str(key)

    # Validation of input data
    if key:
      if len(str_key) > 6:
        raise Exception('Key max length is 6')

    if lang not in ['en', 'ru']:
      raise Exception('Unknown language: %s' % lang)

    send_data = {
    'method': 'getQuote',
    'format': 'json',
    'lang': lang,
    'key': str_key if key else ""
    }

    response = requests.post(self.api_url, data=send_data)

    if response.status_code == 200:
      # Decoding JSON and fill Quote, if HTTP responce is OK
      try:
        retrieved_data = response.json()
      except ValueError:
        return None

      return Quote(data=retrieved_data)
    else:
      return None
