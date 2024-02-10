# import asyncio
#
# import pytest
#
#
# @pytest.fixture(scope="session", autouse=True)
# def event_loop():
#     try:
#         loop = asyncio.get_running_loop()
#     except RuntimeError:
#         loop = asyncio.new_event_loop()
#     yield loop
#     loop.close()