#!/usr/bin/env python
# init_py_dont_write_bytecode

import os, sys
import unittest
from operate_google_calendar import *
import datetime
from pprint import pprint


# settings file, credential file, token files
CALENDAR_SCOPES = 'https://www.googleapis.com/auth/calendar'
CWD = os.path.dirname(os.path.abspath(__file__))
TOKEN_JSON_PATH = os.path.join(CWD,'token.json')
CREDENTIAL_JSON_PATH = os.path.join(CWD,'credential.json')

print('token.json path: %s' % TOKEN_JSON_PATH)
print('credential.json path: %s'% CREDENTIAL_JSON_PATH)



# create shortcut less confusing
datetime2 = datetime.datetime
datetime2_now = datetime2.now
DATE_FMT_STRING = '%Y-%m-%d'
get_day = lambda x: (datetime.date.today()+datetime.timedelta(days=x)).strftime(DATE_FMT_STRING)

TODAY = get_day(0)
TODAY_AND_1 = get_day(1)
TODAY_AND_2 = get_day(2)
TODAY_AND_7 = get_day(7)
TEST_TIMEZONE = 'Asia/Hong_Kong'
TEST_CALENDAR = 'test_calendar_list'

LOREM_IPSUM_TEST_MSG = '''What is Lorem Ipsum?< @louis.law >
#sandbox
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a gal
<http://www.google.com|www.google.com>
louis.law@tinklabs.com
的苦或體，年引標關死每除又那科可親條開的不
# NOTE: ㊙ ️I would like to ...
# TODO: 🤦 Temporary solution ...
# QUESTION?: 🤔 What is the opinion about ... ??
'''

TEST_BASIC_EVENT = {
  'summary': 'test_event summary',
  'location': 'test_event_location',
  'description': LOREM_IPSUM_TEST_MSG,
  'start': {'date':TODAY,'timeZone': TEST_TIMEZONE,},
  'end': {'date':TODAY_AND_1,'timeZone': TEST_TIMEZONE,},
  'attendees': [
    {'email': 'people1@example.com'},
    {'email': 'people2@example.com'},
  ],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}


def setUpModule():
    print('setup (topic) module')
def tearDownModule():
    print('teardown (topic) module')

class TestGoogleCalendar(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setup (topic) class')

    @classmethod
    def tearDownClass(cls):
        print('teardown (topic) class')

    def setUp(self):
        print('setup (topic) test')

    def tearDown(self):
        print('teardown (topic) test')

    def test_get_user_calendar_list(self, calendar_wanted = TEST_CALENDAR):
        ERROR_MSG = 'the wanted calendar not in list'
        google_service = self.test_login_oauth()
        calendar_list = google_service.get_user_calendar_list()
        pprint(calendar_list)
        self.assertIn(calendar_wanted,calendar_list.keys(),ERROR_MSG)
        return calendar_list

    def test_get_calendar_id(self, calendar_wanted=TEST_CALENDAR):
        calendar_list = self.test_get_user_calendar_list(calendar_wanted)
        return calendar_list[calendar_wanted]

    def test_login_oauth(self):
        google_service = google_calendar_helper(TOKEN_JSON_PATH, CREDENTIAL_JSON_PATH, CALENDAR_SCOPES)
        return google_service

    def test_insert_basic_event_into_calendar(self, target_calendar_name=TEST_CALENDAR):
        google_service = self.test_login_oauth()
        google_service.insert_event_into_calendar(target_calendar_name, TEST_BASIC_EVENT)

    # def test_getting_calendar_list(self):


    # def test_create_event(self):
    #     print("hello (topic)")
    #     self.assertEqual(1/0, 1)




if __name__ == '__main__':
    unittest.main(verbosity=2)
