=========================
:mod:`panoramisk.testing`
=========================

..
    >>> import os
    >>> stream = os.path.join('tests', 'fixtures', 'ping.yaml')

.. code-block:: python

    >>> from trio_panoramisk import testing
    >>> import trio
    >>> async def run():
    >>>    manager = testing.Manager(stream=stream)  # stream is a filename containing an Asterisk trace
    >>>    resp = await manager.send_action({'Action': 'Ping'})
    >>>    assert 'ping' in resp
    >>>    assert resp.ping == 'Pong'
    >>> trio.run(run)

.. automodule:: panoramisk.testing

.. autoclass:: Manager
   :members:
