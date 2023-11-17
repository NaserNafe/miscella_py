import ssl
import asyncio
from python_socks.async_.asyncio import Proxy


async def main():
    proxy = Proxy.from_url('socks5://user:password@127.0.0.1:1080')

    # `connect` returns standard Python socket in non-blocking mode
    # so we can pass it to asyncio.open_connection(...)
    sock = await proxy.connect(dest_host='check-host.net', dest_port=443)

    reader, writer = await asyncio.open_connection(
        host=None,
        port=None,
        sock=sock,
        ssl=ssl.create_default_context(),
        server_hostname='check-host.net',
    )

    request = (
        b'GET /ip HTTP/1.1\r\n'
        b'Host: check-host.net\r\n'
        b'Connection: close\r\n\r\n'
    )

    writer.write(request)
    response = await reader.read(-1)
    print(response)

if __name__ == '__main__':
    main()
