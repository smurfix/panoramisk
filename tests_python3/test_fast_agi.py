import asyncio
from panoramisk.fast_agi import Application
import pytest

FAST_AGI_PAYLOAD = b'''agi_network: yes
agi_network_script: call_waiting
agi_request: agi://127.0.0.1:4574/call_waiting
agi_channel: SIP/xxxxxx-00000000
agi_language: en_US
agi_type: SIP
agi_uniqueid: 1437920906.0
agi_version: asterisk
agi_callerid: 201
agi_calleridname: user 201
agi_callingpres: 0
agi_callingani2: 0
agi_callington: 0
agi_callingtns: 0
agi_dnid: 9011
agi_rdnis: unknown
agi_context: default
agi_extension: 9011
agi_priority: 2
agi_enhanced: 0.0
agi_accountcode: default
agi_threadid: -1260881040
agi_arg_1: answered

'''


async def call_waiting(request):
    r = await request.send_command('ANSWER')
    assert {'message': None, 'result': 0, 'status_code': 200, 'value': None} == r


async def fake_asterisk_client(loop):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 4575, loop=loop)
    # send headers
    writer.write(FAST_AGI_PAYLOAD)
    # read it back
    msg_back = await reader.readline()
    writer.write(b'200 result=0\n')
    writer.close()
    return msg_back


@pytest.mark.asyncio
async def test_fast_agi_application(event_loop):
    fa_app = Application(loop=event_loop)
    fa_app.add_route('call_waiting', call_waiting)

    server = await asyncio.start_server(fa_app.handler, '127.0.0.1', 4575, loop=event_loop)

    msg_back = await fake_asterisk_client(loop=event_loop)
    assert b'ANSWER\n' == msg_back

    server.close()
    await server.wait_closed()
    await asyncio.sleep(1)  # Wait the end of endpoint
