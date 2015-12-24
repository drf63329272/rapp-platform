#! /usr/bin/env python

#Copyright 2015 RAPP

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

import os
import sys
import unittest
import mock
import getpass
import time

import roslib
import rospy
import rostest

roslib.load_manifest("rapp_email")

from rapp_email import EmailReceiver

from rapp_platform_ros_communications.srv import (
  ReceiveEmailSrv,
  ReceiveEmailSrvRequest,
  ReceiveEmailSrvResponse
  )

from rapp_platform_ros_communications.msg import (
  MailMsg
  )

class TestEmailReceiver(unittest.TestCase):
  def setUp(self):
    serviceTopic = rospy.get_param("rapp_email_receive_topic")
    rospy.wait_for_service(serviceTopic)

    self._test_service = rospy.ServiceProxy(
        serviceTopic, ReceiveEmailSrv)

    self._email = raw_input()
    self._password = getpass.getpass("Enter password: ")
    self._server = raw_input("Enter server: ")
    self._port = raw_input("Enter port: ")

  @unittest.skip('Skipping email tests - Uncomment decorators to test manually')
  def test_checkDefaults(self):

    req = ReceiveEmailSrvRequest()
    req.email = self._email
    req.password = self._password
    req.server = self._server

    response = self._test_service( req )
    self.assertEquals( response.status, 0 )
    for emailMsg in response.emails:
      self.assertTrue(os.path.exists(emailMsg.bodyPath))
      for attach in emailMsg.attachmentPaths:
        self.assertTrue(os.path.exists(attach))

  @unittest.skip('Skipping email tests - Uncomment decorators to test manually')
  def test_fromDate(self):

    req = ReceiveEmailSrvRequest()
    req.email = self._email
    req.password = self._password
    req.server = self._server

    req.requestedEmailStatus = 'ALL'
    req.fromDate = int(time.time() - 5000000)

    response = self._test_service( req )
    self.assertEquals( response.status, 0 )
    for emailMsg in response.emails:
      self.assertTrue(os.path.exists(emailMsg.bodyPath))
      for attach in emailMsg.attachmentPaths:
        self.assertTrue(os.path.exists(attach))

  @unittest.skip('Skipping email tests - Uncomment decorators to test manually')
  def test_toDate(self):

    req = ReceiveEmailSrvRequest()
    req.email = self._email
    req.password = self._password
    req.server = self._server

    req.requestedEmailStatus = 'ALL'
    req.fromDate = int(time.time() - 5000000)
    req.toDate = int(time.time() - 1000000)

    response = self._test_service( req )
    self.assertEquals( response.status, 0 )
    for emailMsg in response.emails:
      self.assertTrue(os.path.exists(emailMsg.bodyPath))
      for attach in emailMsg.attachmentPaths:
        self.assertTrue(os.path.exists(attach))

  @unittest.skip('Skipping email tests - Uncomment decorators to test manually')
  def test_emailNumber(self):

    req = ReceiveEmailSrvRequest()
    req.email = self._email
    req.password = self._password
    req.server = self._server

    req.requestedEmailStatus = 'ALL'

    req.numberOfEmails = 2

    response = self._test_service( req )
    self.assertEquals( response.status, 0 )
    for emailMsg in response.emails:
      self.assertTrue(os.path.exists(emailMsg.bodyPath))
      for attach in emailMsg.attachmentPaths:
        self.assertTrue(os.path.exists(attach))


if __name__ == '__main__':
  rostest.rosrun('rapp_email', 'email_receiver_unit_tests', TestEmailReceiver)