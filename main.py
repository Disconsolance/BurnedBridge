from VK import LongPoll
import asyncio

if __name__ == '__main__':
	asyncio.run(LongPoll.listen())
# Written with hate. By Juno Arceneaux.
# Credits to Alexey Kuznetsov for the longpoll implementation.
