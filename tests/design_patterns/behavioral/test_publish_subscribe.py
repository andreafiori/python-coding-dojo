import unittest

from unittest.mock import patch, call
from python_algorithms.design_patterns.behavioral.publish_subscribe import Provider, Publisher, Subscriber

class TestProvider(unittest.TestCase):
    """
    Integration tests ~ provider class with as little mocking as possible.
    """

    def test_subscriber_shall_be_attachable_to_subscriptions(cls):
        subscription = 'sub msg'
        pro = Provider()
        cls.assertEqual(len(pro.subscribers), 0)
        sub = Subscriber('sub name', pro)
        sub.subscribe(subscription)
        cls.assertEqual(len(pro.subscribers[subscription]), 1)

    def test_subscriber_shall_be_detachable_from_subscriptions(cls):
        subscription = 'sub msg'
        pro = Provider()
        sub = Subscriber('sub name', pro)
        sub.subscribe(subscription)
        cls.assertEqual(len(pro.subscribers[subscription]), 1)
        sub.unsubscribe(subscription)
        cls.assertEqual(len(pro.subscribers[subscription]), 0)

    def test_publisher_shall_append_subscription_message_to_queue(cls):
        """ msg_queue ~ Provider.notify(msg) ~ Publisher.publish(msg) """
        expected_msg = 'expected msg'
        pro = Provider()
        pub = Publisher(pro)
        Subscriber('sub name', pro)
        cls.assertEqual(len(pro.msg_queue), 0)
        pub.publish(expected_msg)
        cls.assertEqual(len(pro.msg_queue), 1)
        cls.assertEqual(pro.msg_queue[0], expected_msg)

    def test_provider_shall_update_affected_subscribers_with_published_subscription(cls):
        pro = Provider()
        pub = Publisher(pro)
        sub1 = Subscriber('sub 1 name', pro)
        sub1.subscribe('sub 1 msg 1')
        sub1.subscribe('sub 1 msg 2')
        sub2 = Subscriber('sub 2 name', pro)
        sub2.subscribe('sub 2 msg 1')
        sub2.subscribe('sub 2 msg 2')
        with patch.object(sub1, 'run') as mock_subscriber1_run, patch.object(sub2, 'run') as mock_subscriber2_run:
            pro.update()
            cls.assertEqual(mock_subscriber1_run.call_count, 0)
            cls.assertEqual(mock_subscriber2_run.call_count, 0)
        pub.publish('sub 1 msg 1')
        pub.publish('sub 1 msg 2')
        pub.publish('sub 2 msg 1')
        pub.publish('sub 2 msg 2')
        with patch.object(sub1, 'run') as mock_subscriber1_run, patch.object(sub2, 'run') as mock_subscriber2_run:
            pro.update()
            expected_sub1_calls = [call('sub 1 msg 1'), call('sub 1 msg 2')]
            mock_subscriber1_run.assert_has_calls(expected_sub1_calls)
            expected_sub2_calls = [call('sub 2 msg 1'), call('sub 2 msg 2')]
            mock_subscriber2_run.assert_has_calls(expected_sub2_calls)

"""
>>> message_center = Provider()

>>> fftv = Publisher(message_center)

>>> jim = Subscriber("jim", message_center)
>>> jim.subscribe("cartoon")
>>> jack = Subscriber("jack", message_center)
>>> jack.subscribe("music")
>>> gee = Subscriber("gee", message_center)
>>> gee.subscribe("movie")
>>> vani = Subscriber("vani", message_center)
>>> vani.subscribe("movie")
>>> vani.unsubscribe("movie")

# Note that no one subscirbed to `ads`
# and that vani changed their mind

>>> fftv.publish("cartoon")
>>> fftv.publish("music")
>>> fftv.publish("ads")
>>> fftv.publish("movie")
>>> fftv.publish("cartoon")
>>> fftv.publish("cartoon")
>>> fftv.publish("movie")
>>> fftv.publish("blank")

>>> message_center.update()
jim got cartoon
jack got music
gee got movie
jim got cartoon
jim got cartoon
gee got movie
"""
